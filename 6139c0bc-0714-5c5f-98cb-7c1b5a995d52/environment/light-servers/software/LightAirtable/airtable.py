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


def _to_bool(v) -> bool:
    return str(v).strip().lower() == "true"


# Very small filterByFormula support: {Field}='Value' (also "=" with double quotes)
_FORMULA_RE = re.compile(r"^\{(?P<field>[^}]+)\}\s*=\s*(['\"])(?P<value>.*)\2$")

# ======================================================================================
# task world rule (T02 FY2026 Scope 2 inventory) — cross-app live events
# Apps run as separate processes; they signal each other through flag files.
import os as _t02_os, pathlib as _t02_pl, functools as _t02_ft


def _t02_ev():
    # the event directory is read from the environment at call time
    return _t02_pl.Path(_t02_os.environ.get("ATLAS_EVENT_DIR", "/tmp/atlas_events"))


def _t02_fire(name):
    _t02_ev().mkdir(parents=True, exist_ok=True)
    (_t02_ev() / name).touch()


def _t02_fired(name):
    return (_t02_ev() / name).exists()

_T02_CHANGES = {'NRR-2026-0233-SOL': {'Status': 'Retirement reversed', 'Retired on': '', 'Claim period': '', 'Site claimed': '', 'Beneficiary': '', 'Retirement note': "Retirement reversed by NRR on 2026-11-11 under issuance-error notice IE-2026-117: serials 2026-0233-000001 to 2026-0233-004800 of Ocmulgee Solar Farm were issued twice for the same generation; the duplicate batch is void and its retirement for Talvik Precision Components Inc. (FY2026, TPC-08 Macon) is cancelled. Replacement certificates will be issued under a new ID once the generator's meter data is re-validated (expected Q1 2027)."}, 'NRR-2026-0091-SOL': {'Status': 'Retired', 'Retired on': '2026-11-11', 'Claim period': 'FY2026', 'Site claimed': 'TPC-06 Elkhart', 'Beneficiary': 'Talvik Precision Components Inc.', 'Retirement note': 'Retired 2026-11-11 ahead of the December window on the written instruction of M. Ostrowski dated 2026-11-10 (Greenledger ticket GL-RT-5521); beneficiary Talvik Precision Components Inc.; claim period FY2026; site claimed TPC-06 Elkhart.'}}
_T02_NOTICES = [{'id': 'recT02N099', 'createdTime': '2026-11-11T09:40:00.000Z', 'fields': {'Notice': 'IE-2026-117', 'Date': '2026-11-11', 'Registry': 'NRR', 'Certificate ID': 'NRR-2026-0233-SOL', 'Text': "Retirement reversed by NRR on 2026-11-11 under issuance-error notice IE-2026-117: serials 2026-0233-000001 to 2026-0233-004800 of Ocmulgee Solar Farm were issued twice for the same generation; the duplicate batch is void and its retirement for Talvik Precision Components Inc. (FY2026, TPC-08 Macon) is cancelled. Replacement certificates will be issued under a new ID once the generator's meter data is re-validated (expected Q1 2027)."}}, {'id': 'recT02N098', 'createdTime': '2026-11-11T09:40:00.000Z', 'fields': {'Notice': 'RN-2026-1112', 'Date': '2026-11-11', 'Registry': 'NRR', 'Certificate ID': 'NRR-2026-0091-SOL', 'Text': 'Retired 2026-11-11 ahead of the December window on the written instruction of M. Ostrowski dated 2026-11-10 (Greenledger ticket GL-RT-5521); beneficiary Talvik Precision Components Inc.; claim period FY2026; site claimed TPC-06 Elkhart.'}}]
# ======================================================================================


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
        # stock defect: _field_types is never set in seed mode; derive it from the tables' own field list
        types = getattr(self, "_field_types", None)
        if not isinstance(types, dict):
            types = {t["id"]: {f.get("name"): f.get("type") for f in (t.get("fields") or []) if isinstance(f, dict)}
                     for t in getattr(self, "tables", []) if isinstance(t, dict) and t.get("id")}
        ftype = types.get(table_id, {}).get(name)
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

    # ---- task world rule (T02): once eight distinct FY2026 inventory items have been written, the nightly
    # registry sync lands two changes in the mirror: NRR reverses one FY2026 retirement (issuance error) and
    # the broker's brought-forward retirement of another certificate is executed; each comes with a registry
    # notice (applied once per session, before every tool call and before the sign-out dump).
    def _t02_apply(self):
        if self.__dict__.get("_t02_done") or not _t02_fired("t02_reversal"):
            return
        self.__dict__["_t02_done"] = True
        for rec in self.records.get("tblT02Certs", []):
            change = _T02_CHANGES.get(rec.get("fields", {}).get("Certificate ID"))
            if change:
                rec["fields"] = {**rec["fields"], **change}
        notes = self.records.setdefault("tblT02Notices", [])
        have = {r.get("id") for r in notes}
        for n in _T02_NOTICES:
            if n["id"] not in have:
                notes.append({"id": n["id"], "createdTime": n["createdTime"], "fields": dict(n["fields"])})

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
                # stock defect: _field_meta is never set in seed mode; fall back to the table's own field list
                "fields": (getattr(self, "_field_meta", None) or {}).get(t["id"]) or t.get("fields", []),
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




def _t02_guarded(fn):
    @_t02_ft.wraps(fn)
    def inner(self, *a, **k):
        self._t02_apply()
        return fn(self, *a, **k)
    return inner


for _t02_n, _t02_f in list(vars(AirtableSession).items()):
    if callable(_t02_f) and _t02_n != "_t02_apply" and (not _t02_n.startswith("_") or _t02_n == "get_session_dict"):
        setattr(AirtableSession, _t02_n, _t02_guarded(_t02_f))
# ======================================================================================

if __name__ == "__main__":
    s = AirtableSession(seed=12)
    print(s.list_bases())
    print(s.list_tables("appNW1studio0001"))
