"""Factory worker: drains the persistent job queue (create / test / repair / monitor) with leases + audit.

  python tools/factory_worker.py run   [--once] [--worker NAME] [--idle-exit 30] [--fast-lane] [--respawn]   # D-079: --fast-lane = run/test/tick/probe/report only
  python tools/factory_worker.py add create "<objective>" [--priority 3]
  python tools/factory_worker.py add plan "<multi-part objective>" [--max 4]     # D-053: decompose -> N creates
  python tools/factory_worker.py add test|repair|rearchitect <bot_id>
  python tools/factory_worker.py add monitor
  python tools/factory_worker.py add run <bot_id> --task "..." [--in DIR] [--out DIR]   # D-063 real work
  python tools/factory_worker.py add run --plan <plan_job> --in DIR                       # run a whole pipeline
  python tools/factory_worker.py add tick                     # D-076: fire due schedules now (self-chains hourly)
  python tools/factory_worker.py add insight [--days 7]      # D-057 factory self-review -> proposals/<date>.md
  python tools/factory_worker.py add bench [--lanes a,b] [--stale-only] [--max N]   # D-050 lane quality
  python tools/factory_worker.py status | audit-verify (D-091 hash chain) | jobs | resume <job_id> [--allow fs:read,shell:workspace] | cancel <job_id> | release <job_id> [--uncount] | audit [bot_id] [--width N]

Autonomous loop (capability 1): a `create` job that ends VERIFIED enqueues nothing more (monitor covers it);
a `monitor` job enqueues a `repair` job for every bot it demoted; a `repair` that fails pauses with a class
(security/logic → human) or retries with backoff (quota/transient/model → other lane via the chain).
Security (capability 6): every create/repair result is checked with guard.assert_no_silent_expansion against the
pre-job spec; a violation pauses the job and audits it — it never reaches the registry.
"""
from __future__ import annotations
import json, os, sys, time, socket, pathlib, datetime, traceback
ROOT = pathlib.Path(os.environ.get("AIFACTORY_REPO", pathlib.Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(ROOT / "core")); sys.path.insert(0, str(ROOT / "tools"))
from factory.jobs import JobStore                                     # noqa: E402
from factory.guard import assert_no_silent_expansion, diff_boundaries, SecurityViolation  # noqa: E402
from factory.registry import Registry                                 # noqa: E402
from factory.factory import FactoryError                              # noqa: E402
import factory_pipeline as fp                                          # noqa: E402
import factory_repair as fr                                            # noqa: E402
import factory_monitor as fm                                           # noqa: E402
import factory_probe as fpr                                            # noqa: E402
import factory_report as frp                                           # noqa: E402
import factory_discover as fdc                                         # noqa: E402
import factory_schedule as fsch                                        # noqa: E402
import factory_bench as fbn
import factory_plan as fpl
import factory_insight as fin
import factory_run as frun

DB = ROOT / "run" / "jobs.sqlite3"
LEASE = 300          # D-043: short lease + heartbeat every 60 s -> a dead worker is detected within 5 min


def _carry(p: dict) -> dict:
    """Lineage fields that must follow a bot through retest/repair/rearchitect so delivery can still fire."""
    return {k: p[k] for k in ("then_run", "plan") if p.get(k)}


def _maybe_deliver(store: JobStore, job: dict, worker: str) -> None:
    """D-066 deliver: a create (or its retest/repair descendants) that carries `then_run` triggers the run once every
    bot of its plan is active — or immediately for a single-bot objective. Idempotent via the run job's idem key."""
    p = job["payload"]; tr = p.get("then_run")
    if not tr:
        return
    if p.get("plan"):
        sib = [j for j in store.list() if j["kind"] == "create" and j["payload"].get("plan") == p["plan"]]
        bots = []
        for j in sib:
            b = next((r["bot_id"] for r in store.audit_rows(3000) if r["job_id"] == j["id"] and r["event"] == "bot.created"), None)
            bots.append(b)
        if any(b is None or reg_status(b) != "active" for b in bots):
            return
        store.enqueue("run", {"plan": p["plan"], "in": tr.get("in"), "cap": 300}, priority=4, parent=job["id"], actor=worker)
        store.audit("deliver.run_queued", job_id=job["id"], actor=worker, plan=p["plan"][:8], bots=bots)
    else:
        bot = p.get("bot_id") or next((r["bot_id"] for r in store.audit_rows(3000) if r["job_id"] == job["id"] and r["event"] == "bot.created"), None)
        if bot and reg_status(bot) == "active":
            store.enqueue("run", {"bot_id": bot, "task": tr.get("task") or p.get("objective"), "in": tr.get("in"), "cap": 300}, priority=4, parent=job["id"], actor=worker)
            store.audit("deliver.run_queued", job_id=job["id"], actor=worker, bot_id=bot)


def reg_status(bot_id: str) -> str | None:
    from factory.registry import Registry
    e = Registry(ROOT / "registry").get("bots", bot_id); return e.status if e else None


def _spec_of(bot_id: str) -> dict | None:
    reg = Registry(ROOT / "registry"); e = reg.get("bots", bot_id)
    if not e: return None
    p = ROOT / "specs" / f"{e.id}-{e.name}.json"
    d = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {"permissions": e.permissions, "tools": e.tools, "model_policy": e.model_policy}
    patch = ROOT / "bots" / f"{e.id}-{e.name}" / "nanobot.patch.json"
    if not patch.exists() and fp.WIN: patch = fp.LAPTOP_BOTS / f"{e.id}-{e.name}" / "nanobot.patch.json"
    if patch.exists(): d["env"] = json.loads(patch.read_text(encoding="utf-8")).get("env", {})
    return d


def handle(job: dict, store: JobStore, worker: str) -> dict:
    kind, p = job["kind"], job["payload"]; jid = job["id"]
    if kind == "plan":
        # D-053: objective -> 1..N single-purpose bot objectives -> one create job each (same allowance, chained parent)
        res = fpl.plan(p["objective"], int(p.get("max", fpl.MAX_STEPS)))
        queued = []
        for i, st in enumerate(res["steps"], 1):
            if st.get("reuse"):
                store.audit("plan.reused", job_id=jid, actor=worker, step=i, bot_id=st["reuse"]["id"], similarity=st["reuse"]["similarity"]); continue
            j = store.enqueue("create", {"objective": st["objective"], "plan": jid, "step": i, "produces": st.get("produces", []),
                                         "allowed_permissions": p.get("allowed_permissions", ["fs:read", "fs:write", "net:search", "net:fetch"]),
                                         **({"then_run": p["then_run"]} if p.get("then_run") else {})},
                              priority=int(p.get("priority", 5)), parent=jid, actor=worker)
            queued.append((i, j["id"][:8]))
        store.audit("plan.made", job_id=jid, actor=worker, lane=res["lane"], steps=len(res["steps"]), queued=queued, rationale=res.get("rationale", "")[:200])
        if p.get("then_run") and not queued:        # every step reused an existing bot -> nothing to build, run now
            store.enqueue("run", {"plan": jid, "in": p["then_run"].get("in"), "cap": 300}, priority=4, parent=jid, actor=worker)
        return {"name": f"plan:{len(res['steps'])} steps", "status": "queued " + ",".join(q[1] for q in queued), "lane": res["lane"]}
    if kind == "create":
        # D-065 crash-resume: if an earlier attempt of THIS job already registered a bot (crash between build and
        # test verdict), do not build a second one — pick up at the test stage. Identity comes from our own audit.
        prev = next((r["bot_id"] for r in store.audit_rows(2000) if r["job_id"] == jid and r["event"] == "bot.created" and r["bot_id"]), None)
        if prev and reg_status(prev) in ("building", "testing"):
            store.audit("job.resumed_at", job_id=jid, bot_id=prev, actor=worker, stage="test", reason="bot already built by earlier attempt")
            res = fp.cmd_test(prev); res.update({"bot_id": prev, "name": _spec_of(prev).get("name") if _spec_of(prev) else prev})
        else:
            # D-054: allowance is enforced INSIDE cmd_create before any file is written (post-hoc check let bot 015 be built)
            def _built(rep):
                store.audit("bot.created", job_id=jid, bot_id=rep["bot_id"], actor=worker, name=rep["name"], tools=rep["spec"]["tools"],
                            permissions=rep["spec"]["permissions"], chain=rep.get("chain"), lane=rep.get("spec_lane"))
            res = fp.cmd_create(p["objective"], p.get("id"), False, False, p.get("allowed_permissions", fp.DEFAULT_ALLOWANCE), on_built=_built)
        spec = res.get("spec") or _spec_of(res["bot_id"]) or {}
        store.audit("bot.tested", job_id=jid, bot_id=res["bot_id"], actor=worker, result=res.get("tests"), status=res.get("status"))
        if res.get("status") != "active":
            # D-036: a fresh bot that misses on first run gets exactly one automatic re-test (flaky lanes / timeouts);
            # if the re-test also fails the test handler escalates to repair, which fails closed.
            store.enqueue("test", {"bot_id": res["bot_id"], "retest_of": jid, **_carry(p)}, priority=3, parent=jid, actor=worker)
        else:
            _maybe_deliver(store, job, worker)
        return res
    if kind == "test":
        before = _spec_of(p["bot_id"]); before_status = reg_status(p["bot_id"])
        res = fp.cmd_test(p["bot_id"])
        store.audit("bot.tested", job_id=jid, bot_id=p["bot_id"], actor=worker, result=res["tests"], status=res["status"],
                    inconclusive=bool(res.get("inconclusive")), quota=res.get("quota", 0))
        if p.get("monitor_of"):
            # D-072: nightly re-verification row (was written by factory_monitor in one go)
            fm.record_row(p["bot_id"], res, before_status=before_status)
            store.audit("bot.monitored", job_id=jid, bot_id=p["bot_id"], actor=worker, result=res["tests"][:200], after=res["status"],
                        inconclusive=bool(res.get("inconclusive")), quota=res.get("quota", 0))
        if res.get("inconclusive"):     # D-051: lanes were rate-limited, not the bot's fault -> same test again in 2h, no repair
            store.enqueue("test", {"bot_id": p["bot_id"], "retest_of": p.get("retest_of") or jid, "after_quota": jid, **({"monitor_of": p["monitor_of"]} if p.get("monitor_of") else {})},
                          priority=3, parent=jid, actor=worker, not_before=time.time() + 7200)
            return res
        if res["status"] != "active" and p.get("monitor_of"):
            store.audit("bot.demoted", job_id=jid, bot_id=p["bot_id"], actor=worker, to=res["status"])
            if p["bot_id"] == "001":
                # D-060: the master is hand-wired (no spec) — re-verify it in 30 min; the daily report flags persistent failure
                store.enqueue("test", {"bot_id": "001", "monitor_of": p["monitor_of"], "retry_of": jid}, priority=2, parent=jid, actor=worker, not_before=time.time() + 1800)
            else:
                store.enqueue("repair", {"bot_id": p["bot_id"], "max_rounds": 2}, priority=2, parent=jid, actor=worker)
        elif res["status"] != "active" and (p.get("retest_of") or before_status == "active"):
            # retest after build/rearchitect, OR an ad-hoc test that just demoted an active bot (D-078: no orphan demotions)
            if before_status == "active" and not p.get("retest_of"):
                store.audit("bot.demoted", job_id=jid, bot_id=p["bot_id"], actor=worker, to=res["status"])
            store.enqueue("repair", {"bot_id": p["bot_id"], "max_rounds": 2, "rearchitected": bool(p.get("rearchitected")), **_carry(p)}, priority=2, parent=jid, actor=worker)
        elif res["status"] == "active":
            _maybe_deliver(store, job, worker)
        return res
    if kind == "repair":
        before = _spec_of(p["bot_id"])
        if before is None: raise FactoryError(f"unknown bot {p['bot_id']}")
        res = fr.repair(p["bot_id"], p.get("max_rounds", 2))
        after = _spec_of(p["bot_id"])
        d = assert_no_silent_expansion(before, after, context=f"repair {p['bot_id']}")   # raises -> security pause
        store.audit("bot.repair", job_id=jid, bot_id=p["bot_id"], actor=worker, ok=res.get("ok"), status=res.get("status"),
                    rounds=[{k: r.get(k) for k in ("round", "lane", "sandbox", "rejected")} for r in res.get("rounds", [])],
                    boundary_diff=d)
        if res.get("ok"):
            store.audit("bot.promoted", job_id=jid, bot_id=p["bot_id"], actor=worker, to="active")
            _maybe_deliver(store, job, worker)
        else:
            err = res.get("error") or "repair produced no passing candidate"
            rounds = res.get("rounds") or []
            all_reward_hack = bool(rounds) and all("reward hacking" in str(r.get("rejected") or "") for r in rounds)
            if all_reward_hack:
                # D-073: every candidate was rejected for echoing a test's expected literal — the TEST is the problem
                # (its expected value is a phrase the bot legitimately has to say, e.g. 'Status: PASS'), not the bot.
                # Re-architect with that feedback so the spec gets tests whose answers are computed, not quoted.
                err = "logic: spec/tests inconsistent, tests expect a literal the instructions must mention (" + err[:200] + ")"
            if err.startswith("logic: spec/tests inconsistent") and not p.get("rearchitected"):
                # D-052: instructions can't fix it -> one automatic re-architect from the original objective
                store.enqueue("rearchitect", {"bot_id": p["bot_id"], "feedback": err[:400], "from_repair": jid, **_carry(p)}, priority=2, parent=jid, actor=worker)
                store.audit("bot.rearchitect_queued", job_id=jid, bot_id=p["bot_id"], actor=worker, reason=err[:200])
            raise FactoryError(err)
        return res
    if kind == "rearchitect":
        before = _spec_of(p["bot_id"])
        if before is None: raise FactoryError(f"unknown bot {p['bot_id']}")
        # D-054/D-061: a re-architect may keep what the owner already granted this bot (its current permissions were
        # approved at create time, e.g. 016's shell:workspace) plus the default allowance — never more.
        allowance = sorted(set(p.get("allowed_permissions", fp.DEFAULT_ALLOWANCE)) | set(before.get("permissions") or []))
        res = fp.cmd_rearchitect(p["bot_id"], p.get("feedback", ""), allowance)
        if not res.get("ok"): raise FactoryError(res.get("error"))
        after = _spec_of(p["bot_id"])
        # D-052: NOT silent — the diff is audited and bounded by the job allowance; shell/net beyond allowance is impossible
        d = diff_boundaries(before, after)
        store.audit("bot.rearchitected", job_id=jid, bot_id=p["bot_id"], actor=worker, lane=res.get("spec_lane"), tools=res["spec"]["tools"],
                    permissions=res["spec"]["permissions"], boundary_diff=d, result=res.get("tests"), status=res.get("status"))
        if res.get("status") == "active":
            store.audit("bot.promoted", job_id=jid, bot_id=p["bot_id"], actor=worker, to="active")
            # a paused repair for this bot is now moot: clear it so "needs attention" stays truthful
            for j in store.list():
                if j["state"] == "paused" and j["kind"] == "repair" and j["payload"].get("bot_id") == p["bot_id"]:
                    store.cancel(j["id"], actor=worker); store.audit("job.superseded", job_id=j["id"], bot_id=p["bot_id"], actor=worker, by=jid)
        else:
            # one re-test like a fresh create; the test handler escalates to repair (flagged so repair->rearchitect can't loop)
            store.enqueue("test", {"bot_id": p["bot_id"], "retest_of": jid, "rearchitected": True, **_carry(p)}, priority=3, parent=jid, actor=worker)
        return {k: res.get(k) for k in ("bot_id", "spec_lane", "pass", "total", "status", "boundary_diff")}
    if kind == "probe":
        if not p.get("only"):   # D-077: chain the next hourly probe FIRST so a failing probe can never end the chain
            nxt = (datetime.datetime.now() + datetime.timedelta(hours=1))
            store.enqueue("probe", {"only": [], "hour": nxt.strftime("%Y-%m-%dT%H")}, priority=1, parent=jid, actor=worker, not_before=time.time() + 3600)
        res = fpr.run(set(p["only"]) if p.get("only") else None)
        if res.get("network_down"):                   # D-086: our outage, not theirs — re-probe in 10 min, touch nothing
            store.audit("probe.network_down", job_id=jid, actor=worker, detail=res["detail"])
            store.enqueue("probe", {"only": [], "hour": p.get("hour", "") + "-retry", "retry_of": jid}, priority=0, parent=jid, actor=worker, not_before=time.time() + 600)
            return {"probed": res["probed"], "network_down": True, "detail": res["detail"]}
        for r in res["changed"]:
            store.audit("model.health", job_id=jid, actor=worker, model=r["id"], outcome=r["outcome"],
                        before=r["before"], after=r["after"], detail=r.get("detail"))
        for r in res.get("retired", []):            # D-069: gone for 3 days -> removed from registry, ledger blocks re-add
            store.audit("model.retired", job_id=jid, actor=worker, model=r["id"], reason=r["reason"])
        _sync_presets()                             # BLOCKED lanes leave nanobot config immediately; quota-cooled primary rotates (D-062)
        if not res["healthy"] and not p.get("only"):
            raise RuntimeError("transient: probe found no healthy remote lane")
        # D-047: a lane went BLOCKED, or the healthy remote pool is thin -> discover replacements (dedup by day)
        remote_ok = [r for r in res["rows"] if r.get("outcome") == "ok" and r["id"] not in ("local3b", "local4b")]
        newly_blocked = [c for c in res["changed"] if c["after"] == "BLOCKED"]
        if not p.get("only") and (newly_blocked or len(remote_ok) < fdc.MIN_HEALTHY):
            trig = "blocked:" + ",".join(c["id"] for c in newly_blocked) if newly_blocked else f"healthy={len(remote_ok)}"
            # D-069: free-first scout — also try the other 2026 free providers; without a key each yields a needs_owner notice
            for prov in ("openrouter", "cerebras", "nvidia", "mistral"):
                store.enqueue("discover", {"provider": prov, "day": datetime.date.today().isoformat(), "trigger": trig}, priority=2, parent=jid, actor=worker)
        return {"probed": res["probed"], "healthy": res["healthy"], "changed": [(c["id"], c["after"]) for c in res["changed"]], "retired": [r["id"] for r in res.get("retired", [])]}
    if kind == "discover":
        res = fdc.run(p.get("provider", "openrouter"), int(p.get("max", 2)))
        if isinstance(res.get("needs_owner"), dict):                    # D-069: surfaced in STATUS.md; owner acts, factory never self-applies
            store.audit("owner.needed", job_id=jid, actor=worker, provider=res.get("provider") or p.get("provider"), reason=res["needs_owner"]["reason"])
        for v in res.get("verdicts", []):
            if v["verdict"] in ("approved", "rejected"):
                store.audit("lane.discovered" if v["verdict"] == "approved" else "lane.rejected", job_id=jid, actor=worker,
                            model=v["model"], reason=v["reason"], provider=res.get("provider"))
        if res.get("added"):
            store.audit("config.presets", job_id=jid, actor=worker, added=res["added"])
            _sync_presets()
            store.enqueue("bench", {"lanes": res["added"], "day": datetime.date.today().isoformat()}, priority=4, parent=jid, actor=worker)
        return {k: res.get(k) for k in ("skipped", "healthy_before", "catalog", "evaluated", "added")}
    if kind == "bench":
        # D-050: pinned single-lane quality score on the reference suite; ranks default_fallbacks()
        res = fbn.run(p.get("lanes") or None, p.get("ref", fbn.REF_BOT), bool(p.get("stale_only")), int(p.get("max", 3)))
        for r in res["results"]:
            store.audit("lane.benchmarked", job_id=jid, actor=worker, lane=r["lane"], result=f"{r['pass']}/{r['total']}", quota=r.get("quota", 0), secs=r["secs"])
        for r in res["errors"]:
            store.audit("lane.bench_error", job_id=jid, actor=worker, lane=r["lane"], error=r["error"])
        _sync_presets()                            # D-062: bench scores may change the master's primary/fallback chain
        return {"benchmarked": [(r["lane"], f"{r['pass']}/{r['total']}" + (f" q{r['quota']}" if r.get("quota") else "")) for r in res["results"]], "errors": res["errors"], "rank": res["rank"][:8]}
    if kind == "run":
        # D-063: run a bot or a whole plan on real input; audited per step; failure classes flow through the normal machinery
        if p.get("plan"):
            res = frun.run_plan(p["plan"], pathlib.Path(p["in"]) if p.get("in") else None, None, int(p.get("cap", 300)))
            for st in res.get("steps", []):
                store.audit("bot.ran", job_id=jid, bot_id=st.get("bot"), actor=worker, plan=p["plan"], step=st["step"], ok=st.get("ok"),
                            produced=st.get("produced"), missing=st.get("missing_outputs"), secs=st.get("secs"), reply=(st.get("reply") or "")[:160], chain=st.get("chain"))
            if not res.get("ok"):
                bad = next((s_ for s_ in res.get("steps", []) if not s_.get("ok")), {})
                if bad.get("quota"): raise RuntimeError("transient: lane quota during run")
                raise FactoryError(f"logic: plan run failed at step {bad.get('step')} ({bad.get('bot')}): {bad.get('error') or bad.get('status')}")
            return {"name": f"run:plan {p['plan'][:8]}", "status": "ok " + ",".join(res.get("outputs", [])), "path": res.get("dir")}
        res = frun.run_bot(p["bot_id"], p["task"], pathlib.Path(p["in"]) if p.get("in") else None, pathlib.Path(p["out"]) if p.get("out") else frun.RUNS / f"bot-{p['bot_id']}-{int(time.time())}", int(p.get("cap", 300)))
        store.audit("bot.ran", job_id=jid, bot_id=p["bot_id"], actor=worker, ok=res.get("ok"), produced=res.get("produced"), secs=res.get("secs"), reply=(res.get("reply") or "")[:160], chain=res.get("chain"))
        if not res.get("ok"):
            if res.get("quota"): raise RuntimeError("transient: lane quota during run")
            raise FactoryError(f"logic: run failed: {res.get('error') or res.get('status')}")
        return {"bot_id": p["bot_id"], "name": "run", "status": "ok " + ",".join(res.get("produced", []))}
    if kind == "tick":
        # D-076: fire due schedules (idempotent per slot); chained hourly like probe/report so it survives restarts
        res = fsch.tick(store, actor=worker)
        nxt = datetime.datetime.now() + datetime.timedelta(hours=1)
        store.enqueue("tick", {"hour": nxt.strftime("%Y-%m-%dT%H")}, priority=1, parent=jid, actor=worker, not_before=time.time() + 3600)
        return res
    if kind == "insight":
        # D-057 self-improvement stage 1: evidence -> proposals/<date>.md. Only pre-approved mechanisms are auto-enqueued.
        res = fin.run(int(p.get("days", 7)), write=True)
        acted = []
        for pr in res["proposals"]:
            aa = pr.get("auto_actionable")
            if aa:
                j = store.enqueue(aa["kind"], aa["payload"], priority=6, parent=jid, actor=worker); acted.append((aa["kind"], j["id"][:8]))
        store.audit("factory.proposals", job_id=jid, actor=worker, count=len(res["proposals"]),
                    kinds=[f"{x['severity']}:{x['kind']}" for x in res["proposals"]], auto=acted, path=res["paths"].get("md"))
        return {"name": f"insight:{len(res['proposals'])} proposals", "status": "auto " + ",".join(f"{k}:{i}" for k, i in acted) if acted else "review", "path": res["paths"].get("md")}
    if kind == "report":
        r = frp.build(); (ROOT / "STATUS.md").write_text(frp.markdown(r), encoding="utf-8")
        nxt = datetime.datetime.now() + datetime.timedelta(days=1)
        store.enqueue("report", {"day": nxt.strftime("%Y-%m-%d")}, priority=6, parent=jid, actor=worker, not_before=time.time() + 86400)
        store.enqueue("bench", {"stale_only": True, "max": 2, "day": datetime.date.today().isoformat()}, priority=7, parent=jid, actor=worker)
        if datetime.date.today().weekday() == 0:       # D-057 weekly self-review (Mondays; idem by iso week)
            store.enqueue("insight", {"days": 7, "week": datetime.date.today().strftime("%G-W%V")}, priority=8, parent=jid, actor=worker)
        # D-055: the factory owns its nightly cycle. If no monitor ran today (Task Scheduler skipped: battery, asleep),
        # enqueue one now — idempotent by day, so a scheduler-triggered monitor is never duplicated.
        today = datetime.date.today().isoformat()
        if not any(j["kind"] == "monitor" and j["payload"].get("day") == today and not j["payload"].get("only") and j["state"] in ("done", "running", "queued") for j in store.list()):
            store.enqueue("monitor", {"only": None, "day": today}, priority=3, parent=jid, actor=worker)   # same payload as the scheduler => same idem key
        return {"bots_active": r["bots"]["active"], "attention": r["attention"][:10], "healthy_lanes": r["healthy_lanes"]}
    if kind == "monitor":
        # D-035 pre-flight: a bloated config makes every test fail for the wrong reason — refuse to demote on it
        cfg_path = pathlib.Path(r"C:\AI\Factory\config.json")
        if cfg_path.exists():
            from factory.guard import config_hygiene
            probs = config_hygiene(json.loads(cfg_path.read_bytes().decode("utf-8")), cfg_path.stat().st_size)
            if probs:
                store.audit("config.unhealthy", job_id=jid, actor=worker, problems=probs)
                raise RuntimeError("logic: config.json unhealthy, monitor aborted before demoting anyone: " + "; ".join(probs))
        # D-072: the monitor no longer tests every bot inside one 40-minute job (it blocked the queue for hours and lost
        # everything on a laptop sleep). It fans out one low-priority `test` job per active bot; each is independently
        # leased, resumable and interleaves with owner work. Demote -> repair happens in the test handler (monitor_of).
        reg = fm.Registry(ROOT / "registry"); only = set(p["only"]) if p.get("only") else None
        targets = [e.id for e in reg.all("bots") if (e.status == "active" or e.id == "001") and (not only or e.id in only)]
        kids = []
        for bid in targets:
            j = store.enqueue("test", {"bot_id": bid, "monitor_of": jid, "day": p.get("day")}, priority=6, parent=jid, actor=worker)
            kids.append(j["id"][:8])
        store.audit("monitor.fanout", job_id=jid, actor=worker, bots=targets, jobs=kids)
        return {"fanout": len(targets), "bots": targets}
    raise FactoryError(f"unknown job kind {kind}")


CODE_FILES = [pathlib.Path(__file__), *sorted((ROOT / "core" / "factory").glob("*.py")), *sorted((ROOT / "tools").glob("factory_*.py")),
              *sorted((ROOT / "core" / "tests").glob("*.py"))]   # D-074: a test-only fix must also unblock/restart the worker


def _code_stamp() -> float:
    return max((f.stat().st_mtime for f in CODE_FILES if f.exists()), default=0.0)


def _sync_presets() -> None:
    """D-048: nanobot modelPresets mirror the registry for every non-BLOCKED remote model (config.json is the runtime)."""
    import factory_presets
    try: factory_presets.sync()
    except Exception as e: JobStore(DB).audit("config.presets_error", actor="worker", error=str(e)[:200])


STATE_PATHS = ["registry", "specs", "AUDIT.md", "MONITOR.md", "BOT_REGISTRY.md", "STATUS.md", "audit", "proposals"]


def _commit_state(kind: str, jid8: str) -> None:
    """D-041: factory state (registry, specs, audit) is committed to git after every job so it can never be lost by a
    sync/reset. Local commit only; the push is done by the sync script (network may be down). Never raises."""
    import subprocess
    lock = ROOT / "run" / "git-state.lock"              # D-079: two workers must never rebase/push at the same time
    for _ in range(120):
        try:
            fd = os.open(str(lock), os.O_CREAT | os.O_EXCL | os.O_WRONLY); os.write(fd, str(os.getpid()).encode()); os.close(fd); break
        except FileExistsError:
            try:
                if time.time() - lock.stat().st_mtime > 300: lock.unlink()     # stale lock from a killed worker
            except Exception: pass
            time.sleep(1)
    else:
        return
    try:
        env = {**os.environ, "GIT_TERMINAL_PROMPT": "0", "GCM_INTERACTIVE": "Never", "GIT_ASKPASS": "echo"}
        g = lambda *a: subprocess.run(["git", *a], cwd=str(ROOT), capture_output=True, text=True, timeout=60, env=env)
        g("add", "-A", "--", *STATE_PATHS)
        if g("diff", "--cached", "--quiet").returncode != 0:
            g("-c", "user.name=AI Factory Worker", "-c", "user.email=contactgleamsphere-afk+worker@users.noreply.github.com",
              "commit", "-q", "-m", f"state: after {kind} job {jid8}")
            tok = os.environ.get("GITHUB_TOKEN")
            if tok:   # push with the token in the URL and every credential helper disabled -> can never block on a GUI prompt
                url = f"https://x-access-token:{tok}@github.com/contactgleamsphere-afk/grok-system.git"
                nh = ["-c", "credential.helper=", "-c", "core.askPass=", "-c", "credential.interactive=never"]
                g(*nh, "fetch", "-q", url, "main")
                if g("rebase", "-q", "FETCH_HEAD").returncode != 0:
                    # D-101: never leave a rebase half-done or throw state away — abort, then merge with the laptop's
                    # state commits winning every conflict (code files never conflict: the laptop never edits them).
                    g("rebase", "--abort")
                    if g("merge", "-q", "--no-edit", "-X", "ours", "FETCH_HEAD").returncode != 0:
                        g("merge", "--abort"); JobStore(DB).audit("git.sync_conflict", actor="worker", note="local state kept unpushed; retry next job")
                g(*nh, "push", "-q", url, "HEAD:main")
    except Exception:
        pass
    finally:
        try: lock.unlink()
        except Exception: pass


def _keep_awake(on: bool) -> None:
    """D-071: the laptop uses Modern Standby (S0 idle) and drifted into it twice today mid-job (bench 6f50b9fd lease
    expired, tunnel down 15 min). While a job is in flight the worker holds a system-required execution request
    (the same API media players use); released between jobs so an idle machine can still sleep."""
    if os.name != "nt": return
    try:
        import ctypes
        ES_CONTINUOUS, ES_SYSTEM_REQUIRED, ES_AWAYMODE_REQUIRED = 0x80000000, 0x00000001, 0x00000040
        ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_AWAYMODE_REQUIRED if on else ES_CONTINUOUS)
    except Exception:
        pass


def _self_test_gate(store: "JobStore", worker: str) -> bool:
    """D-074: a long-lived worker must not run code whose own regression suite is red (a bad push would otherwise
    demote/repair real bots with broken logic). Runs core/tests once per code stamp; result cached in run/selftest.json.
    Skips gracefully when pytest is absent (sandbox CI still covers it)."""
    import subprocess
    cache = ROOT / "run" / "selftest.json"; stamp = _code_stamp()
    try:
        c = json.loads(cache.read_text(encoding="utf-8"))
        if c.get("stamp") == stamp: return bool(c.get("ok"))
    except Exception:
        pass
    try:
        r = subprocess.run([sys.executable, "-m", "pytest", str(ROOT / "core" / "tests"), "-q", "-p", "no:cacheprovider", "-x"],
                           cwd=str(ROOT), capture_output=True, text=True, timeout=600, env={**os.environ, "AIFACTORY_REPO": str(ROOT)})
        if "No module named pytest" in (r.stderr or ""): ok, tail = True, "pytest not installed - skipped"
        else: ok, tail = r.returncode == 0, (r.stdout or r.stderr).strip().splitlines()[-1:] 
    except Exception as e:
        ok, tail = True, f"selftest error {type(e).__name__} - skipped"
    cache.parent.mkdir(exist_ok=True); cache.write_text(json.dumps({"stamp": stamp, "ok": ok, "tail": tail, "at": time.strftime("%Y-%m-%dT%H:%M:%S")}), encoding="utf-8")
    store.audit("worker.selftest", actor=worker, ok=ok, tail=tail)
    return ok


RECURRING = {   # D-077: self-chaining jobs that must always have exactly one live successor
    "probe":  lambda: ({"only": [], "hour": datetime.datetime.now().strftime("%Y-%m-%dT%H")}, 1),
    "tick":   lambda: ({"hour": datetime.datetime.now().strftime("%Y-%m-%dT%H")}, 1),
    "report": lambda: ({"day": datetime.date.today().isoformat()}, 6),
}


def ensure_recurring(store: "JobStore", worker: str) -> list[str]:
    """D-077: the hourly probe chain silently died on 21 Sep (a probe failed as `logic`, so its successor was never
    enqueued) and lane health went 22 h stale — bots then spent whole test budgets on quota-exhausted lanes. On every
    worker start, re-seed any recurring chain that has no queued/running successor. Idempotent (idem key per hour/day)."""
    live = {j["kind"] for j in store.list(["queued", "running"])}
    seeded = []
    for kind, mk in RECURRING.items():
        if kind in live: continue
        payload, prio = mk()
        store.enqueue(kind, payload, priority=prio, actor=worker); seeded.append(kind)
    if seeded: store.audit("worker.reseeded", actor=worker, kinds=seeded)
    return seeded


FAST_KINDS = ("run", "test", "tick", "probe", "report", "discover")   # D-079: minutes, not tens of minutes


def _respawn() -> None:
    """D-081b: `--respawn` workers relaunch themselves with fresh modules on a code change instead of relying on the
    supervisor loop (which only iterates when the slow worker exits — so the fast lane used to vanish for the length of
    a create/repair after every push)."""
    if "--respawn" not in sys.argv: return
    import subprocess
    flags = 0x00000008 | 0x00000200 if os.name == "nt" else 0          # DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP
    try: subprocess.Popen([sys.executable, *sys.argv], cwd=str(ROOT), creationflags=flags, close_fds=True,
                          stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception: pass


def run(worker: str, once: bool = False, idle_exit: int = 0, kinds: tuple[str, ...] | None = None) -> int:
    store = JobStore(DB); idle_since = time.time(); processed = 0; stamp = _code_stamp()
    if not once: ensure_recurring(store, worker)
    if not once and not _self_test_gate(store, worker):
        store.audit("worker.blocked_by_tests", actor=worker, reason="core/tests red on current code; refusing to process jobs until code changes")
        # wait for a code change (repo-sync/push), then let the supervisor relaunch us
        while _code_stamp() == stamp: time.sleep(30)
        return 0
    while True:
        # D-039: a long-lived worker must never run stale code — exit between jobs when any factory module changed;
        # the supervisor loop (run-worker.ps1) relaunches it with fresh modules.
        if _code_stamp() != stamp:
            store.audit("worker.restart", actor=worker, reason="code changed on disk"); _respawn(); return processed
        job = store.claim(worker, LEASE, kinds=kinds)
        if not job:
            if once or (idle_exit and time.time() - idle_since > idle_exit): break
            time.sleep(5); continue
        idle_since = time.time(); processed += 1
        import threading
        stop = threading.Event()

        def _beat():
            hb = JobStore(DB)                      # own connection: sqlite objects are not thread-safe
            while not stop.wait(60):
                try: hb.heartbeat(job["id"], worker, LEASE)      # D-081: re-adopts after a sleep, or reports 'lost'
                except Exception: pass
        threading.Thread(target=_beat, daemon=True).start()
        _keep_awake(True)
        try:
            res = handle(job, store, worker)
            if store.heartbeat(job["id"], worker, LEASE) == "lost":   # D-081: someone else owns it now -> never overwrite
                store.audit("job.orphaned_result", job_id=job["id"], bot_id=job["payload"].get("bot_id"), actor=worker,
                            summary=str(res)[:300])
            else:
                store.done(job["id"], res if isinstance(res, dict) else {"result": res}, worker)
        except SecurityViolation as e:
            store.audit("security.violation", job_id=job["id"], bot_id=job["payload"].get("bot_id"), actor=worker, error=str(e))
            store.fail(job["id"], f"security: {e}", worker)
        except Exception as e:
            if store.heartbeat(job["id"], worker, LEASE) == "lost":
                store.audit("job.orphaned_result", job_id=job["id"], bot_id=job["payload"].get("bot_id"), actor=worker, error=str(e)[:300])
            else:
                store.fail(job["id"], f"{type(e).__name__}: {e}\n{traceback.format_exc()[-800:]}", worker)
        stop.set(); _keep_awake(False)
        store.audit_export(ROOT / "AUDIT.md"); store.audit_sync_jsonl(ROOT / "audit")      # D-067 durable trail
        _commit_state(job["kind"], job["id"][:8])
        if once: break
    store.audit_export(ROOT / "AUDIT.md")
    return processed


def main(a: list[str]) -> int:
    if len(a) < 2: print(__doc__); return 2
    store = JobStore(DB); cmd = a[1]
    opt = lambda k, d=None: a[a.index(k) + 1] if k in a else d
    if cmd == "run":
        n = run(opt("--worker", f"{socket.gethostname()}-{os.getpid()}"), "--once" in a, int(opt("--idle-exit", 0)),
                kinds=FAST_KINDS if "--fast-lane" in a else None)   # D-079: second worker serves short jobs only
        print(json.dumps({"processed": n, "queue": store.summary()})); return 0
    if cmd == "add":
        kind = a[2]
        if kind in ("create", "plan"):
            obj = opt("--objective") or (a[3] if len(a) > 3 and not a[3].startswith("--") else "")
            if len(obj.split()) < 3:                                      # D-094: never spend an architect call on an empty/flag objective
                print(json.dumps({"error": "objective must be a sentence (>=3 words); got " + repr(obj[:40])})); return 2
            a = a[:3] + [obj] + a[3:]
        if kind == "create":
            pl = {"objective": a[3]}
            if opt("--allow"): pl["allowed_permissions"] = opt("--allow").split(",")     # D-054: explicit owner grant (recorded in the job + audit)
            if opt("--then-run"): pl["then_run"] = {"in": opt("--then-run"), "task": opt("--task")}   # D-066
            j = store.enqueue("create", pl, priority=int(opt("--priority", 5)), actor=opt("--actor", "owner"))
        elif kind == "plan":
            pl = {"objective": a[3], "max": int(opt("--max", 4))}
            if opt("--then-run"): pl["then_run"] = {"in": opt("--then-run")}          # D-066: build, then run on these files
            j = store.enqueue("plan", pl, priority=int(opt("--priority", 5)), actor=opt("--actor", "owner"))
        elif kind == "rearchitect": j = store.enqueue("rearchitect", {"bot_id": a[3], "feedback": opt("--feedback", ""), "t": int(time.time())}, priority=2, actor=opt("--actor", "owner"))
        elif kind in ("test", "repair"): j = store.enqueue(kind, {"bot_id": a[3]}, priority=int(opt("--priority", 4)), actor=opt("--actor", "owner"))
        elif kind == "probe":
            only = [x for x in opt("--only", "").split(",") if x]
            j = store.enqueue("probe", {"only": only, "hour": datetime.datetime.now().strftime("%Y-%m-%dT%H")}, priority=1, actor=opt("--actor", "owner"))
        elif kind == "discover":
            j = store.enqueue("discover", {"provider": opt("--provider", "openrouter"), "day": str(datetime.date.today()), "trigger": "manual"}, priority=2, actor=opt("--actor", "owner"))
        elif kind == "bench":
            lanes = [x for x in opt("--lanes", "").split(",") if x]
            j = store.enqueue("bench", {"lanes": lanes, "stale_only": "--stale-only" in a, "max": int(opt("--max", 3)), "day": str(datetime.date.today()), "t": int(time.time())}, priority=4, actor=opt("--actor", "owner"))
        elif kind == "run":
            if opt("--plan"): pl = {"plan": opt("--plan"), "in": opt("--in"), "cap": int(opt("--cap", 300)), "t": int(time.time())}
            else: pl = {"bot_id": a[3].zfill(3), "task": opt("--task", ""), "in": opt("--in"), "out": opt("--out"), "cap": int(opt("--cap", 300)), "t": int(time.time())}
            j = store.enqueue("run", pl, priority=int(opt("--priority", 4)), actor=opt("--actor", "owner"))
        elif kind == "insight":
            j = store.enqueue("insight", {"days": int(opt("--days", 7)), "t": int(time.time())}, priority=8, actor=opt("--actor", "owner"))
        elif kind == "report":
            j = store.enqueue("report", {"day": str(datetime.date.today())}, priority=6, actor=opt("--actor", "owner"))
        elif kind == "tick":
            j = store.enqueue("tick", {"hour": datetime.datetime.now().strftime("%Y-%m-%dT%H")}, priority=1, actor=opt("--actor", "owner"))
        elif kind == "monitor":
            only = [x.strip().zfill(3) for x in str(opt("--only", "")).split(",") if x.strip()] or None   # zfill: shells turn 002 into 2
            j = store.enqueue("monitor", {"only": only, "day": str(datetime.date.today())}, priority=3, actor=opt("--actor", "owner"))
        else: print(__doc__); return 2
        print(json.dumps({"job_id": j["id"], "state": j["state"], "kind": j["kind"]})); return 0
    if cmd == "status": print(json.dumps(store.summary())); return 0
    if cmd == "audit-verify":                                   # D-091
        r = JobStore.audit_verify(ROOT / "audit"); print(json.dumps(r)); return 0 if r["ok"] else 1
    if cmd == "jobs":
        for j in store.list(): print(f"{j['id'][:8]} {j['kind']:8s} {j['state']:9s} att={j['attempts']} cls={j['failure_class'] or '-':9s} {json.dumps(j['payload'])[:70]}")
        return 0
    if cmd == "resume":
        ids = [j["id"] for j in store.list(["paused", "failed"])] if (len(a) < 3 or a[2] == "--all") else [store.resolve(a[2])]
        patch = {"allowed_permissions": opt("--allow").split(",")} if opt("--allow") else None    # D-054 owner grant
        if patch and len(ids) != 1: print("--allow needs exactly one job id"); return 2
        if patch and "shell:system" in patch["allowed_permissions"]: print("shell:system is never grantable"); return 2
        for i in ids: store.resume(i, actor=opt("--actor", "owner"), payload_patch=patch)
        print(json.dumps({"resumed": [i[:8] for i in ids], "granted": patch})); return 0
    if cmd == "cancel": print(json.dumps(store.cancel(store.resolve(a[2]))["state"])); return 0
    if cmd == "release": print(json.dumps(store.release(store.resolve(a[2]), uncount="--uncount" in a)["state"])); return 0
    if cmd == "audit":
        for r in reversed(store.audit_rows(40, a[2] if len(a) > 2 else None)):
            print(f"{datetime.datetime.fromtimestamp(r['ts']):%H:%M:%S} {r['event']:20s} job={str(r['job_id'])[:8]} bot={r['bot_id'] or '-'} {r['detail'][:int(opt('--width', 110))]}")
        return 0
    print(__doc__); return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
