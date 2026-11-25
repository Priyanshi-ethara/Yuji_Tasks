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

# MetDesk reissues: once flag nfg_skelwith_reissue exists, the Skelwith Edge station forecast carries
# the winds MetDesk reissued after the anemometer icing cleared; once nfg_warm_front exists, the
# Coldfell Moor and Harrowgate Pike forecasts carry the temperatures of amendment AMD-1116-02.
# Values are per 3-hourly step, in step order (2026-11-16 18:00 ... 2026-11-18 06:00).
_WR_STEPS_TXT = _wr_json.loads("[\"2026-11-16 18:00:00\", \"2026-11-16 21:00:00\", \"2026-11-17 00:00:00\", \"2026-11-17 03:00:00\", \"2026-11-17 06:00:00\", \"2026-11-17 09:00:00\", \"2026-11-17 12:00:00\", \"2026-11-17 15:00:00\", \"2026-11-17 18:00:00\", \"2026-11-17 21:00:00\", \"2026-11-18 00:00:00\", \"2026-11-18 03:00:00\", \"2026-11-18 06:00:00\"]")
_WR_EVENTS = (
    ("nfg_skelwith_reissue", "wind_speed", _wr_json.loads("{\"9104101\": [3.0, 6.5, 7.0, 6.0, 5.0, 4.0, 4.5, 5.5, 6.5, 7.5, 8.0, 7.5, 7.0]}")),
    ("nfg_warm_front", "temp", _wr_json.loads("{\"9104102\": [2.9, 2.3, 2.4, 2.6, 4.1, 5.9, 6.8, 6.3, 5.0, 4.4, 4.0, 3.6, 3.3], \"9104103\": [2.4, 1.9, 1.9, 2.2, 3.5, 5.1, 5.9, 5.6, 4.4, 3.6, 3.1, 2.8, 2.6]}")),
)


def _wr_apply(session):
    done = session.__dict__.setdefault("_wr_done", set())
    for flag, field, by_city in _WR_EVENTS:
        if flag in done or not _wr_fired(flag):
            continue
        done.add(flag)
        for row in getattr(session, "forecast", []):
            vals = by_city.get(str(row.get("city_id")))
            if not vals or row.get("dt_txt") not in _WR_STEPS_TXT:
                continue
            v = vals[_WR_STEPS_TXT.index(row["dt_txt"])]
            row[field] = v
            if field == "temp":
                row["temp_min"] = round(v - 0.3, 1)
                row["temp_max"] = round(v + 0.3, 1)
                row["feels_like"] = round(v - 0.18 * row.get("wind_speed", 0) - 1.0, 1)
            else:
                row["feels_like"] = round(row.get("temp", 0) - 0.18 * v - 1.0, 1)


class OpenweatherSession:
    """Deterministic sandbox for the OpenWeather API mock, ported from the FastAPI service."""

    def __init__(self, os_cfg, seed=None):
        # Seedless: world loaded verbatim from a frozen snapshot next to
        # this module; `seed` is accepted for client compat and ignored.
        if seed_mode():
            # Seed architecture: world rolled from a seed (re-armed).
            self.rng = random.Random(resolve_seed(seed))
            self.os = connect_os(os_cfg)
            self.time_machine = TimeMachine(rng=self.rng)

            info = corpus_registry.load(CORPUS_PATH / "openweather.yaml")

            self.cities: List[Dict[str, Any]] = [
                {
                    "id": int(r["id"]),
                    "name": r["name"],
                    "country": r["country"],
                    "state": (str(r.get("state") or "") or None),
                    "lat": float(r["lat"]),
                    "lon": float(r["lon"]),
                    "timezone": int(r["timezone"]),
                }
                for r in info.get("cities", [])
            ]
            self.current: List[Dict[str, Any]] = [
                {
                    "city_id": int(r["city_id"]),
                    "weather_id": int(r["weather_id"]),
                    "weather_main": r["weather_main"],
                    "weather_description": r["weather_description"],
                    "weather_icon": r["weather_icon"],
                    "temp": float(r["temp"]),
                    "feels_like": float(r["feels_like"]),
                    "temp_min": float(r["temp_min"]),
                    "temp_max": float(r["temp_max"]),
                    "pressure": int(r["pressure"]),
                    "humidity": int(r["humidity"]),
                    "wind_speed": float(r["wind_speed"]),
                    "wind_deg": int(r["wind_deg"]),
                    "clouds": int(r["clouds"]),
                    "visibility": int(r["visibility"]),
                    "dt": int(r["dt"]),
                }
                for r in info.get("current_weather", [])
            ]
            self.forecast: List[Dict[str, Any]] = [
                {
                    "city_id": int(r["city_id"]),
                    "dt": int(r["dt"]),
                    "dt_txt": r["dt_txt"],
                    "temp": float(r["temp"]),
                    "feels_like": float(r["feels_like"]),
                    "temp_min": float(r["temp_min"]),
                    "temp_max": float(r["temp_max"]),
                    "pressure": int(r["pressure"]),
                    "humidity": int(r["humidity"]),
                    "weather_id": int(r["weather_id"]),
                    "weather_main": r["weather_main"],
                    "weather_description": r["weather_description"],
                    "weather_icon": r["weather_icon"],
                    "wind_speed": float(r["wind_speed"]),
                    "wind_deg": int(r["wind_deg"]),
                    "clouds": int(r["clouds"]),
                    "pop": float(r["pop"]),
                }
                for r in info.get("forecast", [])
            ]
            from software.utils.world_data import hydrate as _hydrate_world_data
            _hydrate_world_data(self, 'LightOpenWeather')
        else:
            # Seedless: world loaded verbatim from the frozen snapshot.
            restore_into(self, Path(__file__).resolve().parent / "world.pkl")
            self.os = connect_os(os_cfg)

    def get_session_dict(self):
        return {"cities": self.cities}

    # --- helpers -----------------------------------------------------------
    def _now(self) -> str:
        return self.os.now()

    def _find_city_by_name(self, q):
        if not q:
            return None
        name = q.split(",")[0].strip().lower()
        for c in self.cities:
            if c["name"].lower() == name:
                return c
        for c in self.cities:
            if name in c["name"].lower():
                return c
        return None

    def _find_city_by_coords(self, lat, lon):
        best = None
        best_d = None
        for c in self.cities:
            d = (c["lat"] - lat) ** 2 + (c["lon"] - lon) ** 2
            if best_d is None or d < best_d:
                best_d = d
                best = c
        return best

    def _current_for(self, city_id):
        for w in self.current:
            if w["city_id"] == city_id:
                return w
        return None

    def _weather_block(self, rec):
        return [{
            "id": rec["weather_id"],
            "main": rec["weather_main"],
            "description": rec["weather_description"],
            "icon": rec["weather_icon"],
        }]

    def _current_payload(self, city, w):
        return {
            "coord": {"lon": city["lon"], "lat": city["lat"]},
            "weather": self._weather_block(w),
            "base": "stations",
            "main": {
                "temp": w["temp"],
                "feels_like": w["feels_like"],
                "temp_min": w["temp_min"],
                "temp_max": w["temp_max"],
                "pressure": w["pressure"],
                "humidity": w["humidity"],
            },
            "visibility": w["visibility"],
            "wind": {"speed": w["wind_speed"], "deg": w["wind_deg"]},
            "clouds": {"all": w["clouds"]},
            "dt": w["dt"],
            "sys": {"country": city["country"]},
            "timezone": city["timezone"],
            "id": city["id"],
            "name": city["name"],
            "cod": 200,
        }

    def _forecast_item(self, rec):
        return {
            "dt": rec["dt"],
            "main": {
                "temp": rec["temp"],
                "feels_like": rec["feels_like"],
                "temp_min": rec["temp_min"],
                "temp_max": rec["temp_max"],
                "pressure": rec["pressure"],
                "humidity": rec["humidity"],
            },
            "weather": self._weather_block(rec),
            "clouds": {"all": rec["clouds"]},
            "wind": {"speed": rec["wind_speed"], "deg": rec["wind_deg"]},
            "pop": rec["pop"],
            "dt_txt": rec["dt_txt"],
        }

    # --- Current weather ---------------------------------------------------
    def get_current_weather(self, q: str | None = None, lat: float | None = None,
                            lon: float | None = None) -> Dict[str, Any]:
        if q:
            city = self._find_city_by_name(q)
        elif lat is not None and lon is not None:
            city = self._find_city_by_coords(lat, lon)
        else:
            return {"status": "failed", "output": "Nothing to geocode"}
        if not city:
            return {"status": "failed", "output": "city not found"}
        w = self._current_for(city["id"])
        if not w:
            return {"status": "failed", "output": "city not found"}
        return {"status": "ok", "output": self._current_payload(city, w)}

    # --- Forecast ----------------------------------------------------------
    def get_forecast(self, q: str | None = None, lat: float | None = None,
                     lon: float | None = None) -> Dict[str, Any]:
        if q:
            city = self._find_city_by_name(q)
        elif lat is not None and lon is not None:
            city = self._find_city_by_coords(lat, lon)
        else:
            return {"status": "failed", "output": "Nothing to geocode"}
        if not city:
            return {"status": "failed", "output": "city not found"}
        rows = [r for r in self.forecast if r["city_id"] == city["id"]]
        rows.sort(key=lambda r: r["dt"])
        items = [self._forecast_item(r) for r in rows]
        return {"status": "ok", "output": {
            "cod": "200",
            "message": 0,
            "cnt": len(items),
            "list": items,
            "city": {
                "id": city["id"],
                "name": city["name"],
                "coord": {"lat": city["lat"], "lon": city["lon"]},
                "country": city["country"],
                "timezone": city["timezone"],
            },
        }}

    # --- Geocoding ---------------------------------------------------------
    def geocode_direct(self, q: str, limit: int = 5) -> Dict[str, Any]:
        name = (q or "").split(",")[0].strip().lower()
        matches = [c for c in self.cities if name and name in c["name"].lower()]
        out = []
        for c in matches[:limit]:
            out.append({
                "name": c["name"],
                "lat": c["lat"],
                "lon": c["lon"],
                "country": c["country"],
                "state": c["state"],
            })
        return {"status": "ok", "output": out}



    def save_location(self, name: str, lat: float | None = None, lon: float | None = None) -> Dict[str, Any]:
        if not hasattr(self, 'saved_locations'):
            self.saved_locations = []
        if any(loc["name"] == name for loc in self.saved_locations):
            return {"status": "failed", "output": f"Location '{name}' already saved"}
        entry = {"name": name, "lat": lat, "lon": lon, "saved_at": self._now()}
        self.saved_locations.append(entry)
        return {"status": "ok", "output": entry}

    def list_saved_locations(self) -> Dict[str, Any]:
        if not hasattr(self, 'saved_locations'):
            self.saved_locations = []
        return {"status": "ok", "output": list(self.saved_locations)}

    def delete_saved_location(self, name: str) -> Dict[str, Any]:
        if not hasattr(self, 'saved_locations'):
            self.saved_locations = []
        before = len(self.saved_locations)
        self.saved_locations = [loc for loc in self.saved_locations if loc["name"] != name]
        if len(self.saved_locations) == before:
            return {"status": "failed", "output": f"Saved location '{name}' not found"}
        return {"status": "ok", "output": {"deleted_name": name}}

    def update_saved_location(self, name: str, new_name: str | None = None, lat: float | None = None, lon: float | None = None) -> Dict[str, Any]:
        if not hasattr(self, 'saved_locations'):
            self.saved_locations = []
        for loc in self.saved_locations:
            if loc["name"] == name:
                if new_name is not None:
                    loc["name"] = new_name
                if lat is not None:
                    loc["lat"] = lat
                if lon is not None:
                    loc["lon"] = lon
                return {"status": "ok", "output": loc}
        return {"status": "failed", "output": f"Saved location '{name}' not found"}


def _wr_wrap(cls, hook):
    """Apply pending world events at the start of every public method (tools and get_session_dict)."""
    import functools
    for _name, _fn in list(vars(cls).items()):
        if _name.startswith("_") or not callable(_fn):
            continue

        def _make(fn):
            @functools.wraps(fn)
            def _inner(self, *a, **k):
                hook(self)
                return fn(self, *a, **k)
            return _inner
        setattr(cls, _name, _make(_fn))


_wr_wrap(OpenweatherSession, _wr_apply)

if __name__ == "__main__":
    s = OpenweatherSession(seed=12)
    print(s.geocode_direct("London"))
    print(s.get_current_weather(q="London"))
