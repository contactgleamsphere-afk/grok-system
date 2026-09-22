"""D-076: minimal 5-field cron (min hour dom mon dow) -> next fire time. Supports *, N, a-b, */n, a,b,c. Local time.
No external dependency; enough for 'every hour', 'daily at 07:00', 'weekdays 09:30'."""
from __future__ import annotations
import datetime


def _field(expr: str, lo: int, hi: int) -> set[int]:
    out: set[int] = set()
    for part in expr.split(","):
        step = 1
        if "/" in part:
            part, s = part.split("/", 1); step = int(s)
        if part == "*":
            a, b = lo, hi
        elif "-" in part:
            a, b = (int(x) for x in part.split("-", 1))
        else:
            a = b = int(part)
            if step > 1: b = hi
        if not (lo <= a <= hi and lo <= b <= hi and a <= b):
            raise ValueError(f"cron field {expr!r} out of range {lo}-{hi}")
        out.update(range(a, b + 1, step))
    return out


def parse(spec: str) -> tuple[set[int], set[int], set[int], set[int], set[int]]:
    f = spec.split()
    if len(f) != 5: raise ValueError(f"cron needs 5 fields: {spec!r}")
    return (_field(f[0], 0, 59), _field(f[1], 0, 23), _field(f[2], 1, 31), _field(f[3], 1, 12),
            {0 if d == 7 else d for d in _field(f[4], 0, 7)})   # 7 == Sunday == 0


def next_fire(spec: str, after: datetime.datetime | None = None) -> datetime.datetime:
    mins, hours, doms, mons, dows = parse(spec)
    t = (after or datetime.datetime.now()).replace(second=0, microsecond=0) + datetime.timedelta(minutes=1)
    for _ in range(366 * 24 * 60):
        # python weekday(): Mon=0..Sun=6 ; cron dow: Sun=0..Sat=6
        if t.month in mons and t.day in doms and ((t.weekday() + 1) % 7) in dows and t.hour in hours and t.minute in mins:
            return t
        t += datetime.timedelta(minutes=1)
    raise ValueError(f"cron {spec!r} never fires")
