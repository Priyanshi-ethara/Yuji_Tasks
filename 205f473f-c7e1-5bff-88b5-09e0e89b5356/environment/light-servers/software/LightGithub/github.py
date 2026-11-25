# --- task world rule (U04 crash-owner-routing): task-layer fix of a stock crash --------------------
# The stock corpus carries one pull request without a "repo" key and one repository in the dump shape
# (owner as an object, stargazers_count). list_pulls / get_pull / merge_pull and list_repos() raised
# KeyError on them for every caller. The reads below tolerate both shapes; no tool, record type, field
# or output shape changes.
# -----------------------------------------------------------------------------------------------
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


def _to_int(v) -> int:
    return int(v)


# ============================================================================ task world rule (U04, live)
# pellam/fleetd on Monday 16 Nov 2026: pull request #3490 (the /internal/notify/ line of .github/CODEOWNERS
# moves to Driver Comms' handle) is merged at 08:40 UTC. It is in the repository's records once the triage
# register has 21 distinct rows written (flag pellam_u04_notify, raised by the Airtable app). Applied
# idempotently at the start of every tool method and in get_session_dict; no tool, record type or field
# is added.
import os as _u04_os
import pathlib as _u04_pathlib


def _u04_fired(name):
    ev = _u04_pathlib.Path(_u04_os.environ.get("ATLAS_EVENT_DIR", "/tmp/atlas_events"))
    return (ev / name).exists()


_U04_BODY = (
    "Driver Comms took over driver-facing notification delivery on 2 Nov (hand-over list from Messaging, MSG-588). "
    "This moves the notifications line of CODEOWNERS to their handle, in place:\n\n"
    "```diff\n"
    " # Notifications\n"
    "-/internal/notify/                   @pellam/messaging\n"
    "+/internal/notify/                   @pellam/driver-comms\n"
    "```\n\n"
    "No other line changes. Reviewed by Platform Foundations (Ruth) as for every CODEOWNERS change."
)
_U04_ISSUE = {
    "id": 7703490, "number": 3490, "repo": "fleetd", "title": "CODEOWNERS: internal/notify/ to Driver Comms",
    "body": _U04_BODY, "state": "closed", "user": "petra-lindqvist", "assignee": "", "labels": ["codeowners"],
    "milestone": None, "created_at": "2026-11-16T08:05:00Z", "updated_at": "2026-11-16T08:40:00Z",
    "closed_at": "2026-11-16T08:40:00Z", "is_pull_request": True,
}
_U04_PULL = {
    "number": 3490, "id": "pr_fleetd_3490", "repo": "fleetd", "title": "CODEOWNERS: internal/notify/ to Driver Comms",
    "state": "closed", "user": {"login": "petra-lindqvist"}, "head": {"ref": "petra/3490", "sha": "c41e07d2b9a5"},
    "base": {"ref": "main"}, "body": _U04_BODY, "created_at": "2026-11-16T08:05:00Z",
    "updated_at": "2026-11-16T08:40:00Z", "merged": True, "mergeable": False, "draft": False,
}
_U04_COMMENTS = [
    {"id": 8800004, "issue_number": 3490, "repo": "fleetd", "user": "ruth-calloway",
     "body": "Approved for Platform. Merging; the line takes effect on main now.", "created_at": "2026-11-16T08:38:00Z"},
    {"id": 8800005, "issue_number": 3490, "repo": "fleetd", "user": "tamsin-okafor",
     "body": "Thanks. Driver Comms picks up anything under internal/notify from here.", "created_at": "2026-11-16T08:42:00Z"},
]


def _u04_apply(session):
    if not _u04_fired("pellam_u04_notify"):
        return
    issues = getattr(session, "issues", None)
    if issues is not None and not any(i.get("repo") == "fleetd" and i.get("number") == 3490 for i in issues):
        issues.append(dict(_U04_ISSUE, labels=list(_U04_ISSUE["labels"])))
    pulls = getattr(session, "pulls", None)
    if pulls is not None and not any(p.get("repo") == "fleetd" and p.get("number") == 3490 for p in pulls):
        pulls.append(dict(_U04_PULL))
    comments = getattr(session, "comments", None)
    if comments is not None:
        for c in _U04_COMMENTS:
            if not any(x.get("id") == c["id"] for x in comments):
                comments.append(dict(c))
# ============================================================================ end task world rule


class GithubSession:
    """Deterministic sandbox for the GitHub REST API mock, ported from the FastAPI service.

    State is loaded from the corpus at init; subsequent calls read and mutate the
    in-memory tables so repeated calls within a session stay consistent.
    """

    def __init__(self, os_cfg, seed=None):
        # Seedless: world loaded verbatim from a frozen snapshot next to
        # this module; `seed` is accepted for client compat and ignored.
        if seed_mode():
            # Seed architecture: world rolled from a seed (re-armed).
            self.rng = random.Random(resolve_seed(seed))
            self.os = connect_os(os_cfg)
            self.time_machine = TimeMachine(rng=self.rng)

            # World data loaded verbatim from corpus/state.json (no cooking):
            # repos/issues/pulls/comments/user stored in final shape.
            from software.utils.world_data import load_state as _load_state
            _load_state(self, 'LightGithub')
        else:
            # Seedless: world loaded verbatim from the frozen snapshot.
            restore_into(self, Path(__file__).resolve().parent / "world.pkl")
            self.os = connect_os(os_cfg)

    def get_session_dict(self):
        _u04_apply(self)
        return {"issues": self.issues, "comments": self.comments}

    # --- helpers -----------------------------------------------------------
    def _now(self) -> str:
        return self.os.now()

    def uuid(self) -> str:
        _u04_apply(self)
        alphabet = "0123456789"
        return ''.join(self.rng.choices(alphabet, k=16))

    def _serialize_repo(self, r):
        return {
            "id": r["id"],
            "name": r["name"],
            "full_name": r["full_name"],
            "owner": {"login": r["owner"]["login"] if isinstance(r["owner"], dict) else r["owner"]},
            "private": r["private"],
            "description": r["description"],
            "default_branch": r["default_branch"],
            "language": r["language"],
            "stargazers_count": r.get("stars", r.get("stargazers_count", 0)),
            "forks_count": r.get("forks", r.get("forks_count", 0)),
            "open_issues_count": r.get("open_issues", r.get("open_issues_count", 0)),
            "created_at": r.get("created_at"),
            "updated_at": r.get("updated_at"),
        }

    def _serialize_issue(self, i):
        return {
            "id": i["id"],
            "number": i["number"],
            "title": i["title"],
            "body": i["body"],
            "state": i["state"],
            "user": {"login": i["user"]},
            "assignee": {"login": i["assignee"]} if i["assignee"] else None,
            "labels": [{"name": l} for l in i["labels"]],
            "milestone": {"title": i["milestone"]} if i["milestone"] else None,
            "created_at": i["created_at"],
            "updated_at": i["updated_at"],
            "closed_at": i["closed_at"],
            "pull_request": {"url": f"/repos/{i['repo']}/pulls/{i['number']}"} if i["is_pull_request"] else None,
        }

    # --- API methods -------------------------------------------------------
    def get_user(self) -> Dict[str, Any]:
        _u04_apply(self)
        return {"status": "ok", "output": self.user}

    def list_repos(self, owner: str | None = None) -> Dict[str, Any]:
        _u04_apply(self)
        results = list(self.repos)
        if owner:
            results = [r for r in results if (r["owner"]["login"] if isinstance(r["owner"], dict) else r["owner"]) == owner]
        return {"status": "ok", "output": [self._serialize_repo(r) for r in results]}

    def get_repo(self, owner: str, repo: str) -> Dict[str, Any]:
        _u04_apply(self)
        for r in self.repos:
            if r["owner"] == owner and r["name"] == repo:
                return {"status": "ok", "output": self._serialize_repo(r)}
        return {"status": "failed", "output": f"Repo {owner}/{repo} not found"}

    def list_issues(self, owner: str, repo: str, state: str = "open", labels: str | None = None,
                    assignee: str | None = None, per_page: int = 30) -> Dict[str, Any]:
        _u04_apply(self)
        if not any(r["owner"] == owner and r["name"] == repo for r in self.repos):
            return {"status": "failed", "output": f"Repo {owner}/{repo} not found"}
        results = [i for i in self.issues if i["repo"] == repo]
        if state and state != "all":
            results = [i for i in results if i["state"] == state]
        if labels:
            wanted = {l.strip().lower() for l in labels.split(",")}
            results = [i for i in results if {l.lower() for l in i["labels"]} & wanted]
        if assignee:
            results = [i for i in results if i["assignee"] == assignee]
        results.sort(key=lambda i: i["updated_at"], reverse=True)
        return {"status": "ok", "output": [self._serialize_issue(i) for i in results[:per_page]]}

    def get_issue(self, owner: str, repo: str, number: int) -> Dict[str, Any]:
        _u04_apply(self)
        for i in self.issues:
            if i["repo"] == repo and i["number"] == number:
                return {"status": "ok", "output": self._serialize_issue(i)}
        return {"status": "failed", "output": f"Issue {repo}#{number} not found"}

    def create_issue(self, owner: str, repo: str, title: str, body: str = "",
                     assignee: str | None = None, labels: List[str] | None = None) -> Dict[str, Any]:
        _u04_apply(self)
        if not any(r["owner"] == owner and r["name"] == repo for r in self.repos):
            return {"status": "failed", "output": f"Repo {owner}/{repo} not found"}
        next_number = max((i["number"] for i in self.issues if i["repo"] == repo), default=0) + 1
        issue = {
            "id": max(i["id"] for i in self.issues) + 1 if self.issues else 1,
            "number": next_number,
            "repo": repo,
            "title": title,
            "body": body or "",
            "state": "open",
            "user": self.user["login"],
            "assignee": assignee or "",
            "labels": labels or [],
            "milestone": None,
            "created_at": self._now(),
            "updated_at": self._now(),
            "closed_at": None,
            "is_pull_request": False,
        }
        self.issues.append(issue)
        for j, r in enumerate(self.repos):
            if r["owner"] == owner and r["name"] == repo:
                self.repos[j]["open_issues"] += 1
        return {"status": "ok", "output": self._serialize_issue(issue)}

    def update_issue(self, owner: str, repo: str, number: int, title: str | None = None,
                     body: str | None = None, state: str | None = None,
                     assignee: str | None = None, labels: List[str] | None = None) -> Dict[str, Any]:
        _u04_apply(self)
        for i, issue in enumerate(self.issues):
            if issue["repo"] == repo and issue["number"] == number:
                if title is not None:
                    self.issues[i]["title"] = title
                if body is not None:
                    self.issues[i]["body"] = body
                if assignee is not None:
                    self.issues[i]["assignee"] = assignee
                if labels is not None:
                    self.issues[i]["labels"] = labels
                if state and state != self.issues[i]["state"]:
                    self.issues[i]["state"] = state
                    if state == "closed":
                        self.issues[i]["closed_at"] = self._now()
                        for j, r in enumerate(self.repos):
                            if r["name"] == repo:
                                self.repos[j]["open_issues"] = max(0, self.repos[j]["open_issues"] - 1)
                    else:
                        self.issues[i]["closed_at"] = None
                self.issues[i]["updated_at"] = self._now()
                return {"status": "ok", "output": self._serialize_issue(self.issues[i])}
        return {"status": "failed", "output": f"Issue {repo}#{number} not found"}

    def list_pulls(self, owner: str, repo: str, state: str = "open") -> Dict[str, Any]:
        _u04_apply(self)
        if not any(r["owner"] == owner and r["name"] == repo for r in self.repos):
            return {"status": "failed", "output": f"Repo {owner}/{repo} not found"}
        pulls = [p for p in self.pulls if p.get("repo") == repo]
        issues_by_number = {i["number"]: i for i in self.issues if i["repo"] == repo}
        out = []
        for p in pulls:
            issue = issues_by_number.get(p["number"])
            if not issue:
                continue
            if state != "all" and issue["state"] != state:
                continue
            out.append({**self._serialize_issue(issue), **p, "issue_state": issue["state"]})
        return {"status": "ok", "output": out}

    def get_pull(self, owner: str, repo: str, number: int) -> Dict[str, Any]:
        _u04_apply(self)
        pull = next((p for p in self.pulls if p.get("repo") == repo and p.get("number") == number), None)
        issue = next((i for i in self.issues if i["repo"] == repo and i["number"] == number), None)
        if not pull or not issue:
            return {"status": "failed", "output": f"Pull {repo}#{number} not found"}
        return {"status": "ok", "output": {**self._serialize_issue(issue), **pull}}

    def merge_pull(self, owner: str, repo: str, number: int) -> Dict[str, Any]:
        _u04_apply(self)
        for i, p in enumerate(self.pulls):
            if p.get("repo") == repo and p.get("number") == number:
                if not p.get("mergeable"):
                    return {"status": "failed", "output": "PR is not mergeable"}
                if p.get("draft"):
                    return {"status": "failed", "output": "PR is a draft"}
                self.pulls[i]["merged"] = True
                self.update_issue(owner, repo, number, state="closed")
                return {"status": "ok", "output": {"merged": True, "sha": "deadbeefcafe123"}}
        return {"status": "failed", "output": f"Pull {repo}#{number} not found"}

    def list_comments(self, owner: str, repo: str, number: int) -> Dict[str, Any]:
        _u04_apply(self)
        if not any(i["repo"] == repo and i["number"] == number for i in self.issues):
            return {"status": "failed", "output": f"Issue {repo}#{number} not found"}
        return {"status": "ok", "output": [c for c in self.comments if c["repo"] == repo and c["issue_number"] == number]}

    def create_comment(self, owner: str, repo: str, number: int, body: str) -> Dict[str, Any]:
        _u04_apply(self)
        if not any(i["repo"] == repo and i["number"] == number for i in self.issues):
            return {"status": "failed", "output": f"Issue {repo}#{number} not found"}
        comment = {
            "id": max(c["id"] for c in self.comments) + 1 if self.comments else 1,
            "issue_number": number,
            "repo": repo,
            "user": self.user["login"],
            "body": body,
            "created_at": self._now(),
        }
        self.comments.append(comment)
        return {"status": "ok", "output": comment}


    def update_comment(self, owner: str, repo: str, comment_id: int, body: str) -> Dict[str, Any]:
        _u04_apply(self)
        c = next((x for x in self.comments if x["id"] == int(comment_id) and x["repo"] == repo), None)
        if not c:
            return {"status": "failed", "output": f"Comment {comment_id} not found in {repo}"}
        c["body"] = body
        c["updated_at"] = self._now()
        return {"status": "ok", "output": c}

    def delete_comment(self, owner: str, repo: str, comment_id: int) -> Dict[str, Any]:
        _u04_apply(self)
        idx = next((i for i, c in enumerate(self.comments) if c["id"] == int(comment_id) and c["repo"] == repo), None)
        if idx is None:
            return {"status": "failed", "output": f"Comment {comment_id} not found in {repo}"}
        self.comments.pop(idx)
        return {"status": "ok", "output": {"id": comment_id, "deleted": True}}



    def delete_issue(self, owner: str, repo: str, number: int) -> dict:
        _u04_apply(self)
        idx = next((i for i, iss in enumerate(self.issues) if iss["repo"] == repo and iss["number"] == int(number)), None)
        if idx is None:
            return {"status": "failed", "output": f"Issue {number} not found in {owner}/{repo}"}
        self.issues.pop(idx)
        return {"status": "ok", "output": {}}

if __name__ == "__main__":
    s = GithubSession(seed=12)
    print(s.get_user())
    print(s.list_repos())
