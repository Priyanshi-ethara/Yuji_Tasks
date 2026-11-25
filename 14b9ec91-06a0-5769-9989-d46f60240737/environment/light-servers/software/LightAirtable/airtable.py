import random
import re
from typing import Dict, List, Any
from pathlib import Path
import yaml
import sys
from datetime import datetime

WORK_DIR = Path('.').__str__()
if WORK_DIR not in sys.path:
    sys.path.append(WORK_DIR)

from software.utils.core import OSConnector, DummyOSConnector, connect_os
from software.utils.world_snapshot import restore_into, seed_mode, resolve_seed
from software.utils.time import TimeMachine

CORPUS_PATH = Path(__file__).resolve().parent / "corpus"

# ----------------------------------------------------------------------------------------------
# Task world rule (Northfell Grid day-ahead ratings). Flags are files in ATLAS_EVENT_DIR, read at
# call time; every value below is fixed (no clock, no randomness).
import json as _wr_json
import os as _wr_os
import pathlib as _wr_pathlib


def _wr_dir():
    return _wr_pathlib.Path(_wr_os.environ.get("ATLAS_EVENT_DIR", "/tmp/atlas_events"))


def _wr_fire(name):
    d = _wr_dir()
    d.mkdir(parents=True, exist_ok=True)
    (d / name).touch()


def _wr_fired(name):
    return (_wr_dir() / name).exists()

# A distinct circuit row of the Next-Day Ratings register counts once it receives any accepted
# non-empty write. After the first such row MetDesk's Skelwith Edge reissue becomes visible; after
# the 21st (of 22) the warm-front revision does. No register record changes on its own.
_WR_TABLE = "tblNFGRATE000001"
_WR_ROWS = set(_wr_json.loads("[\"recNFR01skbr100\", \"recNFR02skbr200\", \"recNFR03sktn100\", \"recNFR04cfln100\", \"recNFR05cfhg100\", \"recNFR06cfbr100\", \"recNFR07hgtn100\", \"recNFR08hgox100\", \"recNFR09lnbr100\", \"recNFR10lnbr200\", \"recNFR11lnox100\", \"recNFR12brtn100\", \"recNFR13brtn200\", \"recNFR14brms100\", \"recNFR15tnox100\", \"recNFR16tnqy100\", \"recNFR17oxfd100\", \"recNFR18oxfd200\", \"recNFR19lnks100\", \"recNFR20brwd100\", \"recNFR21mswd100\", \"recNFR22ksfd100\"]"))
_WR_STEPS = (("nfg_skelwith_reissue", 1), ("nfg_warm_front", 21))


def _wr_note_write(table_id, record_id, fields):
    # Rows already written are kept as marker files in ATLAS_EVENT_DIR (not in process memory), so the count
    # survives a server restart and repeated writes to one row count once.
    if table_id != _WR_TABLE or record_id not in _WR_ROWS:
        return
    if not any(v not in (None, "") for v in (fields or {}).values()):
        return
    _wr_fire("nfg_row_" + record_id)
    seen = sum(1 for r in _WR_ROWS if _wr_fired("nfg_row_" + r))
    for flag, n in _WR_STEPS:
        if seen >= n and not _wr_fired(flag):
            _wr_fire(flag)


def _to_bool(v) -> bool:
    return str(v).strip().lower() == "true"


# Very small filterByFormula support: {Field}='Value' (also "=" with double quotes)
_FORMULA_RE = re.compile(r"^\{(?P<field>[^}]+)\}\s*=\s*(['\"])(?P<value>.*)\2$")


class AirtableSession:
    """Deterministic sandbox for the Airtable mock, ported from the FastAPI service.

    Records are modeled generically as {id, createdTime, fields:{...}}. Field
    value casting is driven by the field type declared in the corpus fields
    table (number -> float/int, checkbox -> bool); everything else stays a string.
    """

    def __init__(self, os_cfg, seed=None):
        # Seedless: world loaded verbatim from a frozen snapshot next to
        # this module; `seed` is accepted for client compat and ignored.
        if seed_mode():
            # Seed architecture: world rolled from a seed (re-armed).
            self.rng = random.Random(resolve_seed(seed))
            self.os = connect_os(os_cfg)
            self.time_machine = TimeMachine(rng=self.rng)

            from software.utils.world_data import load_state as _load_state
            _load_state(self, 'LightAirtable')
        else:
            # Seedless: world loaded verbatim from the frozen snapshot.
            restore_into(self, Path(__file__).resolve().parent / "world.pkl")
            self.os = connect_os(os_cfg)

    def get_session_dict(self):
        return {"records": self.records}

    # --- helpers -----------------------------------------------------------
    def _now(self) -> str:
        return self.os.now()

    def uuid(self) -> str:
        alphabet = "0123456789abcdef"
        return "rec" + ''.join(self.rng.choices(alphabet, k=14))

    def _cast_field(self, table_id, name, value):
        ftype = self._field_types.get(table_id, {}).get(name)
        if value == "" or value is None:
            return None if ftype in ("number",) else value
        if ftype == "number":
            try:
                f = float(value)
                return int(f) if f.is_integer() else f
            except (TypeError, ValueError):
                return value
        if ftype == "checkbox":
            return _to_bool(value)
        return value

    def _coerce_records(self, table_id, rows):
        out = []
        for r in rows:
            fields = {}
            for k, v in r.items():
                if k in ("id", "createdTime"):
                    continue
                cast = self._cast_field(table_id, k, v)
                if cast is None:
                    continue
                fields[k] = cast
            out.append({
                "id": r["id"],
                "createdTime": r["createdTime"],
                "fields": fields,
            })
        return out

    def _resolve_table(self, base_id, table_id_or_name):
        for t in self.tables:
            if t.get("baseId", t.get("base_id")) != base_id:
                continue
            if t["id"] == table_id_or_name or t["name"].lower() == str(table_id_or_name).lower():
                return t
        return None

    def _apply_formula(self, records, formula):
        if not formula:
            return records
        m = _FORMULA_RE.match(formula.strip())
        if not m:
            return records
        field = m.group("field")
        value = m.group("value")
        out = []
        for rec in records:
            fv = rec["fields"].get(field)
            if fv is None:
                continue
            if str(fv) == value:
                out.append(rec)
        return out

    # --- API methods -------------------------------------------------------
    def list_bases(self) -> Dict[str, Any]:
        return {"status": "ok", "output": {"bases": [{
            "id": b["id"], "name": b["name"],
            "permissionLevel": b.get("permissionLevel", b.get("permission_level")),
        } for b in self.bases]}}

    def list_tables(self, base_id: str) -> Dict[str, Any]:
        if not any(b["id"] == base_id for b in self.bases):
            return {"status": "failed", "output": f"Base {base_id} not found"}
        tables = []
        for t in self.tables:
            if t.get("baseId", t.get("base_id")) != base_id:
                continue
            tables.append({
                "id": t["id"],
                "name": t["name"],
                "primaryFieldId": t.get("primaryFieldId", t.get("primary_field_id", "")),
                # _field_meta is never populated in seed mode (stock defect); fall back to the table's declared fields
                "fields": getattr(self, "_field_meta", {}).get(t["id"]) or t.get("fields", []),
            })
        return {"status": "ok", "output": {"tables": tables}}

    def list_records(self, base_id: str, table_id_or_name: str, page_size: int = 100,
                     offset: str | None = None, filter_by_formula: str | None = None) -> Dict[str, Any]:
        table = self._resolve_table(base_id, table_id_or_name)
        if not table:
            return {"status": "failed", "output": f"Table {table_id_or_name} not found in base {base_id}"}
        records = self.records.get(table["id"], [])
        records = self._apply_formula(records, filter_by_formula)

        page_size = max(1, min(int(page_size), 100))
        try:
            start = int(offset) if offset is not None else 0
        except (TypeError, ValueError):
            start = 0
        page = records[start: start + page_size]
        resp = {"records": page}
        next_offset = start + page_size
        if next_offset < len(records):
            resp["offset"] = str(next_offset)
        return {"status": "ok", "output": resp}

    def get_record(self, base_id: str, table_id_or_name: str, record_id: str) -> Dict[str, Any]:
        table = self._resolve_table(base_id, table_id_or_name)
        if not table:
            return {"status": "failed", "output": f"Table {table_id_or_name} not found in base {base_id}"}
        for rec in self.records.get(table["id"], []):
            if rec["id"] == record_id:
                return {"status": "ok", "output": rec}
        return {"status": "failed", "output": f"Record {record_id} not found"}

    def create_records(self, base_id: str, table_id_or_name: str, records: List[Dict[str, Any]]) -> Dict[str, Any]:
        table = self._resolve_table(base_id, table_id_or_name)
        if not table:
            return {"status": "failed", "output": f"Table {table_id_or_name} not found in base {base_id}"}
        created = []
        rows = self.records.setdefault(table["id"], [])
        for item in records:
            fields = item.get("fields", {}) or {}
            rec = {
                "id": self.uuid(),
                "createdTime": self._now(),
                "fields": dict(fields),
            }
            rows.append(rec)
            created.append(rec)
        return {"status": "ok", "output": {"records": created}}

    def update_record(self, base_id: str, table_id_or_name: str, record_id: str,
                      fields: Dict[str, Any]) -> Dict[str, Any]:
        table = self._resolve_table(base_id, table_id_or_name)
        if not table:
            return {"status": "failed", "output": f"Table {table_id_or_name} not found in base {base_id}"}
        for rec in self.records.get(table["id"], []):
            if rec["id"] == record_id:
                rec["fields"] = {**rec["fields"], **(fields or {})}
                _wr_note_write(table["id"], record_id, fields)
                return {"status": "ok", "output": rec}
        return {"status": "failed", "output": f"Record {record_id} not found"}

    def delete_record(self, base_id: str, table_id_or_name: str, record_id: str) -> Dict[str, Any]:
        table = self._resolve_table(base_id, table_id_or_name)
        if not table:
            return {"status": "failed", "output": f"Table {table_id_or_name} not found in base {base_id}"}
        rows = self.records.get(table["id"], [])
        for i, rec in enumerate(rows):
            if rec["id"] == record_id:
                rows.pop(i)
                return {"status": "ok", "output": {"id": record_id, "deleted": True}}
        return {"status": "failed", "output": f"Record {record_id} not found"}


if __name__ == "__main__":
    s = AirtableSession(seed=12)
    print(s.list_bases())
    print(s.list_tables("appNW1studio0001"))
