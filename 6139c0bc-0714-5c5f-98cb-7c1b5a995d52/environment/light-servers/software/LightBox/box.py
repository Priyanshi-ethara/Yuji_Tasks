import random
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

CORPUS_PATH = Path(__file__).resolve().parent / "corpus"


def _to_int(v) -> int:
    if v is None or (isinstance(v, str) and v.strip() == ""):
        return 0
    try:
        return int(str(v).strip())
    except (TypeError, ValueError):
        return 0


_DOWNLOAD_TEXT_MIMES = (
    "application/json",
    "application/xml",
    "application/x-yaml",
    "application/yaml",
    "text/yaml",
    "text/csv",
    "application/csv",
)
_DOWNLOAD_PDF_MIME = "application/pdf"
_DOWNLOAD_MAX_TEXT_BYTES_DEFAULT = 30_000_000
_DOWNLOAD_EXT_MIMES = {
    ".md": "text/markdown",
    ".markdown": "text/markdown",
    ".txt": "text/plain",
    ".csv": "text/csv",
    ".json": "application/json",
    ".xml": "application/xml",
    ".yaml": "application/yaml",
    ".yml": "application/yaml",
    ".pdf": "application/pdf",
}


def _is_downloadable_text_mime(mime: str) -> bool:
    m = (mime or "").split(";", 1)[0].strip().lower()
    if not m:
        return False
    if m.startswith("text/"):
        return True
    return m in _DOWNLOAD_TEXT_MIMES


def _guess_download_mime(name: str) -> str:
    import mimetypes
    ext = Path(name).suffix.lower()
    if ext in _DOWNLOAD_EXT_MIMES:
        return _DOWNLOAD_EXT_MIMES[ext]
    mime, _ = mimetypes.guess_type(name)
    return mime or "application/octet-stream"


# The user whose token is used (the "me" of /2.0/users/me).
_ME = "11446498"

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

_T02_FILES = [{'id': '910099', 'name': 'KEV-RE-26-0819 reissued invoice TPC-19 2026-08.csv', 'parent_id': '720100', 'owner_id': '11446511', 'description': 'Reissued invoice from Kessler Energie Vertrieb — replaces KEV-26-0819 for August 2026 (CT ratio correction)', 'size': 401, 'extension': 'csv', 'sha1': '0d1e2f3a4b5c6d7e8f9012345678901234567899', 'created_at': '2026-11-11T09:05:00.000Z', 'modified_at': '2026-11-11T09:05:00.000Z'}, {'id': '910098', 'name': 'KEV-RE-26-0918 reissued invoice TPC-18 2026-09.csv', 'parent_id': '720100', 'owner_id': '11446511', 'description': 'Reissued invoice from Kessler Energie Vertrieb — replaces KEV-26-0918 for September 2026 (off-peak register restored)', 'size': 373, 'extension': 'csv', 'sha1': '0d1e2f3a4b5c6d7e8f9012345678901234567898', 'created_at': '2026-11-11T09:05:30.000Z', 'modified_at': '2026-11-11T09:05:30.000Z'}]
_T02_BLOBS = {'KEV-RE-26-0819 reissued invoice TPC-19 2026-08.csv': 'site_code,account_no,supplier,invoice_no,period_start,period_end,read_type,consumption_kwh,amount,currency,posted_on,replaces_invoice_no,reason\nTPC-19,KEV-DE-71388,Kessler Energie Vertrieb,KEV-RE-26-0819,2026-08-01,2026-08-31,A,371200,97996.80,EUR,2026-11-11,KEV-26-0819,"CT ratio corrected from 200/5 to 250/5 after the 2026-08-03 metering transformer change; original overstated consumption by 25%"\n', 'KEV-RE-26-0918 reissued invoice TPC-18 2026-09.csv': 'site_code,account_no,supplier,invoice_no,period_start,period_end,read_type,consumption_kwh,amount,currency,posted_on,replaces_invoice_no,reason\nTPC-18,KEV-DE-71104,Kessler Energie Vertrieb,KEV-RE-26-0918,2026-09-01,2026-09-30,A,650310,171681.84,EUR,2026-11-11,KEV-26-0918,"Off-peak register 1.8.2 omitted after the billing-platform migration; reissued with both registers"\n'}
# ======================================================================================


class BoxSession:
    """Deterministic sandbox for the Box mock, ported from the FastAPI service.

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

            info = corpus_registry.load(CORPUS_PATH / "box.yaml")

            self.users: List[Dict[str, Any]] = [
                {
                    "id": r["id"],
                    "name": r["name"],
                    "login": r["login"],
                    "role": r["role"],
                    "status": r["status"],
                    "language": r["language"],
                    "timezone": r["timezone"],
                    "space_amount": _to_int(r.get("space_amount", 0)),
                    "space_used": _to_int(r.get("space_used", 0)),
                    "max_upload_size": _to_int(r.get("max_upload_size", 0)),
                    "job_title": r["job_title"],
                    "phone": r["phone"],
                    "created_at": r["created_at"],
                }
                for r in info.get("users", [])
            ]
            self.folders: List[Dict[str, Any]] = [
                {
                    "id": r["id"],
                    "name": r["name"],
                    "parent_id": r["parent_id"],
                    "owner_id": r["owner_id"],
                    "description": r["description"],
                    "created_at": r["created_at"],
                    "modified_at": r["modified_at"],
                    "item_count": _to_int(r.get("item_count", 0)),
                }
                for r in info.get("folders", [])
            ]
            self.files: List[Dict[str, Any]] = [
                {
                    "id": r["id"],
                    "name": r["name"],
                    "parent_id": r["parent_id"],
                    "owner_id": r["owner_id"],
                    "description": r["description"],
                    "size": _to_int(r.get("size", 0)),
                    "extension": r["extension"],
                    "sha1": r["sha1"],
                    "created_at": r["created_at"],
                    "modified_at": r["modified_at"],
                }
                for r in info.get("files", [])
            ]
            self.file_blobs: Dict[str, str] = dict(info.get("file_blobs", {}))
            from software.utils.world_data import hydrate as _hydrate_world_data
            _hydrate_world_data(self, 'LightBox')
        else:
            # Seedless: world loaded verbatim from the frozen snapshot.
            restore_into(self, Path(__file__).resolve().parent / "world.pkl")
            self.os = connect_os(os_cfg)

    def get_session_dict(self):
        return {"files": self.files}

    # --- helpers -----------------------------------------------------------
    def _now(self) -> str:
        return self.os.now()

    def uuid(self) -> str:
        alphabet = "0123456789"
        return ''.join(self.rng.choices(alphabet, k=6))

    def _user_mini(self, user_id):
        u = next((x for x in self.users if x["id"] == user_id), None)
        if not u:
            return None
        return {"type": "user", "id": u["id"], "name": u["name"], "login": u["login"]}

    def _folder_mini(self, folder_id):
        f = next((x for x in self.folders if x["id"] == folder_id), None)
        if not f:
            return None
        return {"type": "folder", "id": f["id"], "name": f["name"]}

    def _serialize_user(self, u):
        return {
            "type": "user",
            "id": u["id"],
            "name": u["name"],
            "login": u["login"],
            "role": u["role"],
            "status": u["status"],
            "language": u["language"],
            "timezone": u["timezone"],
            "space_amount": u["space_amount"],
            "space_used": u["space_used"],
            "max_upload_size": u["max_upload_size"],
            "job_title": u["job_title"],
            "phone": u["phone"],
            "created_at": u["created_at"],
        }

    def _serialize_folder(self, f):
        return {
            "type": "folder",
            "id": f["id"],
            "name": f["name"],
            "description": f["description"],
            "size": sum(x["size"] for x in self.files if x["parent_id"] == f["id"]),
            "created_at": f["created_at"],
            "modified_at": f["modified_at"],
            "item_count": f["item_count"],
            "parent": self._folder_mini(f["parent_id"]) if f["parent_id"] else None,
            "owned_by": self._user_mini(f["owner_id"]),
        }

    def _serialize_file(self, f):
        return {
            "type": "file",
            "id": f["id"],
            "name": f["name"],
            "description": f["description"],
            "size": f["size"],
            "extension": f["extension"],
            "sha1": f["sha1"],
            "created_at": f["created_at"],
            "modified_at": f["modified_at"],
            "parent": self._folder_mini(f["parent_id"]),
            "owned_by": self._user_mini(f["owner_id"]),
        }

    def _extract_file_content_text(self, basename, mime_type, max_text_bytes=None):
        import os
        if max_text_bytes is None:
            env_v = os.environ.get("WCB_DOWNLOAD_MAX_BYTES", "").strip()
            try:
                max_text_bytes = int(env_v) if env_v else _DOWNLOAD_MAX_TEXT_BYTES_DEFAULT
            except ValueError:
                max_text_bytes = _DOWNLOAD_MAX_TEXT_BYTES_DEFAULT

        if (
            "/" in basename
            or "\\" in basename
            or basename in ("", ".", "..")
            or basename.startswith(".")
        ):
            return {"error": True, "message": f"basename {basename!r} is not a single safe path component"}

        mime = (mime_type or "").split(";", 1)[0].strip().lower()
        is_pdf = mime == _DOWNLOAD_PDF_MIME

        if not is_pdf and not _is_downloadable_text_mime(mime):
            return {"error": True, "message": (
                f"mime {mime!r} not supported; only text/*, "
                "application/json|xml|yaml|csv, and application/pdf are downloadable"
            )}

        if basename not in self.file_blobs:
            return {"error": True, "message": f"file_blob {basename!r} not found in corpus"}

        raw = self.file_blobs[basename]

        if is_pdf:
            try:
                from pypdf import PdfReader  # type: ignore
                import io
                reader = PdfReader(io.BytesIO(raw.encode("utf-8", errors="replace")))
                parts = []
                for idx, page in enumerate(reader.pages, start=1):
                    page_text = page.extract_text() or ""
                    parts.append(f"--- page {idx} ---\n{page_text}".rstrip())
                text = "\n\n".join(parts)
            except ImportError as exc:
                return {"error": True, "message": f"pypdf not installed in this container: {exc}"}
            except Exception as exc:
                return {"error": True, "message": f"could not parse PDF: {exc}"}
        else:
            text = raw

        size_bytes = len(text.encode("utf-8"))
        if size_bytes > max_text_bytes:
            return {"error": True, "message": (
                f"extracted text {size_bytes} bytes exceeds cap {max_text_bytes}"
            )}

        return {"error": False, "text": text}

    # ---- task world rule (T02): once the first FY2026 inventory item has been written, Kessler Energie's
    # reissued invoices (Leipzig August, Stuttgart September) are filed by Facilities in the invoice folder
    # (applied once per session, before every tool call and before the sign-out dump).
    def _t02_apply(self):
        if self.__dict__.get("_t02_done") or not _t02_fired("t02_reissue"):
            return
        self.__dict__["_t02_done"] = True
        have = {f["id"] for f in self.files}
        for f in _T02_FILES:
            if f["id"] not in have:
                self.files.append(dict(f))
        self.file_blobs.update(_T02_BLOBS)

    # --- API methods -------------------------------------------------------
    def get_me(self) -> Dict[str, Any]:
        u = next((x for x in self.users if x["id"] == _ME), self.users[0])
        return {"status": "ok", "output": self._serialize_user(u)}

    def get_folder(self, folder_id: str) -> Dict[str, Any]:
        f = next((x for x in self.folders if x["id"] == str(folder_id)), None)
        if not f:
            return {"status": "failed", "output": f"Folder {folder_id} not found"}
        return {"status": "ok", "output": self._serialize_folder(f)}

    def get_folder_items(self, folder_id: str, limit: int = 100, offset: int = 0) -> Dict[str, Any]:
        if not any(x["id"] == str(folder_id) for x in self.folders):
            return {"status": "failed", "output": f"Folder {folder_id} not found"}
        folders = [self._serialize_folder(x) for x in self.folders
                   if x["parent_id"] == str(folder_id)]
        files = [self._serialize_file(x) for x in self.files
                 if x["parent_id"] == str(folder_id)]
        entries = folders + files
        total = len(entries)
        page = entries[offset:offset + limit]
        return {"status": "ok", "output": {
            "total_count": total,
            "entries": page,
            "offset": offset,
            "limit": limit,
        }}

    def get_file(self, file_id: str) -> Dict[str, Any]:
        f = next((x for x in self.files if x["id"] == str(file_id)), None)
        if not f:
            return {"status": "failed", "output": f"File {file_id} not found"}
        return {"status": "ok", "output": self._serialize_file(f)}

    def download_file(self, file_id: str) -> Dict[str, Any]:
        f = next((x for x in self.files if x["id"] == str(file_id)), None)
        if not f:
            return {"status": "failed", "output": f"File {file_id} not found"}
        name = f["name"]
        mime_type = _guess_download_mime(name)
        res = self._extract_file_content_text(name, mime_type)
        if res.get("error"):
            return {"status": "failed", "output": res["message"]}
        text = res["text"]
        return {"status": "ok", "output": {
            "file_id": str(file_id),
            "name": name,
            "mime_type": mime_type,
            "size_bytes": len(text.encode("utf-8")),
            "content": text,
        }}

    def search(self, query: str | None = None, type: str | None = None,
               limit: int = 100, offset: int = 0) -> Dict[str, Any]:
        q = (query or "").lower()
        type_filter = type
        entries = []
        if type_filter in (None, "folder"):
            for f in self.folders:
                if q in f["name"].lower():
                    entries.append(self._serialize_folder(f))
        if type_filter in (None, "file"):
            for f in self.files:
                if q in f["name"].lower():
                    entries.append(self._serialize_file(f))
        total = len(entries)
        page = entries[offset:offset + limit]
        return {"status": "ok", "output": {
            "total_count": total,
            "entries": page,
            "offset": offset,
            "limit": limit,
        }}


    def create_folder(self, name: str, parent_id: str) -> Dict[str, Any]:
        parent = next((f for f in self.folders if f["id"] == str(parent_id)), None)
        if not parent:
            return {"status": "failed", "output": f"Parent folder {parent_id} not found"}
        now = self._now()
        folder = {
            "id": self.uuid(),
            "name": name,
            "parent_id": str(parent_id),
            "owner_id": self.users[0]["id"] if self.users else "0",
            "description": "",
            "created_at": now,
            "modified_at": now,
            "item_count": 0,
        }
        self.folders.append(folder)
        return {"status": "ok", "output": self._serialize_folder(folder)}

    def upload_file(self, name: str, parent_id: str, content: str, description: str = "") -> Dict[str, Any]:
        parent = next((f for f in self.folders if f["id"] == str(parent_id)), None)
        if not parent:
            return {"status": "failed", "output": f"Parent folder {parent_id} not found"}
        ext = name.rsplit(".", 1)[-1].lower() if "." in name else ""
        now = self._now()
        file_obj = {
            "id": self.uuid(),
            "name": name,
            "parent_id": str(parent_id),
            "owner_id": self.users[0]["id"] if self.users else "0",
            "description": description,
            "size": len(content.encode("utf-8")),
            "extension": ext,
            "sha1": (self.uuid() * 7)[:40],
            "created_at": now,
            "modified_at": now,
        }
        self.files.append(file_obj)
        if not hasattr(self, "file_blobs"):
            self.file_blobs = {}
        self.file_blobs[name] = content
        return {"status": "ok", "output": self._serialize_file(file_obj)}

    def update_file(self, file_id: str, name: str | None = None, description: str | None = None) -> Dict[str, Any]:
        f = next((x for x in self.files if x["id"] == str(file_id)), None)
        if not f:
            return {"status": "failed", "output": f"File {file_id} not found"}
        if name is not None:
            f["name"] = name
        if description is not None:
            f["description"] = description
        f["modified_at"] = self._now()
        return {"status": "ok", "output": self._serialize_file(f)}

    def delete_file(self, file_id: str) -> Dict[str, Any]:
        idx = next((i for i, f in enumerate(self.files) if f["id"] == str(file_id)), None)
        if idx is None:
            return {"status": "failed", "output": f"File {file_id} not found"}
        self.files.pop(idx)
        return {"status": "ok", "output": {"id": file_id, "deleted": True}}




def _t02_guarded(fn):
    @_t02_ft.wraps(fn)
    def inner(self, *a, **k):
        self._t02_apply()
        return fn(self, *a, **k)
    return inner


for _t02_n, _t02_f in list(vars(BoxSession).items()):
    if callable(_t02_f) and _t02_n != "_t02_apply" and (not _t02_n.startswith("_") or _t02_n == "get_session_dict"):
        setattr(BoxSession, _t02_n, _t02_guarded(_t02_f))
# ======================================================================================

if __name__ == "__main__":
    s = BoxSession(seed=12)
    print(s.get_me())
    print(s.get_folder("0"))
    print(s.search(query="a"))
