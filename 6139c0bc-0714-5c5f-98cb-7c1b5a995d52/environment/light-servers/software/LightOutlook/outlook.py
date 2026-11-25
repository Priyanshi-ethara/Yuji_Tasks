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

_ME_NAME = "Alex Carter"
_ME_ADDRESS = "alex.carter@contoso.com"

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

_T02_MAIL = {'id': 'AAMkT02msg0099', 'subject': 'Reissued invoices KEV-RE-26-0819 (TPC-19 Leipzig, August) and KEV-RE-26-0918 (TPC-18 Stuttgart, September)', 'from_name': 'Henrik Bauer', 'from_address': 'h.bauer@kessler-energie.example', 'to_name': 'Carbon Accounting Desk', 'to_address': 'alex.carter@contoso.com', 'bodyPreview': "Dear desk, following Ms Vogel's query our metering team confirmed that billing still used the old CT ratio 200/5 after the transformer change on 3 August; the correct ratio is 250/5. Invoice KEV-26-0819 (464,000 kWh) is cancelled and replaced by reissued invoice KEV-RE-26-0819 for account KEV-DE-71388, period 2026-08-01 to 2026-08-31: 371,200 kWh, actual read. Checking your other account after our billing-platform migration we also found that September invoice KEV-26-0918 for KEV-DE-71104 (TPC-18 Stuttgart) omitted the off-peak register 1.8.2; it is replaced by KEV-RE-26-0918, period 2026-09-01 to 2026-09-30: 650,310 kWh, actual read. Facilities has filed both reissued invoices in your Box invoice folder 'Facilities — Utility invoices FY2026'. Apologies for the errors. Henrik Bauer, Key Account Management, Kessler Energie Vertrieb GmbH", 'contentType': 'text', 'isRead': False, 'importance': 'high', 'receivedDateTime': '2026-11-11T09:07:00Z'}
_T02_MDV_MAIL = {'id': 'AAMkT02msg0098', 'subject': 'Energy platform — validated month-end register reads posted (MDV-2026-11)', 'from_name': 'Lena Okafor', 'from_address': 'lena.okafor@talvik.example', 'to_name': 'Carbon Accounting Desk', 'to_address': 'alex.carter@contoso.com', 'bodyPreview': 'Hello desk, the annual register validation MDV-2026-11 is complete. We compared every FY2026 month-end register on the energy platform with the load-profile logs downloaded from the main meters during the November field campaign. Every automatic (AMR) month-end matched its log. Four month-ends that had been loaded by hand or by backfill did not, and the validated register values replaced them on the platform today: M-06-01 Elkhart (TPC-06) 2025-12-31 23:59 — manual read taken on 29 Dec at 16:40 and loaded as the 31 Dec month-end: 6,689,555 kWh replaced by 6,720,875 kWh; M-08-01 Macon (TPC-08) 2026-04-30 23:59 — manual read taken on 28 Apr at 15:30 and loaded as the 30 Apr month-end: 9,785,133 kWh replaced by 9,820,163 kWh; M-10-01 Salem (TPC-10) 2026-02-28 23:59 — manual read of 28 Feb keyed with two digits transposed: 9,857,661 kWh replaced by 9,875,661 kWh; M-17-01 Eindhoven (TPC-17) 2026-06-30 23:59 — the 9 July backfill loaded the 30 Jun 00:00 interval register instead of the 30 Jun 24:00 register: 15,521,883 kWh replaced by 15,529,763 kWh. The platform readings of these meters now carry the validated values; extracts and exports taken before today (including the 3 October export) still show the old ones. Lena Okafor, Energy platform administrator, Facilities Shared Services', 'contentType': 'text', 'isRead': False, 'importance': 'normal', 'receivedDateTime': '2026-11-11T15:20:00Z'}
# ======================================================================================


def _to_bool(v) -> bool:
    return str(v).strip().lower() == "true"


class OutlookSession:
    """Deterministic sandbox for the Outlook (Microsoft Graph) mock, ported from the FastAPI service."""

    def __init__(self, os_cfg, seed=None):
        # Seedless: world loaded verbatim from a frozen snapshot next to
        # this module; `seed` is accepted for client compat and ignored.
        if seed_mode():
            # Seed architecture: world rolled from a seed (re-armed).
            self.rng = random.Random(resolve_seed(seed))
            self.os = connect_os(os_cfg)
            self.time_machine = TimeMachine(rng=self.rng)

            # World data loaded verbatim from corpus/state.json (no cooking).
            from software.utils.world_data import load_state as _load_state
            _load_state(self, 'LightOutlook')
        else:
            # Seedless: world loaded verbatim from the frozen snapshot.
            restore_into(self, Path(__file__).resolve().parent / "world.pkl")
            self.os = connect_os(os_cfg)

    def get_session_dict(self):
        return {"messages": self.messages}

    # --- helpers -----------------------------------------------------------
    def _now(self) -> str:
        return self.os.now()

    def uuid(self) -> str:
        alphabet = "0123456789abcdef"
        return ''.join(self.rng.choices(alphabet, k=12))

    def _serialize_message(self, m):
        return {
            "id": m["id"],
            "subject": m["subject"],
            "bodyPreview": m["bodyPreview"],
            "importance": m["importance"],
            "isRead": m["isRead"],
            "receivedDateTime": m["receivedDateTime"],
            "from": {"emailAddress": {"name": m["from_name"], "address": m["from_address"]}},
            "toRecipients": [{"emailAddress": {"name": m["to_name"], "address": m["to_address"]}}],
            "body": {"contentType": m["contentType"], "content": m["bodyPreview"]},
        }

    def _serialize_event(self, e):
        return {
            "id": e["id"],
            "subject": e["subject"],
            "isAllDay": e.get("isAllDay", False),
            "isOnlineMeeting": e.get("isOnlineMeeting", False),
            "start": e["start"] if isinstance(e.get("start"), dict) else {"dateTime": e.get("start"), "timeZone": "UTC"},
            "end": e["end"] if isinstance(e.get("end"), dict) else {"dateTime": e.get("end"), "timeZone": "UTC"},
            "location": {"displayName": e.get("location", "")},
            "organizer": {"emailAddress": {"name": e.get("organizer_name", ""), "address": e.get("organizer_address", "")}},
            "attendees": [
                {"emailAddress": {"address": a}, "type": "required"} for a in e.get("attendees", [])
            ],
        }

    def _serialize_contact(self, c):
        return {
            "id": c["id"],
            "displayName": c["displayName"],
            "givenName": c.get("givenName", ""),
            "surname": c.get("surname", ""),
            "emailAddresses": c.get("emailAddresses") or [{"address": c.get("email", ""), "name": c["displayName"]}],
            "jobTitle": c.get("jobTitle", ""),
            "companyName": c.get("companyName", ""),
            "mobilePhone": c.get("mobilePhone", ""),
        }

    # ---- task world rule (T02): once the first FY2026 inventory item has been written, the Leipzig
    # supplier's key-account manager mails the desk about the two reissued invoices; once the last
    # (22nd) site item has been written, the energy platform administrator mails the desk that the
    # validated register reads are posted (each applied once per session, before every tool call and
    # before the sign-out dump).
    def _t02_apply(self):
        self._t02_apply_mdv()
        if self.__dict__.get("_t02_done") or not _t02_fired("t02_reissue"):
            return
        self.__dict__["_t02_done"] = True
        if not any(m["id"] == _T02_MAIL["id"] for m in self.messages):
            self.messages.append(dict(_T02_MAIL))

    def _t02_apply_mdv(self):
        if self.__dict__.get("_t02_mdv_done") or not _t02_fired("t02_mdv"):
            return
        self.__dict__["_t02_mdv_done"] = True
        if not any(m["id"] == _T02_MDV_MAIL["id"] for m in self.messages):
            self.messages.append(dict(_T02_MDV_MAIL))

    # --- Messages ----------------------------------------------------------
    def list_messages(self, is_read: bool | None = None) -> Dict[str, Any]:
        msgs = list(self.messages)
        if is_read is not None:
            msgs = [m for m in msgs if m["isRead"] == is_read]
        msgs = sorted(msgs, key=lambda m: m["receivedDateTime"], reverse=True)
        return {"status": "ok", "output": {"value": [self._serialize_message(m) for m in msgs]}}

    def get_message(self, message_id: str) -> Dict[str, Any]:
        for m in self.messages:
            if m["id"] == message_id:
                return {"status": "ok", "output": self._serialize_message(m)}
        return {"status": "failed", "output": f"Message {message_id} not found"}

    def send_mail(self, subject: str | None, content: str | None, to_recipients: List[str],
                  content_type: str = "HTML") -> Dict[str, Any]:
        if not to_recipients:
            return {"status": "failed", "output": "message.toRecipients is required"}
        to_address = to_recipients[0]
        msg = {
            "id": "AAMkAGsent" + self.uuid(),
            "subject": subject or "(no subject)",
            "from_name": _ME_NAME,
            "from_address": _ME_ADDRESS,
            "to_name": to_address,
            "to_address": to_address,
            "bodyPreview": (content or "")[:255],
            "contentType": (content_type or "HTML").lower(),
            "isRead": True,
            "importance": "normal",
            "receivedDateTime": self._now(),
        }
        self.messages.append(msg)
        return {"status": "ok", "output": {"status": "accepted", "id": msg["id"]}}

    # --- Events ------------------------------------------------------------
    def list_events(self) -> Dict[str, Any]:
        events = sorted(self.events, key=lambda e: str(e["start"].get("dateTime") if isinstance(e.get("start"), dict) else e.get("start")))
        return {"status": "ok", "output": {"value": [self._serialize_event(e) for e in events]}}

    # --- Contacts ----------------------------------------------------------
    def list_contacts(self) -> Dict[str, Any]:
        contacts = sorted(self.contacts, key=lambda c: c["displayName"])
        return {"status": "ok", "output": {"value": [self._serialize_contact(c) for c in contacts]}}



    def update_message(self, message_id: str, is_read: bool | None = None,
                       subject: str | None = None) -> Dict[str, Any]:
        m = next((x for x in self.messages if x["id"] == message_id), None)
        if not m:
            return {"status": "failed", "output": f"Message {message_id} not found"}
        if is_read is not None:
            m["isRead"] = bool(is_read)
        if subject is not None:
            m["subject"] = subject
        return {"status": "ok", "output": self._serialize_message(m)}

    def delete_message(self, message_id: str) -> Dict[str, Any]:
        idx = next((i for i, x in enumerate(self.messages) if x["id"] == message_id), None)
        if idx is None:
            return {"status": "failed", "output": f"Message {message_id} not found"}
        self.messages.pop(idx)
        return {"status": "ok", "output": {}}



def _t02_guarded(fn):
    @_t02_ft.wraps(fn)
    def inner(self, *a, **k):
        self._t02_apply()
        return fn(self, *a, **k)
    return inner


for _t02_n, _t02_f in list(vars(OutlookSession).items()):
    if callable(_t02_f) and _t02_n != "_t02_apply" and (not _t02_n.startswith("_") or _t02_n == "get_session_dict"):
        setattr(OutlookSession, _t02_n, _t02_guarded(_t02_f))
# ======================================================================================

if __name__ == "__main__":
    s = OutlookSession(seed=12)
    print(s.list_messages())
    print(s.list_contacts())
