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
        # Task-layer fix: stock events carry start/end as {dateTime, timeZone} objects and lack some
        # keys this serializer read directly (it raised). Same output shape.
        def _dt(v):
            return v.get("dateTime") if isinstance(v, dict) else v
        return {
            "id": e["id"],
            "subject": e.get("subject", ""),
            "isAllDay": e.get("isAllDay", False),
            "isOnlineMeeting": e.get("isOnlineMeeting", False),
            "start": {"dateTime": _dt(e.get("start")), "timeZone": "UTC"},
            "end": {"dateTime": _dt(e.get("end")), "timeZone": "UTC"},
            "location": {"displayName": e.get("location", "")},
            "organizer": {"emailAddress": {"name": e.get("organizer_name", ""), "address": e.get("organizer_address", "")}},
            "attendees": [
                {"emailAddress": {"address": a}, "type": "required"} for a in e.get("attendees", [])
            ],
        }

    def _serialize_contact(self, c):
        # Task-layer fix: stock contacts keep their address under emailAddresses[] and have no
        # givenName/surname/jobTitle keys (the serializer raised). Same output shape.
        email = c.get("email") or next((x.get("address") for x in c.get("emailAddresses") or [] if isinstance(x, dict)), "")
        parts = str(c.get("displayName", "")).split(" ", 1)
        return {
            "id": c["id"],
            "displayName": c.get("displayName", ""),
            "givenName": c.get("givenName", parts[0]),
            "surname": c.get("surname", parts[1] if len(parts) > 1 else ""),
            "emailAddresses": [{"address": email, "name": c.get("displayName", "")}],
            "jobTitle": c.get("jobTitle", ""),
            "companyName": c.get("companyName", ""),
            "mobilePhone": c.get("mobilePhone", (c.get("businessPhones") or [""])[0]),
        }

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

if __name__ == "__main__":
    s = OutlookSession(seed=12)
    print(s.list_messages())
    print(s.list_contacts())
