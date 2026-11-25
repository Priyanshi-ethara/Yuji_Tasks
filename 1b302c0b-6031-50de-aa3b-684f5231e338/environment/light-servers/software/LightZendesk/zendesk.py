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


def _to_int(v, default=None):
    if v is None or str(v).strip() == "":
        return default
    try:
        return int(v)
    except (TypeError, ValueError):
        return default


def _opt_csv_list(v, sep=";"):
    if not v:
        return []
    return [x for x in str(v).split(sep) if x]


VALID_STATUS = {"new", "open", "pending", "hold", "solved", "closed"}
VALID_PRIORITY = {"low", "normal", "high", "urgent"}


class ZendeskSession:
    """Deterministic sandbox for the Zendesk Support API mock, ported from the FastAPI service."""

    def __init__(self, os_cfg, seed=None):
        # Seedless: world loaded verbatim from a frozen snapshot next to
        # this module; `seed` is accepted for client compat and ignored.
        if seed_mode():
            # Seed architecture: world rolled from a seed (re-armed).
            self.rng = random.Random(resolve_seed(seed))
            self.os = connect_os(os_cfg)
            self.time_machine = TimeMachine(rng=self.rng)

            from software.utils.world_data import load_state as _load_state
            _load_state(self, "LightZendesk")
        else:
            # Seedless: world loaded verbatim from the frozen snapshot.
            restore_into(self, Path(__file__).resolve().parent / "world.pkl")
            self.os = connect_os(os_cfg)

    def get_session_dict(self):
        return {"tickets": self.tickets, "comments": self.comments}

    # --- helpers -----------------------------------------------------------
    def _now(self) -> str:
        return self.os.now()

    def _next_id(self, store):
        return (max((x["id"] for x in store), default=None) + 1) if store else 1

    def _find(self, store, obj_id):
        obj_id = _to_int(obj_id)
        return next((x for x in store if x["id"] == obj_id), None)

    # --- Tickets -----------------------------------------------------------
    def list_tickets(self, status: str | None = None, priority: str | None = None,
                     assignee_id: int | None = None) -> Dict[str, Any]:
        results = list(self.tickets)
        if status:
            results = [t for t in results if t["status"] == status]
        if priority:
            results = [t for t in results if t["priority"] == priority]
        if assignee_id is not None:
            results = [t for t in results if t["assignee_id"] == _to_int(assignee_id)]
        results.sort(key=lambda t: t["id"])
        return {"status": "ok", "output": {"tickets": results, "count": len(results)}}

    def get_ticket(self, ticket_id: int) -> Dict[str, Any]:
        t = self._find(self.tickets, ticket_id)
        if not t:
            return {"status": "failed", "output": f"Ticket {ticket_id} not found"}
        return {"status": "ok", "output": {"ticket": t}}

    def create_ticket(self, subject: str, description: str | None = None, priority: str = "normal",
                      ticket_type: str = "question", requester_id: int | None = None,
                      assignee_id: int | None = None, organization_id: int | None = None,
                      tags: List[str] | None = None, comment_body: str | None = None) -> Dict[str, Any]:
        if not subject:
            return {"status": "failed", "output": "subject is required"}
        if priority and priority not in VALID_PRIORITY:
            return {"status": "failed", "output": f"Invalid priority: {priority}"}
        now = self._now()
        ticket_id = self._next_id(self.tickets)
        ticket = {
            "id": ticket_id,
            "subject": subject,
            "description": description or (comment_body or ""),
            "status": "new",
            "priority": priority or "normal",
            "type": ticket_type or "question",
            "requester_id": _to_int(requester_id),
            "assignee_id": _to_int(assignee_id),
            "organization_id": _to_int(organization_id),
            "tags": tags or [],
            "created_at": now,
            "updated_at": now,
        }
        self.tickets.append(ticket)
        body = comment_body or description
        if body:
            self.comments.append({
                "id": self._next_id(self.comments),
                "ticket_id": ticket_id,
                "author_id": _to_int(requester_id),
                "body": body,
                "public": True,
                "created_at": now,
            })
        return {"status": "ok", "output": {"ticket": ticket}}

    def update_ticket(self, ticket_id: int, status: str | None = None, priority: str | None = None,
                      assignee_id: int | None = None, ticket_type: str | None = None,
                      tags: List[str] | None = None, comment_body: str | None = None,
                      comment_public: bool = True, comment_author_id: int | None = None) -> Dict[str, Any]:
        t = self._find(self.tickets, ticket_id)
        if not t:
            return {"status": "failed", "output": f"Ticket {ticket_id} not found"}
        if status is not None:
            if status not in VALID_STATUS:
                return {"status": "failed", "output": f"Invalid status: {status}"}
            t["status"] = status
        if priority is not None:
            if priority not in VALID_PRIORITY:
                return {"status": "failed", "output": f"Invalid priority: {priority}"}
            t["priority"] = priority
        if assignee_id is not None:
            t["assignee_id"] = _to_int(assignee_id)
        if ticket_type is not None:
            t["type"] = ticket_type
        if tags is not None:
            t["tags"] = tags
        if comment_body:
            self.comments.append({
                "id": self._next_id(self.comments),
                "ticket_id": t["id"],
                "author_id": _to_int(comment_author_id) if comment_author_id is not None else t["assignee_id"],
                "body": comment_body,
                "public": bool(comment_public),
                "created_at": self._now(),
            })
        t["updated_at"] = self._now()
        return {"status": "ok", "output": {"ticket": t}}

    # --- Comments ----------------------------------------------------------
    def list_comments(self, ticket_id: int) -> Dict[str, Any]:
        if not self._find(self.tickets, ticket_id):
            return {"status": "failed", "output": f"Ticket {ticket_id} not found"}
        tid = _to_int(ticket_id)
        comments = [c for c in self.comments if c["ticket_id"] == tid]
        comments.sort(key=lambda c: c["created_at"])
        return {"status": "ok", "output": {"comments": comments, "count": len(comments)}}

    def create_comment(self, ticket_id: int, body: str, author_id: int | None = None,
                       public: bool = True) -> Dict[str, Any]:
        t = self._find(self.tickets, ticket_id)
        if not t:
            return {"status": "failed", "output": f"Ticket {ticket_id} not found"}
        if not body:
            return {"status": "failed", "output": "comment body is required"}
        comment = {
            "id": self._next_id(self.comments),
            "ticket_id": t["id"],
            "author_id": _to_int(author_id) if author_id is not None else t["assignee_id"],
            "body": body,
            "public": bool(public),
            "created_at": self._now(),
        }
        self.comments.append(comment)
        t["updated_at"] = self._now()
        return {"status": "ok", "output": {"comment": comment}}

    # --- Users / Organizations ---------------------------------------------
    def list_users(self, role: str | None = None) -> Dict[str, Any]:
        results = list(self.users)
        if role:
            results = [u for u in results if u["role"] == role]
        return {"status": "ok", "output": {"users": results, "count": len(results)}}

    def get_user(self, user_id: int) -> Dict[str, Any]:
        u = self._find(self.users, user_id)
        if not u:
            return {"status": "failed", "output": f"User {user_id} not found"}
        return {"status": "ok", "output": {"user": u}}

    def list_organizations(self) -> Dict[str, Any]:
        return {"status": "ok", "output": {"organizations": list(self.organizations), "count": len(self.organizations)}}


    def delete_ticket(self, ticket_id: int) -> Dict[str, Any]:
        t = self._find(self.tickets, ticket_id)
        if not t:
            return {"status": "failed", "output": f"Ticket {ticket_id} not found"}
        self.tickets.remove(t)
        tid = _to_int(ticket_id)
        self.comments = [c for c in self.comments if c["ticket_id"] != tid]
        return {"status": "ok", "output": {"ticket_id": ticket_id, "deleted": True}}


# =====================================================================================
# Task world rule - Lumen Telecom service desk ("Lumen Desk" business rules)
# The hosted instance applies three documented rules (DESKADM "Lumen Desk - instance configuration")
# to every save of a ticket, after the save is committed:
#   * organisation (TOOL-503): the ticket is filed under its requester's organisation (the organisation
#     on the requester's user record); every rule below reads that organisation;
#   * field storage: a tag is held to 24 characters; characters after the 24th are dropped;
#   * T-11 self-service standardisation: a ticket of type question whose organisation is tagged
#     seg_res and whose priority is high or urgent is held at priority normal.
# The acknowledgement of an update returns the ticket as submitted (before the rules), as the
# configuration page documents; get_ticket / list_tickets and the session dump show the ticket as held.
# Deterministic: no clock, no randomness, no extra state, no new tools, record types or fields.
# =====================================================================================
import copy as _lumen_copy

_LUMEN_TAG_CHARS = 24


def _lumen_org(self, org_id):
    for org in getattr(self, "organizations", None) or []:
        if isinstance(org, dict) and org.get("id") == _to_int(org_id):
            return org
    return None


def _lumen_requester_org(self, requester_id):
    for user in getattr(self, "users", None) or []:
        if isinstance(user, dict) and user.get("id") == _to_int(requester_id):
            return user.get("organization_id")
    return None


def _lumen_apply_rules(self, ticket):
    if not isinstance(ticket, dict):
        return
    filed = _lumen_requester_org(self, ticket.get("requester_id"))
    if filed is not None:
        ticket["organization_id"] = filed
    tags = ticket.get("tags")
    if isinstance(tags, list):
        ticket["tags"] = [tg[:_LUMEN_TAG_CHARS] if isinstance(tg, str) else tg for tg in tags]
    if str(ticket.get("type") or "").strip().lower() == "question" and \
            str(ticket.get("priority") or "").strip().lower() in ("high", "urgent"):
        org = _lumen_org(self, ticket.get("organization_id"))
        if org is not None and "seg_res" in (org.get("tags") or []):
            ticket["priority"] = "normal"


_lumen_stock_update_ticket = ZendeskSession.update_ticket
_lumen_stock_create_ticket = ZendeskSession.create_ticket
_lumen_stock_create_comment = ZendeskSession.create_comment


def _lumen_update_ticket(self, ticket_id, *args, **kwargs):
    result = _lumen_stock_update_ticket(self, ticket_id, *args, **kwargs)
    if isinstance(result, dict) and result.get("status") == "ok":
        held = self._find(self.tickets, ticket_id)
        submitted = _lumen_copy.deepcopy(held)
        _lumen_apply_rules(self, held)
        result = {"status": "ok", "output": {"ticket": submitted}}
    return result


def _lumen_create_ticket(self, *args, **kwargs):
    result = _lumen_stock_create_ticket(self, *args, **kwargs)
    if isinstance(result, dict) and result.get("status") == "ok":
        held = result["output"]["ticket"]
        submitted = _lumen_copy.deepcopy(held)
        _lumen_apply_rules(self, held)
        result = {"status": "ok", "output": {"ticket": submitted}}
    return result


def _lumen_create_comment(self, ticket_id, *args, **kwargs):
    result = _lumen_stock_create_comment(self, ticket_id, *args, **kwargs)
    if isinstance(result, dict) and result.get("status") == "ok":
        _lumen_apply_rules(self, self._find(self.tickets, ticket_id))
    return result


ZendeskSession.update_ticket = _lumen_update_ticket
ZendeskSession.create_ticket = _lumen_create_ticket
ZendeskSession.create_comment = _lumen_create_comment


if __name__ == "__main__":
    s = ZendeskSession(seed=12)
    print(s.list_tickets())
    print(s.list_organizations())
