import random
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



# ======================================================================================
# TASK WORLD RULE (Kestrel-3 technical-file ToC task) - live events shared through flag
# files in ATLAS_EVENT_DIR (read at call time). Deterministic content, fixed ids/stamps.
#   ks3_ev1_register : fired by LightAirtable when the first ToC row is written
#   ks3_ev2_release  : fired by LightAirtable when the 29th distinct ToC row is written
# ======================================================================================
import os as _tw_os
import pathlib as _tw_pl


def _tw_dir():
    return _tw_pl.Path(_tw_os.environ.get("ATLAS_EVENT_DIR", "/tmp/atlas_events"))


def _tw_fired(name):
    return (_tw_dir() / name).exists()


def _tw_fire(name):
    d = _tw_dir()
    d.mkdir(parents=True, exist_ok=True)
    (d / name).touch()


class ServicenowSession:

    # ---- task world rule: apply pending live events before every public call ----
    def __getattribute__(self, name):
        attr = object.__getattribute__(self, name)
        if not name.startswith("_") and callable(attr):
            object.__getattribute__(self, "_tw_apply")()
        return attr

    def _tw_apply(self):
        """Task world rule, event 2: change request CHG0041187 closed as implemented."""
        st = self.__dict__
        if st.get("_tw_ev2") or "changes" not in st or not _tw_fired("ks3_ev2_release"):
            return
        st["_tw_ev2"] = True
        if any(c.get("number") == "CHG0041187" for c in st["changes"]):
            return
        st["changes"].append({
            "sys_id": "chg_ks3_41187", "number": "CHG0041187",
            "short_description": "Document release - DOC-1047 Rev F (Risk Management Report, 52 pp, open placeholders 0; Q3 complaint trend and benefit-risk chapter 9) and DOC-1188 Rev C (Stability Study Report, 31 pp, open placeholders 0; 18-month real-time and in-use data) into the Kestrel-3 controlled store; CCB approved 2026-11-13; released by R. Montoya (QA) while document control is on leave; implemented 2026-11-16 09:40",
            "state": "Closed", "type": "normal", "category": "Document release", "assigned_to": "sn_ks3_rm",
            "opened_at": "2026-11-16 09:30:00"})

    """Deterministic sandbox for the ServiceNow Table API mock, ported from the FastAPI service.

    State is loaded from the corpus at init; subsequent calls read and mutate the
    in-memory tables so repeated calls within a session stay consistent.
    """

    # state numeric codes used by the incident table
    INCIDENT_STATES = {"1": "New", "2": "In Progress", "3": "On Hold", "6": "Resolved", "7": "Closed"}

    def __init__(self, os_cfg, seed=None):
        # Seedless: world loaded verbatim from a frozen snapshot next to
        # this module; `seed` is accepted for client compat and ignored.
        if seed_mode():
            # Seed architecture: world rolled from a seed (re-armed).
            self.rng = random.Random(resolve_seed(seed))
            self.os = connect_os(os_cfg)
            self.time_machine = TimeMachine(rng=self.rng)

            from software.utils.world_data import load_state as _load_state
            _load_state(self, 'LightServiceNow')
        else:
            # Seedless: world loaded verbatim from the frozen snapshot.
            restore_into(self, Path(__file__).resolve().parent / "world.pkl")
            self.os = connect_os(os_cfg)

    def get_session_dict(self):
        return {"incidents": self.incidents, "changes": self.changes}

    # --- helpers -----------------------------------------------------------
    def _now(self) -> str:
        return self.os.now()

    def uuid(self) -> str:
        alphabet = "0123456789abcdef"
        return ''.join(self.rng.choices(alphabet, k=32))

    def _find(self, rows, sys_id):
        return next((r for r in rows if r["sys_id"] == sys_id), None)

    def _parse_query(self, sysparm_query):
        conditions = []
        if not sysparm_query:
            return conditions
        for clause in sysparm_query.split("^"):
            clause = clause.strip()
            if not clause or "=" not in clause:
                continue
            field, _, value = clause.partition("=")
            conditions.append((field.strip(), value.strip()))
        return conditions

    def _apply_query(self, rows, sysparm_query, sysparm_limit=None):
        conditions = self._parse_query(sysparm_query)
        results = list(rows)
        for field, value in conditions:
            results = [r for r in results if str(r.get(field, "")) == value]
        if sysparm_limit is not None:
            try:
                limit = int(sysparm_limit)
                results = results[:limit]
            except (TypeError, ValueError):
                pass
        return results

    # --- Incidents ---------------------------------------------------------
    def list_incidents(self, sysparm_query: str | None = None,
                       sysparm_limit: int | None = None) -> Dict[str, Any]:
        return {"status": "ok", "output": self._apply_query(self.incidents, sysparm_query, sysparm_limit)}

    def get_incident(self, sys_id: str) -> Dict[str, Any]:
        rec = self._find(self.incidents, sys_id)
        if not rec:
            return {"status": "failed", "output": f"Incident {sys_id} not found"}
        return {"status": "ok", "output": rec}

    def create_incident(self, short_description: str, description: str | None = None,
                        priority: str = "3", impact: str = "3", urgency: str = "3",
                        category: str = "inquiry", assigned_to: str | None = None,
                        opened_by: str | None = None) -> Dict[str, Any]:
        if not short_description:
            return {"status": "failed", "output": "short_description is required"}
        now = self._now()
        seq = 1001 + len(self.incidents)
        rec = {
            "sys_id": self.uuid(),
            "number": f"INC{seq:07d}",
            "short_description": short_description,
            "description": description or "",
            "state": "1",
            "priority": str(priority),
            "impact": str(impact),
            "urgency": str(urgency),
            "category": category or "inquiry",
            "assigned_to": assigned_to or "",
            "opened_by": opened_by or "",
            "opened_at": now,
            "updated_at": now,
        }
        self.incidents.append(rec)
        return {"status": "ok", "output": rec}

    def update_incident(self, sys_id: str, short_description: str | None = None,
                        description: str | None = None, state: str | None = None,
                        priority: str | None = None, impact: str | None = None,
                        urgency: str | None = None, category: str | None = None,
                        assigned_to: str | None = None) -> Dict[str, Any]:
        rec = self._find(self.incidents, sys_id)
        if not rec:
            return {"status": "failed", "output": f"Incident {sys_id} not found"}
        fields = {
            "short_description": short_description,
            "description": description,
            "state": state,
            "priority": priority,
            "impact": impact,
            "urgency": urgency,
            "category": category,
            "assigned_to": assigned_to,
        }
        for key in ("short_description", "description", "state", "priority", "impact",
                    "urgency", "category", "assigned_to"):
            val = fields.get(key)
            if val is not None:
                rec[key] = str(val)
        rec["updated_at"] = self._now()
        return {"status": "ok", "output": rec}

    # --- Change requests ---------------------------------------------------
    def list_change_requests(self, sysparm_query: str | None = None,
                             sysparm_limit: int | None = None) -> Dict[str, Any]:
        return {"status": "ok", "output": self._apply_query(self.changes, sysparm_query, sysparm_limit)}

    def get_change_request(self, sys_id: str) -> Dict[str, Any]:
        rec = self._find(self.changes, sys_id)
        if not rec:
            return {"status": "failed", "output": f"Change request {sys_id} not found"}
        return {"status": "ok", "output": rec}

    # --- Problems ----------------------------------------------------------
    def list_problems(self, sysparm_query: str | None = None,
                      sysparm_limit: int | None = None) -> Dict[str, Any]:
        return {"status": "ok", "output": self._apply_query(self.problems, sysparm_query, sysparm_limit)}

    def get_problem(self, sys_id: str) -> Dict[str, Any]:
        rec = self._find(self.problems, sys_id)
        if not rec:
            return {"status": "failed", "output": f"Problem {sys_id} not found"}
        return {"status": "ok", "output": rec}

    # --- Users -------------------------------------------------------------
    def list_users(self, sysparm_query: str | None = None,
                   sysparm_limit: int | None = None) -> Dict[str, Any]:
        return {"status": "ok", "output": self._apply_query(self.users, sysparm_query, sysparm_limit)}

    def get_user(self, sys_id: str) -> Dict[str, Any]:
        rec = self._find(self.users, sys_id)
        if not rec:
            return {"status": "failed", "output": f"User {sys_id} not found"}
        return {"status": "ok", "output": rec}



    def delete_incident(self, sys_id: str) -> dict:
        rec = self._find(self.incidents, sys_id)
        if not rec:
            return {"status": "failed", "output": f"Incident {sys_id} not found"}
        self.incidents.remove(rec)
        return {"status": "ok", "output": {}}

if __name__ == "__main__":
    s = ServicenowSession(seed=12)
    print(s.list_incidents())
    print(s.get_user("usr-amelia"))
