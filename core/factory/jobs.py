"""Persistent job queue + audit trail for the AI Factory (SQLite, single file, crash-safe).

Jobs:   kind in {create, test, repair, monitor}; states queued -> running -> done | failed | paused | cancelled.
Leases: a worker claims a job with a lease (worker id + expiry). A crashed worker's lease expires and the job is
        re-claimed exactly once per attempt; attempts are counted so nothing loops forever.
Idempotency: every job carries an `idem` key (e.g. create:<sha of objective>) — enqueueing the same work twice
        returns the existing job instead of a duplicate.
Audit:  append-only `audit` table; every state change and every factory event (build, test, repair, promote,
        demote, permission check, failure) is a row. `audit_export()` renders AUDIT.md.
Failure classes (D-031): transient (retry, same lane) | quota (retry later, other lane) | model (retry other lane)
        | logic (pause: needs human/architect) | security (pause + never auto-retry).
"""
from __future__ import annotations
import hashlib, json, os, sqlite3, time, uuid, datetime, pathlib
from typing import Any, Iterable

RETRY_POLICY = {"transient": (3, 60), "quota": (6, 900), "model": (3, 30), "logic": (0, 0), "security": (0, 0)}


def classify_failure(msg: str) -> str:
    m = (msg or "").lower()
    # explicit class prefix wins: "RuntimeError: transient: ..." / "security: ..." / "quota: ..."
    import re as _re
    mm = _re.match(r"^(?:\w+error:\s*)?(transient|quota|model|logic|security)\s*:", m)
    if mm:
        return mm.group(1)
    if m.startswith("security") or any(k in m for k in ("frozen fields changed", "reward hacking", "hard-code test answers", "escaped", "boundary expansion", "credential material",
                            "permission", "outside the workspace", "shell:system")):
        return "security"
    if any(k in m for k in ("429", "quota", "rate limit", "tokens per day", "tpd", "rpd", "daily")):
        return "quota"
    if any(k in m for k in ("timeout", "timed out", "connection", "tunnel", "temporarily", "503", "502", "runner error")):
        return "transient"
    if any(k in m for k in ("empty content", "not json", "usable instructions", "could not produce a valid spec",
                            "invalid spec", "parsing failed", "failed_generation", "context")):
        return "model"
    return "logic"


ONCE_PER_SLOT = ("monitor", "probe", "report", "tick", "insight", "bench", "canary", "scout", "selfpatch")


class JobStore:
    def __init__(self, path: str | os.PathLike):
        self.path = pathlib.Path(path); self.path.parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(self.path, isolation_level=None, timeout=30)   # autocommit; WAL for crash safety
        self.db.execute("PRAGMA journal_mode=WAL"); self.db.execute("PRAGMA synchronous=FULL")
        self.db.executescript("""
        CREATE TABLE IF NOT EXISTS jobs(
          id TEXT PRIMARY KEY, kind TEXT NOT NULL, payload TEXT NOT NULL, idem TEXT UNIQUE,
          state TEXT NOT NULL, priority INTEGER DEFAULT 5, attempts INTEGER DEFAULT 0, max_attempts INTEGER DEFAULT 3,
          not_before REAL DEFAULT 0, lease_owner TEXT, lease_until REAL, result TEXT, error TEXT, failure_class TEXT,
          created REAL NOT NULL, updated REAL NOT NULL, parent TEXT);
        CREATE TABLE IF NOT EXISTS audit(
          seq INTEGER PRIMARY KEY AUTOINCREMENT, ts REAL NOT NULL, job_id TEXT, bot_id TEXT, event TEXT NOT NULL,
          actor TEXT, detail TEXT);
        CREATE INDEX IF NOT EXISTS ix_jobs_state ON jobs(state, priority, created);
        """)

    # ---------------- audit
    def audit(self, event: str, *, job_id: str | None = None, bot_id: str | None = None,
              actor: str = "factory", **detail: Any) -> None:
        self.db.execute("INSERT INTO audit(ts,job_id,bot_id,event,actor,detail) VALUES(?,?,?,?,?,?)",
                        (time.time(), job_id, bot_id, event, actor, json.dumps(detail, default=str)[:4000]))

    def audit_rows(self, limit: int = 500, bot_id: str | None = None) -> list[dict]:
        q = "SELECT seq,ts,job_id,bot_id,event,actor,detail FROM audit"
        args: tuple = ()
        if bot_id: q += " WHERE bot_id=?"; args = (bot_id,)
        q += " ORDER BY seq DESC LIMIT ?"
        return [dict(zip(("seq", "ts", "job_id", "bot_id", "event", "actor", "detail"), r))
                for r in self.db.execute(q, args + (limit,))]

    def audit_sync_jsonl(self, dir_: pathlib.Path) -> int:
        """D-067: durable, append-only audit in git. Every row is appended exactly once to audit/YYYY-MM.jsonl
        (high-water mark = last seq present in the newest file). The SQLite table stays the working copy; the JSONL
        files are the record that survives a laptop loss and lets AUDIT.md be rebuilt for any period."""
        dir_.mkdir(parents=True, exist_ok=True)
        files = sorted(dir_.glob("*.jsonl"))
        last = 0
        if files:
            for line in reversed(files[-1].read_text(encoding="utf-8").splitlines()):
                if line.strip():
                    last = int(json.loads(line)["seq"]); break
        rows = self.db.execute("SELECT seq,ts,job_id,bot_id,event,actor,detail FROM audit WHERE seq>? ORDER BY seq", (last,)).fetchall()
        prev = self._last_hash(files[-1]) if files else "0" * 16
        n = 0
        for seq, ts, job_id, bot_id, event, actor, detail in rows:
            month = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m")
            row = {"seq": seq, "ts": round(ts, 3), "job": job_id, "bot": bot_id, "event": event, "actor": actor, "detail": json.loads(detail) if detail else {}}
            row["prev"] = prev; row["h"] = prev = self._row_hash(row)          # D-091: hash chain -> edits/deletions are detectable
            with (dir_ / f"{month}.jsonl").open("a", encoding="utf-8") as f:
                f.write(json.dumps(row, default=str) + "\n")
            n += 1
        return n

    @staticmethod
    def _row_hash(row: dict) -> str:
        body = {k: row[k] for k in ("seq", "ts", "job", "bot", "event", "actor", "detail", "prev")}
        return hashlib.sha256(json.dumps(body, sort_keys=True, default=str).encode()).hexdigest()[:16]

    @staticmethod
    def _last_hash(path: pathlib.Path) -> str:
        for line in reversed(path.read_text(encoding="utf-8").splitlines()):
            if line.strip():
                r = json.loads(line); return r.get("h") or "0" * 16     # pre-D-091 rows have no hash: chain starts after them
        return "0" * 16

    @staticmethod
    def audit_verify(dir_: pathlib.Path) -> dict:
        """D-091: walk audit/*.jsonl in order; every hashed row must reference the previous row's hash and hash to its own
        `h`. Returns {ok, rows, hashed, first_bad}. Rows written before D-091 (no `h`) are skipped but still counted."""
        prev = "0" * 16; rows = hashed = 0; first_bad = None; last_seq = 0
        for f in sorted(dir_.glob("*.jsonl")):
            for line in f.read_text(encoding="utf-8").splitlines():
                if not line.strip(): continue
                r = json.loads(line); rows += 1
                if r["seq"] <= last_seq and first_bad is None: first_bad = {"file": f.name, "seq": r["seq"], "why": "seq not increasing"}
                last_seq = r["seq"]
                if "h" not in r: continue
                hashed += 1
                if first_bad is None and (r.get("prev") != prev or JobStore._row_hash(r) != r["h"]):
                    first_bad = {"file": f.name, "seq": r["seq"], "why": "prev mismatch" if r.get("prev") != prev else "row altered"}
                prev = r["h"]
        return {"ok": first_bad is None, "rows": rows, "hashed": hashed, "first_bad": first_bad}

    def audit_export(self, path: pathlib.Path, limit: int = 400) -> None:
        rows = list(reversed(self.audit_rows(limit)))
        out = ["# AUDIT — append-only factory event log (latest %d)" % limit, "",
               "| seq | time | job | bot | event | actor | detail |", "|---|---|---|---|---|---|---|"]
        for r in rows:
            d = r["detail"].replace("|", "\\|")[:140]
            out.append(f"| {r['seq']} | {datetime.datetime.fromtimestamp(r['ts']):%Y-%m-%d %H:%M:%S} | {(r['job_id'] or '')[:8]} | "
                       f"{r['bot_id'] or ''} | {r['event']} | {r['actor']} | {d} |")
        path.write_text("\n".join(out) + "\n", encoding="utf-8")

    # ---------------- enqueue
    @staticmethod
    def idem_key(kind: str, payload: dict) -> str:
        return f"{kind}:" + hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()[:16]

    def enqueue(self, kind: str, payload: dict, *, priority: int = 5, max_attempts: int = 3,
                idem: str | None = None, parent: str | None = None, actor: str = "factory", not_before: float = 0.0) -> dict:
        if kind in ("create", "plan") and (not str(payload.get("objective", "")).strip() or str(payload["objective"]).startswith("-")):
            raise ValueError("objective must be non-empty text, not a flag")          # D-094: no architect call for empty/flag objectives
        idem = idem or self.idem_key(kind, payload)
        row = self.db.execute("SELECT id,state FROM jobs WHERE idem=?", (idem,)).fetchone()
        if row and row[1] in ("queued", "running", "paused"):
            self.audit("job.dedup", job_id=row[0], actor=actor, kind=kind)
            return self.get(row[0])
        if row and row[1] == "done" and kind in ONCE_PER_SLOT and any(k in payload for k in ("day", "hour", "week")) \
                and not payload.get("only") and not payload.get("lanes") and not payload.get("t"):   # owner-targeted requests stay re-runnable
            # D-101: slot-keyed housekeeping (monitor/day, probe/hour, report/day, tick/hour, insight/week) runs ONCE per
            # slot even if re-requested after it finished — 2026-09-24 the catch-up Monitor task + the report handler
            # produced two full 24-bot sweeps in one night.
            self.audit("job.dedup", job_id=row[0], actor=actor, kind=kind, note="slot already done")
            return self.get(row[0])
        if row:   # finished earlier -> new job with a fresh idem suffix (explicit re-run)
            idem = f"{idem}:{int(time.time())}"
        jid = uuid.uuid4().hex; now = time.time()
        self.db.execute("INSERT INTO jobs(id,kind,payload,idem,state,priority,max_attempts,created,updated,parent,not_before) "
                        "VALUES(?,?,?,?,'queued',?,?,?,?,?,?)",
                        (jid, kind, json.dumps(payload), idem, priority, max_attempts, now, now, parent, not_before))
        self.audit("job.enqueued", job_id=jid, bot_id=payload.get("bot_id"), actor=actor, kind=kind, payload=payload)
        return self.get(jid)

    def resolve(self, prefix: str) -> str:
        """Accept an 8-char job id prefix (as printed by `jobs`) or a full id."""
        rows = self.db.execute("SELECT id FROM jobs WHERE id LIKE ?", (prefix + "%",)).fetchall()
        if len(rows) != 1: raise KeyError(f"job id {prefix!r} matches {len(rows)} jobs")
        return rows[0][0]

    def get(self, jid: str) -> dict:
        r = self.db.execute("SELECT * FROM jobs WHERE id=?", (jid,)).fetchone()
        cols = [c[1] for c in self.db.execute("PRAGMA table_info(jobs)")]
        d = dict(zip(cols, r)); d["payload"] = json.loads(d["payload"]); return d

    def list(self, states: Iterable[str] | None = None) -> list[dict]:
        cols = [c[1] for c in self.db.execute("PRAGMA table_info(jobs)")]
        q = "SELECT * FROM jobs"; args: tuple = ()
        if states:
            s = list(states); q += " WHERE state IN (%s)" % ",".join("?" * len(s)); args = tuple(s)
        q += " ORDER BY created"
        out = []
        for r in self.db.execute(q, args):
            d = dict(zip(cols, r)); d["payload"] = json.loads(d["payload"]); out.append(d)
        return out

    # ---------------- leases (crash-safe claim)
    def claim(self, worker: str, lease_s: int = 1800, kinds: Iterable[str] | None = None) -> dict | None:
        now = time.time()
        # expire stale leases (crashed workers): back to queued, attempt already counted at claim time
        for (jid,) in self.db.execute("SELECT id FROM jobs WHERE state='running' AND lease_until<?", (now,)).fetchall():
            self.db.execute("UPDATE jobs SET state='queued',lease_owner=NULL,lease_until=NULL,updated=? WHERE id=?", (now, jid))
            self.audit("job.lease_expired", job_id=jid, actor=worker)
        q = "SELECT id FROM jobs WHERE state='queued' AND not_before<=? AND attempts<max_attempts"
        args: list = [now]
        if kinds:
            k = list(kinds); q += " AND kind IN (%s)" % ",".join("?" * len(k)); args += k
        # D-079: two workers may run concurrently, but never on the same bot (bundle/registry entry) at once
        q += (" AND (json_extract(payload,'$.bot_id') IS NULL OR json_extract(payload,'$.bot_id') NOT IN "
              "(SELECT json_extract(payload,'$.bot_id') FROM jobs WHERE state='running' AND json_extract(payload,'$.bot_id') IS NOT NULL))")
        q += " ORDER BY priority, created LIMIT 1"
        with self.db:   # BEGIN IMMEDIATE-style atomic claim
            self.db.execute("BEGIN IMMEDIATE")
            row = self.db.execute(q, args).fetchone()
            if not row:
                self.db.execute("COMMIT"); return None
            jid = row[0]
            self.db.execute("UPDATE jobs SET state='running',lease_owner=?,lease_until=?,attempts=attempts+1,updated=? "
                            "WHERE id=? AND state='queued'", (worker, now + lease_s, now, jid))
            self.db.execute("COMMIT")
        j = self.get(jid)
        self.audit("job.claimed", job_id=jid, bot_id=j["payload"].get("bot_id"), actor=worker, attempt=j["attempts"])
        return j

    def heartbeat(self, jid: str, worker: str, lease_s: int = 1800) -> str:
        """Extend the lease. Returns 'ok' | 'readopted' | 'lost'. D-081: after a laptop sleep the lease has expired and
        the job is back in 'queued' while THIS worker is still running it. If nobody else has claimed it, re-adopt
        atomically (same attempt, no duplicate work); if another worker holds it now, report 'lost' so the caller
        discards its result instead of overwriting the other worker's."""
        now = time.time()
        with self.db:
            cur = self.db.execute("UPDATE jobs SET lease_until=? WHERE id=? AND lease_owner=? AND state='running'", (now + lease_s, jid, worker))
            if cur.rowcount == 1: return "ok"
            cur = self.db.execute("UPDATE jobs SET state='running',lease_owner=?,lease_until=?,updated=? WHERE id=? AND state='queued'",
                                  (worker, now + lease_s, now, jid))
        if cur.rowcount == 1:
            self.audit("job.readopted", job_id=jid, actor=worker); return "readopted"
        return "lost"

    def owns(self, jid: str, worker: str) -> bool:
        r = self.db.execute("SELECT lease_owner, state FROM jobs WHERE id=?", (jid,)).fetchone()
        return bool(r) and r[1] == "running" and r[0] == worker

    def done(self, jid: str, result: dict, actor: str) -> None:
        self.db.execute("UPDATE jobs SET state='done',result=?,lease_owner=NULL,lease_until=NULL,updated=? WHERE id=?",
                        (json.dumps(result, default=str)[:20000], time.time(), jid))
        self.audit("job.done", job_id=jid, bot_id=(result or {}).get("bot_id"), actor=actor,
                   summary={k: result.get(k) for k in ("bot_id", "name", "pass", "total", "status", "verified", "benchmarked", "healthy", "changed", "added") if k in result})

    def fail(self, jid: str, error: str, actor: str) -> dict:
        """Classify, then retry / defer / pause. Returns the updated job."""
        j = self.get(jid); cls = classify_failure(error); max_retries, delay = RETRY_POLICY[cls]
        if cls in ("logic", "security") or j["attempts"] > max_retries or j["attempts"] >= j["max_attempts"]:
            state = "paused" if cls in ("logic", "security") else "failed"
            self.db.execute("UPDATE jobs SET state=?,error=?,failure_class=?,lease_owner=NULL,lease_until=NULL,updated=? WHERE id=?",
                            (state, error[:4000], cls, time.time(), jid))
        else:
            state = "queued"
            self.db.execute("UPDATE jobs SET state='queued',error=?,failure_class=?,not_before=?,lease_owner=NULL,lease_until=NULL,updated=? WHERE id=?",
                            (error[:4000], cls, time.time() + delay, time.time(), jid))
        self.audit("job.failed", job_id=jid, bot_id=j["payload"].get("bot_id"), actor=actor, failure_class=cls,
                   next_state=state, attempt=j["attempts"], error=error[:600])
        return self.get(jid)

    def release(self, jid: str, actor: str = "owner", *, uncount: bool = False) -> dict:
        """Operator override: return a running job to the queue now (e.g. worker known dead)."""
        self.db.execute("UPDATE jobs SET state='queued',lease_owner=NULL,lease_until=NULL,attempts=MAX(0,attempts-?),updated=? "
                        "WHERE id=? AND state='running'", (1 if uncount else 0, time.time(), jid))
        self.audit("job.released", job_id=jid, actor=actor, uncount=uncount); return self.get(jid)

    def resume(self, jid: str, actor: str = "owner", payload_patch: dict | None = None) -> dict:
        """Re-queue a paused/failed job. `payload_patch` (D-054) is how an OWNER grants what the job lacked, e.g.
        {"allowed_permissions": [...]} — recorded in the audit so a widened allowance is never silent."""
        if payload_patch:
            j = self.get(jid)
            if j is None: raise KeyError(jid)
            new = {**j["payload"], **payload_patch}
            self.db.execute("UPDATE jobs SET payload=? WHERE id=?", (json.dumps(new), jid))
            self.audit("job.payload_patched", job_id=jid, actor=actor, patch=payload_patch)
        self.db.execute("UPDATE jobs SET state='queued',attempts=0,not_before=0,updated=? WHERE id=? AND state IN ('paused','failed')",
                        (time.time(), jid))
        self.audit("job.resumed", job_id=jid, actor=actor); return self.get(jid)

    def cancel(self, jid: str, actor: str = "owner") -> dict:
        self.db.execute("UPDATE jobs SET state='cancelled',updated=? WHERE id=? AND state IN ('queued','paused','failed')", (time.time(), jid))
        self.audit("job.cancelled", job_id=jid, actor=actor); return self.get(jid)

    def summary(self) -> dict:
        return {s: n for s, n in self.db.execute("SELECT state,COUNT(*) FROM jobs GROUP BY state")}
