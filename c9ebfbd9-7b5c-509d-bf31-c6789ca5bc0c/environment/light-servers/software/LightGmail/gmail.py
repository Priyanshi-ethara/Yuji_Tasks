import random
import json
from typing import Dict, List, Any
from pathlib import Path
import sys
from datetime import datetime

WORK_DIR = Path('.').__str__()
if WORK_DIR not in sys.path:
    sys.path.append(WORK_DIR)

from software.utils import corpus_registry
from software.utils.core import OSConnector, DummyOSConnector, connect_os
from software.utils.world_snapshot import restore_into, seed_mode, resolve_seed
from software.utils.time import TimeMachine


# ---------------------------------------------------------------------------------------------
# Task world rule (R-2026-45 release round). The release board, the carrier drop and the QA
# mailbox are separate server processes; they signal through flag files in ATLAS_EVENT_DIR.
import os as _ev_os, pathlib as _ev_pathlib
_EV_DIR = _ev_pathlib.Path(_ev_os.environ.get("ATLAS_EVENT_DIR", "/tmp/atlas_events"))
_EV_FLAG = "tk9-5521-seg2-recovered"


def _ev_fire(name):
    _EV_DIR.mkdir(parents=True, exist_ok=True)
    (_EV_DIR / name).touch()


def _ev_fired(name):
    return (_EV_DIR / name).exists()
# ---------------------------------------------------------------------------------------------
_EV_MAIL = json.loads('{"id": "msg-pa-4599", "thread_id": "thr-pa-41207", "from_addr": "dagny.rask@polararc-logistics.example", "to_addr": "qa.release@tarnwick-bio.example", "cc_addr": "aleksander.hune@tarnwick-bio.example", "subject": "HX4-41207 / TK9-5521 - segment 2 recovered and uploaded to the drop", "snippet": "Segment 2 of TK9-5521 (05 Nov 02:00-07:50 UTC) has been recovered from the logger flash and is now in the drop folder.", "body": "Hello QA team,\\n\\nSegment 2 of logger TK9-5521 on HX4-41207 (05 Nov 2026 02:00-07:50 UTC) has been recovered from the logger flash and uploaded to the drop folder:\\n/Polar Arc - Tarnwick drop/R-2026-45/TK9-5521/TK9-5521_HX4-41207_seg2.csv\\n\\nThe metadata file in the same folder now lists the segment as delivered. Unit and interval are as for the other segments (see the metadata). Our recovery log reference is PA-REC-1187.\\n\\nKind regards,\\nDagny Rask\\nOperations Coordinator, Polar Arc Logistics", "date": "2026-11-10T11:42:00Z", "internal_date": 1794310920000, "size_estimate": 2100, "labels": ["INBOX", "Label_Carriers"], "is_unread": true, "is_starred": false}')
_EV_FLAG2 = "tk9-5521-cert-reissued"
_EV_MAIL2 = json.loads('{"id": "msg-twk-4512", "thread_id": "thr-twk-4512", "from_addr": "priya.venkataraman@tarnwick-bio.example", "to_addr": "qa.release@tarnwick-bio.example", "cc_addr": "", "subject": "TK9-5521 certificate reissued - TML-CC-2026-1196 issue 2", "snippet": "Polar Arc\'s recovery of segment 2 (PA-REC-1187) came with the logger\'s diagnostic trace for that period, which issue 1 of the certificate could not see.", "body": "Hello QA desk,\\n\\nPolar Arc\'s recovery of segment 2 (PA-REC-1187) came with the logger\'s diagnostic trace for that period, which issue 1 of the certificate could not see. The trace dates probe open-circuit events on 5 Nov from 03:20 to 03:50 UTC, and the repeat flex test this morning reproduced the intermittent contact.\\n\\nI have reissued the certificate in the Box folder \'Logger calibration certificates 2026\' as TML-CC-2026-1196 issue 2, same file, with the sensor-fault window 2026-11-05T03:20Z to 2026-11-05T03:50Z. Issue 1 of 8 November is superseded.\\n\\nPriya\\nPriya Venkataraman, Metrology & Calibration Lead", "date": "2026-11-10T13:10:00Z", "internal_date": 1794316200000, "size_estimate": 2240, "labels": ["INBOX", "Label_QA"], "is_unread": true, "is_starred": false}')

CORPUS_PATH = Path(__file__).resolve().parent / "corpus"


def _to_bool(v) -> bool:
    return str(v).strip().lower() == "true"


def _to_int(v) -> int:
    return int(str(v).strip())


class GmailSession:
    """Deterministic sandbox for the Gmail mock, ported from the FastAPI service.

    State is loaded from the corpus at init; subsequent calls read and mutate the
    in-memory tables so repeated calls within a session stay consistent.
    """

    def __init__(self, os_cfg, seed=None, fixture=None):
        # Seedless: world loaded verbatim from a frozen snapshot next to
        # this module; `seed` is accepted for client compat and ignored.
        if seed_mode():
            # Seed architecture: world rolled from a seed (re-armed).
            self.rng = random.Random(resolve_seed(seed))
            self.os = connect_os(os_cfg)
            self.time_machine = TimeMachine(rng=self.rng)

            info = corpus_registry.load(CORPUS_PATH / "gmail.yaml")

            self.labels: List[Dict[str, Any]] = [
                {
                    **l,
                    "messagesTotal": _to_int(l["messages_total"]),
                    "messagesUnread": _to_int(l["messages_unread"]),
                    "threadsTotal": _to_int(l["threads_total"]),
                    "threadsUnread": _to_int(l["threads_unread"]),
                }
                for l in info.get("labels", [])
            ]
            self.messages: List[Dict[str, Any]] = [
                {
                    **m,
                    "body": m["body"].replace("\\n", "\n"),
                    "internal_date": _to_int(m["internal_date"]),
                    "size_estimate": _to_int(m["size_estimate"]),
                    "labels": (list(m["labels"]) if isinstance(m.get("labels"), list)
                               else [x.strip() for x in str(m.get("labels") or "").split(",") if x.strip()]),
                    "is_unread": _to_bool(m["is_unread"]),
                    "is_starred": _to_bool(m["is_starred"]),
                }
                for m in info.get("messages", [])
            ]
            self.drafts: List[Dict[str, Any]] = [
                {**d, "body": d["body"].replace("\\n", "\n")} for d in info.get("drafts", [])
            ]
            self.profile: Dict[str, Any] = dict(info.get("profile", {}))

            from software.utils.fixtures import apply as _apply_fixtures
            _apply_fixtures(self, "LightGmail", fixture)
            from software.utils.world_data import hydrate as _hydrate_world_data
            _hydrate_world_data(self, "LightGmail")
        else:
            # Seedless: world loaded verbatim from the frozen snapshot.
            restore_into(self, Path(__file__).resolve().parent / "world.pkl")
            self.os = connect_os(os_cfg)

    def get_session_dict(self):
        self._task_events()
        return {"messages": self.messages, "drafts": self.drafts, "labels": self.labels}


    def _task_events(self):
        """Task world rule: when the carrier has recovered TK9-5521 segment 2, its notice reaches the QA
        release mailbox; when Metrology has reissued the TK9-5521 certificate, Metrology's note follows
        (fixed ids and timestamps). Each is applied once per session."""
        done = getattr(self, "_ev_done", None)
        if done is None:
            done = self._ev_done = set()
        for flag, mail in ((_EV_FLAG, _EV_MAIL), (_EV_FLAG2, _EV_MAIL2)):
            if flag in done or not _ev_fired(flag):
                continue
            done.add(flag)
            if not any(m.get("id") == mail["id"] for m in self.messages):
                self.messages.append(json.loads(json.dumps(mail)))

    # --- helpers -----------------------------------------------------------
    def _now(self) -> str:
        return self.os.now()

    def _now_ms(self) -> int:
        return int(datetime.utcnow().timestamp() * 1000)

    def uuid(self, k: int = 16) -> str:
        alphabet = "0123456789abcdef"
        return ''.join(self.rng.choices(alphabet, k=k))

    def _new_id(self, prefix="msg") -> str:
        return f"{prefix}-{self.uuid(10)}"

    def _serialize_message(self, m, full=True) -> Dict[str, Any]:
        out = {
            "id": m["id"],
            "threadId": m["thread_id"],
            "labelIds": m["labels"],
            "snippet": m["snippet"],
            "internalDate": str(m["internal_date"]),
            "sizeEstimate": m["size_estimate"],
        }
        if full:
            out["payload"] = {
                "headers": [
                    {"name": "From", "value": m["from_addr"]},
                    {"name": "To", "value": m["to_addr"]},
                    {"name": "Cc", "value": m["cc_addr"]},
                    {"name": "Subject", "value": m["subject"]},
                    {"name": "Date", "value": m["date"]},
                ],
                "body": {"data": m["body"], "size": len(m["body"])},
                "mimeType": "text/plain",
            }
        return out

    _QUERY_KV = None

    def _parse_query(self, query):
        import re
        if GmailSession._QUERY_KV is None:
            GmailSession._QUERY_KV = re.compile(r"(\w+):(\"[^\"]*\"|\S+)")
        filters = {}
        free_text = query
        for m in GmailSession._QUERY_KV.finditer(query):
            key = m.group(1).lower()
            val = m.group(2).strip('"')
            filters.setdefault(key, []).append(val)
            free_text = free_text.replace(m.group(0), "")
        free_text = free_text.strip()
        return filters, free_text

    # --- Profile -----------------------------------------------------------
    def get_profile(self) -> Dict[str, Any]:
        self._task_events()
        return {"status": "ok", "output": self.profile}

    # --- Labels ------------------------------------------------------------
    def list_labels(self) -> Dict[str, Any]:
        self._task_events()
        return {"status": "ok", "output": {"labels": [
            {"id": l["id"], "name": l["name"], "type": l["type"]} for l in self.labels
        ]}}

    def get_label(self, label_id: str) -> Dict[str, Any]:
        self._task_events()
        for l in self.labels:
            if l["id"] == label_id:
                return {"status": "ok", "output": l}
        return {"status": "failed", "output": f"Label {label_id} not found"}

    def create_label(self, name: str) -> Dict[str, Any]:
        self._task_events()
        if any(l["name"] == name for l in self.labels):
            return {"status": "failed", "output": f"Label {name} already exists"}
        label = {
            "id": f"Label_{self.uuid(8)}",
            "name": name,
            "type": "user",
            "messages_total": 0, "messagesTotal": 0,
            "messages_unread": 0, "messagesUnread": 0,
            "threads_total": 0, "threadsTotal": 0,
            "threads_unread": 0, "threadsUnread": 0,
        }
        self.labels.append(label)
        return {"status": "ok", "output": label}

    # --- Messages / threads ------------------------------------------------
    def list_messages(self, query: str = "", max_results: int = 25,
                      label_ids: List[str] | None = None) -> Dict[str, Any]:
        self._task_events()
        label_ids = label_ids or []
        filters, free_text = self._parse_query(query or "")
        results = list(self.messages)
        if label_ids:
            results = [m for m in results if all(l in m["labels"] for l in label_ids)]
        if "from" in filters:
            results = [m for m in results if any(f.lower() in m["from_addr"].lower() for f in filters["from"])]
        if "to" in filters:
            results = [m for m in results if any(f.lower() in m["to_addr"].lower() for f in filters["to"])]
        if "subject" in filters:
            results = [m for m in results if any(f.lower() in m["subject"].lower() for f in filters["subject"])]
        if "label" in filters:
            for lname in filters["label"]:
                ids = {l["id"] for l in self.labels if l["name"].lower() == lname.lower()}
                results = [m for m in results if ids & set(m["labels"])]
        if "is" in filters:
            if "unread" in [v.lower() for v in filters["is"]]:
                results = [m for m in results if m["is_unread"]]
            if "starred" in [v.lower() for v in filters["is"]]:
                results = [m for m in results if m["is_starred"]]
        if free_text:
            ft = free_text.lower()
            results = [m for m in results
                       if ft in m["subject"].lower() or ft in m["body"].lower() or ft in m["snippet"].lower()]
        results.sort(key=lambda m: m["internal_date"], reverse=True)
        page = results[:max_results]
        return {"status": "ok", "output": {
            "messages": [{"id": m["id"], "threadId": m["thread_id"]} for m in page],
            "resultSizeEstimate": len(results),
        }}

    def get_message(self, message_id: str, fmt: str = "full") -> Dict[str, Any]:
        self._task_events()
        for m in self.messages:
            if m["id"] == message_id:
                return {"status": "ok", "output": self._serialize_message(m, full=(fmt == "full"))}
        return {"status": "failed", "output": f"Message {message_id} not found"}

    def send_message(self, to_addr: str, subject: str, body: str, cc: str | None = None,
                    thread_id: str | None = None, from_addr: str | None = None) -> Dict[str, Any]:
        self._task_events()
        msg_id = self._new_id("msg")
        thread_id = thread_id or f"thr-{self.uuid(8)}"
        now = self._now_ms()
        msg = {
            "id": msg_id,
            "thread_id": thread_id,
            "from_addr": from_addr or self.profile["emailAddress"],
            "to_addr": to_addr,
            "cc_addr": cc or "",
            "subject": subject,
            "snippet": (body[:140] + "...") if len(body) > 140 else body,
            "body": body,
            "date": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "internal_date": now,
            "size_estimate": len(body) + len(subject),
            "labels": ["SENT"],
            "is_unread": False,
            "is_starred": False,
        }
        self.messages.append(msg)
        return {"status": "ok", "output": self._serialize_message(msg)}

    def modify_message(self, message_id: str, add_labels: List[str] | None = None,
                      remove_labels: List[str] | None = None) -> Dict[str, Any]:
        self._task_events()
        for i, m in enumerate(self.messages):
            if m["id"] == message_id:
                labels = set(m["labels"])
                if add_labels:
                    labels.update(add_labels)
                if remove_labels:
                    labels.difference_update(remove_labels)
                self.messages[i]["labels"] = sorted(labels)
                if "UNREAD" in (remove_labels or []):
                    self.messages[i]["is_unread"] = False
                if "STARRED" in (add_labels or []):
                    self.messages[i]["is_starred"] = True
                if "STARRED" in (remove_labels or []):
                    self.messages[i]["is_starred"] = False
                return {"status": "ok", "output": self._serialize_message(self.messages[i])}
        return {"status": "failed", "output": f"Message {message_id} not found"}

    def trash_message(self, message_id: str) -> Dict[str, Any]:
        self._task_events()
        return self.modify_message(message_id, add_labels=["TRASH"], remove_labels=["INBOX"])

    def delete_message(self, message_id: str) -> Dict[str, Any]:
        self._task_events()
        for i, m in enumerate(self.messages):
            if m["id"] == message_id:
                self.messages.pop(i)
                return {"status": "ok", "output": {"deleted": True, "id": message_id}}
        return {"status": "failed", "output": f"Message {message_id} not found"}

    def list_threads(self, query: str = "") -> Dict[str, Any]:
        self._task_events()
        msg_list = self.list_messages(query=query)["output"]
        seen = []
        for entry in msg_list["messages"]:
            if entry["threadId"] not in [s["id"] for s in seen]:
                seen.append({"id": entry["threadId"]})
        return {"status": "ok", "output": {"threads": seen, "resultSizeEstimate": len(seen)}}

    def get_thread(self, thread_id: str) -> Dict[str, Any]:
        self._task_events()
        msgs = [m for m in self.messages if m["thread_id"] == thread_id]
        if not msgs:
            return {"status": "failed", "output": f"Thread {thread_id} not found"}
        msgs.sort(key=lambda m: m["internal_date"])
        return {"status": "ok", "output": {
            "id": thread_id,
            "historyId": self.profile["historyId"],
            "messages": [self._serialize_message(m) for m in msgs],
        }}

    # --- Drafts ------------------------------------------------------------
    def list_drafts(self) -> Dict[str, Any]:
        self._task_events()
        return {"status": "ok", "output": {"drafts": [
            {"id": d["id"], "message": {"id": "", "threadId": d["thread_id"]}} for d in self.drafts
        ]}}

    def get_draft(self, draft_id: str) -> Dict[str, Any]:
        self._task_events()
        for d in self.drafts:
            if d["id"] == draft_id:
                return {"status": "ok", "output": d}
        return {"status": "failed", "output": f"Draft {draft_id} not found"}

    def create_draft(self, to_addr: str, subject: str, body: str,
                    cc: str | None = None, thread_id: str | None = None) -> Dict[str, Any]:
        self._task_events()
        draft = {
            "id": self._new_id("draft"),
            "thread_id": thread_id or "",
            "to_addr": to_addr,
            "cc_addr": cc or "",
            "subject": subject,
            "body": body,
            "updated_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        self.drafts.append(draft)
        return {"status": "ok", "output": draft}

    def send_draft(self, draft_id: str) -> Dict[str, Any]:
        self._task_events()
        draft = next((d for d in self.drafts if d["id"] == draft_id), None)
        if not draft:
            return {"status": "failed", "output": f"Draft {draft_id} not found"}
        sent = self.send_message(
            to_addr=draft["to_addr"],
            subject=draft["subject"],
            body=draft["body"],
            cc=draft["cc_addr"],
            thread_id=draft["thread_id"] or None,
        )
        self.drafts.remove(draft)
        return sent


if __name__ == "__main__":
    s = GmailSession(seed=12)
    print(s.get_profile())
    print(s.list_labels())
    print(s.list_messages())
