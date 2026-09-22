"""D-076: recurring bot work. Schedules live in registry/schedules.json (git-tracked, owner-readable):
  {"<sid>": {"bot_id": "018", "cron": "0 7 * * *", "task": "...", "in": "C:\\...\\inbox\\orders", "enabled": true,
             "created": ..., "last_fire": "...", "runs": N}}
A `tick` job (chained hourly by the probe, or on demand) enqueues one `run` job per due schedule, idempotent per
(schedule, fire minute), so a slept laptop catches up exactly once and never double-runs.

  python tools/factory_schedule.py add <bot_id> "<cron>" --task "..." [--in DIR]
  python tools/factory_schedule.py list | remove <sid> | enable <sid> | disable <sid> | due
"""
from __future__ import annotations
import json, os, sys, time, uuid, pathlib, datetime
ROOT = pathlib.Path(os.environ.get("AIFACTORY_REPO", pathlib.Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(ROOT / "core"))
from factory.cron import next_fire, parse          # noqa: E402
from factory.registry import Registry              # noqa: E402
PATH = ROOT / "registry" / "schedules.json"
MAX_CATCHUP = 1          # a slept machine runs a missed schedule once, not once per missed slot


def load() -> dict:
    return json.loads(PATH.read_text(encoding="utf-8")) if PATH.exists() else {}


def save(d: dict) -> None:
    PATH.parent.mkdir(exist_ok=True); PATH.write_text(json.dumps(d, indent=2, sort_keys=True), encoding="utf-8")


def add(bot_id: str, cron: str, task: str, in_dir: str | None = None, actor: str = "owner") -> dict:
    parse(cron)                                                   # raises on bad cron
    e = Registry(ROOT / "registry").get("bots", bot_id)
    if e is None: raise ValueError(f"unknown bot {bot_id}")
    if e.status != "active": raise ValueError(f"bot {bot_id} is {e.status}; only active bots may be scheduled")
    if not task.strip(): raise ValueError("task required")
    d = load(); sid = uuid.uuid4().hex[:8]
    d[sid] = {"bot_id": bot_id, "cron": cron, "task": task.strip(), "in": in_dir, "enabled": True, "actor": actor,
              "created": datetime.datetime.now().isoformat(timespec="seconds"), "last_fire": None, "runs": 0,
              "next": next_fire(cron).isoformat(timespec="minutes")}
    save(d); return {"sid": sid, **d[sid]}


def set_enabled(sid: str, on: bool) -> dict:
    d = load()
    if sid not in d: raise ValueError(f"unknown schedule {sid}")
    d[sid]["enabled"] = on; save(d); return d[sid]


def remove(sid: str) -> bool:
    d = load(); ok = d.pop(sid, None) is not None; save(d); return ok


def due(now: datetime.datetime | None = None) -> list[tuple[str, dict, datetime.datetime]]:
    """Schedules whose next fire time is <= now. Fire time = the latest slot <= now (single catch-up)."""
    now = now or datetime.datetime.now(); out = []
    for sid, s in load().items():
        if not s.get("enabled", True): continue
        since = datetime.datetime.fromisoformat(s["last_fire"]) if s.get("last_fire") else datetime.datetime.fromisoformat(s["created"])
        nf = next_fire(s["cron"], since)
        if nf <= now:
            fire = nf
            while True:                                          # advance to the latest slot <= now
                nxt = next_fire(s["cron"], fire)
                if nxt > now: break
                fire = nxt
            out.append((sid, s, fire))
    return out


def tick(store, actor: str = "tick", now: datetime.datetime | None = None) -> dict:
    """Enqueue one `run` per due schedule; idempotent per (sid, fire minute) via the job idem key."""
    now = now or datetime.datetime.now(); d = load(); fired = []
    for sid, s, fire in due(now):
        e = Registry(ROOT / "registry").get("bots", s["bot_id"])
        if e is None or e.status != "active":
            store.audit("schedule.skipped", actor=actor, sid=sid, bot_id=s["bot_id"], reason=f"bot {e.status if e else 'missing'}"); continue
        payload = {"bot_id": s["bot_id"], "task": s["task"], "in": s.get("in"), "out": None, "cap": 300,
                   "schedule": sid, "fire": fire.isoformat(timespec="minutes")}
        idem = f"run:sched:{sid}:{payload['fire']}"
        row = store.db.execute("SELECT id FROM jobs WHERE idem=? OR idem LIKE ?", (idem, idem + ":%")).fetchone()
        if row:                                                  # slot already fired (even if that run finished) -> never twice
            d[sid]["last_fire"] = payload["fire"]; continue
        j = store.enqueue("run", payload, priority=5, idem=idem, actor=actor)
        d[sid]["last_fire"] = payload["fire"]; d[sid]["runs"] = int(d[sid].get("runs", 0)) + 1
        d[sid]["next"] = next_fire(s["cron"], fire).isoformat(timespec="minutes")
        fired.append({"sid": sid, "bot_id": s["bot_id"], "fire": payload["fire"], "job": j["id"][:8]})
        store.audit("schedule.fired", actor=actor, sid=sid, bot_id=s["bot_id"], fire=payload["fire"], job=j["id"][:8])
    save(d)
    return {"fired": fired, "schedules": len(d)}


def main(a: list[str]) -> int:
    if len(a) < 2: print(__doc__); return 2
    opt = lambda k, d=None: a[a.index(k) + 1] if k in a else d
    cmd = a[1]
    if cmd == "add":
        print(json.dumps(add(a[2].zfill(3), a[3], opt("--task", ""), opt("--in"), opt("--actor", "owner")), indent=1)); return 0
    if cmd == "list":
        for sid, s in sorted(load().items()):
            print(f"{sid} bot={s['bot_id']} cron='{s['cron']}' {'on ' if s.get('enabled', True) else 'off'} runs={s.get('runs', 0)} last={s.get('last_fire')} next={s.get('next')} task={s['task'][:50]!r}")
        return 0
    if cmd == "remove": print(json.dumps({"removed": remove(a[2])})); return 0
    if cmd in ("enable", "disable"): print(json.dumps(set_enabled(a[2], cmd == "enable"))); return 0
    if cmd == "due":
        for sid, s, fire in due(): print(sid, s["bot_id"], fire)
        return 0
    print(__doc__); return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
