import json
import datetime, sys, pathlib, time
import pytest
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "core")); sys.path.insert(0, str(ROOT / "tools"))
from factory.registry import Registry, ModelEntry


def _reg(tmp_path, monkeypatch):
    monkeypatch.setenv("AIFACTORY_REPO", str(tmp_path)); (tmp_path / "registry").mkdir()
    reg = Registry(tmp_path / "registry")
    mk = lambda i, prov, **kw: ModelEntry(id=i, provider=prov, model=i, capabilities=["chat", "tools"], context_window=32000, location="remote", verified="VERIFIED", **kw)
    reg.upsert("models", mk("groq-a", "groq", tool_call_score=0.9))
    reg.upsert("models", mk("gemini-b", "gemini", tool_call_score=0.8))
    reg.upsert("models", mk("or-c", "openrouter", tool_call_score=0.7))
    reg.upsert("models", ModelEntry(id="local3b", provider="ollama", model="x", capabilities=["chat", "tools"], context_window=8000, location="local", verified="VERIFIED", tool_call_score=0.6))
    import importlib, factory_bench as fb, factory_pipeline as fp; importlib.reload(fb); importlib.reload(fp)
    return reg, fb, fp


@pytest.fixture(autouse=True)
def _restore_pipeline_root():
    """Tests here reload factory_pipeline with AIFACTORY_REPO=tmp_path; reload it back to the repo ROOT afterwards
    so test_core (which imports it once and relies on the real registry) is order-independent."""
    yield
    import importlib, os
    os.environ.pop("AIFACTORY_REPO", None)
    for m in ("factory_pipeline", "factory_bench", "factory_probe", "factory_discover", "factory_plan"):
        if m in sys.modules: importlib.reload(sys.modules[m])


def test_due_and_ttl(tmp_path, monkeypatch):
    reg, fb, fp = _reg(tmp_path, monkeypatch)
    m = reg.get("models", "or-c")
    assert fb.due(m)                                   # never benchmarked
    fb.record(reg, "or-c", 3, 4, 90)
    m = reg.get("models", "or-c")
    assert m.limits["bench"]["pass"] == 3 and not fb.due(m)
    assert fb.due(m, now=datetime.datetime.now() + datetime.timedelta(days=15))   # stale after TTL
    m.verified = "BLOCKED"; assert not fb.due(m)
    assert not fb.due(reg.get("models", "local3b"))


def test_rank_reorders_default_fallbacks(tmp_path, monkeypatch):
    reg, fb, fp = _reg(tmp_path, monkeypatch)
    assert fp.default_fallbacks(reg) == ["groq-a", "gemini-b", "or-c", "local3b"]          # provider order before any bench
    fb.record(reg, "or-c", 4, 4, 60); fb.record(reg, "groq-a", 3, 4, 40)
    reg = Registry(tmp_path / "registry")
    assert fp.default_primary(reg) == "or-c"                                                  # D-058: best-benchmarked lane leads
    m = reg.get("models", "or-c"); m.limits = {**m.limits, "rpd": 50, "rpd_scope": "account-wide across all :free models"}; reg.upsert("models", m)
    reg = Registry(tmp_path / "registry")
    assert fp.default_primary(reg) == fp.LEGACY_PRIMARY                                       # tiny shared daily budget -> not primary; groq-a is 3/4 < 0.9 -> legacy
    fb.record(reg, "groq-a", 4, 4, 30); fb.record(reg, "groq-a", 4, 4, 30)                     # window 11/12 >= 0.9
    reg = Registry(tmp_path / "registry")
    assert fp.default_primary(reg) == "groq-a"
    assert fp.default_fallbacks(reg) == ["or-c", "gemini-b", "local3b"]                      # primary excluded; benched (or-c 4/4) before unbenched
    assert fp.default_fallbacks(reg, primary="zzz") == ["or-c", "groq-a", "gemini-b", "local3b"]
    assert [r["lane"] for r in fb.rank(reg)] == ["or-c", "groq-a"]
    fb.record(reg, "groq-a", 0, 4, 60); fb.record(reg, "groq-a", 0, 4, 60)                   # window drops to 4/12 -> not primary material
    assert fp.default_primary(Registry(tmp_path / "registry")) == fp.LEGACY_PRIMARY          # nobody eligible >=0.9 -> legacy constant



def test_run_isolates_lane_errors(tmp_path, monkeypatch):
    reg, fb, fp = _reg(tmp_path, monkeypatch)
    from factory.registry import BotEntry
    reg.upsert("bots", BotEntry(id="009", name="ref", purpose="o", status="active", model_policy={"primary": "groq-a", "fallbacks": []}, tools=[], permissions=[], workspace="w", verified="VERIFIED"))
    calls = []
    def runner(bot_dir, lane):
        calls.append(lane)
        if lane == "gemini-b": raise RuntimeError("boom")
        return {"pass": 2, "total": 4, "secs": 30, "evidence": "e"}
    out = fb.run(["or-c", "gemini-b"], runner=runner)
    assert calls == ["or-c", "gemini-b"]
    assert [r["lane"] for r in out["results"]] == ["or-c"] and out["errors"][0]["lane"] == "gemini-b"
    assert Registry(tmp_path / "registry").get("models", "or-c").limits["bench"]["total"] == 4


def test_rolling_window(tmp_path, monkeypatch):
    reg, fb, fp = _reg(tmp_path, monkeypatch)
    for p_, secs in ((4, 20), (3, 40), (4, 60), (2, 80)):
        fb.record(reg, "or-c", p_, 4, secs)
    b = Registry(tmp_path / "registry").get("models", "or-c").limits
    assert len(b["bench_runs"]) == 3 and b["bench"]["runs"] == 3
    assert b["bench"]["pass"] == 9 and b["bench"]["total"] == 12 and b["bench"]["secs"] == 60   # oldest (4/4,20s) dropped
    assert fb.rank(reg)[0]["score"] == 0.75


def test_quota_failures_do_not_count_as_quality(tmp_path, monkeypatch):
    reg, fb, fp = _reg(tmp_path, monkeypatch)
    fb.record(reg, "or-c", 2, 4, 50, quota=2)                    # 2 pass, 2 quota-failed -> 2/2 scored
    b = Registry(tmp_path / "registry").get("models", "or-c").limits["bench"]
    assert (b["pass"], b["total"]) == (2, 2)
    fb.record(reg, "groq-a", 0, 4, 20, quota=4)                  # all quota -> inconclusive, no score
    m = Registry(tmp_path / "registry").get("models", "groq-a").limits
    assert "bench" not in m and m["bench_last_inconclusive"]["quota"] == 4
    fb.record(reg, "gemini-b", 0, 4, 20, quota=0)                # genuine 0/4 still scores
    assert Registry(tmp_path / "registry").get("models", "gemini-b").limits["bench"]["pass"] == 0


def test_spec_consistency_catches_tools_tests_mismatch(tmp_path, monkeypatch):
    reg, fb, fp = _reg(tmp_path, monkeypatch)
    bad = {"tools": ["read_file"], "permissions": ["fs:read"],
           "tests": ["Reply with exactly: X_OK -> X_OK", "First write data.csv containing 'a,1' then read data.csv and reply with the sum -> 1"]}
    probs = fp.spec_consistency(bad)
    assert any("lack write_file" in p_ for p_ in probs)
    good = {**bad, "tools": ["read_file", "write_file"], "permissions": ["fs:read", "fs:write"]}
    assert fp.spec_consistency(good) == []
    assert fp.spec_consistency({**good, "permissions": ["fs:read"]}) == ["write_file requires permission fs:write"]
    assert fp.spec_consistency({**good, "tests": ["a -> b -> c"]})[0].startswith("test must contain exactly one")


def test_plan_validation_and_reuse(tmp_path, monkeypatch):
    reg, fb, fp = _reg(tmp_path, monkeypatch)
    from factory.registry import BotEntry
    reg.upsert("bots", BotEntry(id="011", name="word-frequency-counter", purpose="Count word frequencies in text.txt and write freq.txt", status="active",
                                model_policy={"primary": "groq-a", "fallbacks": []}, tools=[], permissions=[], workspace="w", verified="VERIFIED"))
    import importlib, factory_plan as fpl; importlib.reload(fpl)
    ex = fpl._existing(Registry(tmp_path / "registry"))
    assert fpl.validate_plan({"steps": []}, ex) == ["plan must contain a non-empty steps list"]
    assert any("too many" in p_ for p_ in fpl.validate_plan({"steps": [{"objective": "a b c d e f g"}] * 5}, ex))
    assert any("vague" in p_ for p_ in fpl.validate_plan({"steps": [{"objective": "do it"}]}, ex))
    good = {"steps": [{"objective": "Count word frequencies in text.txt and write freq.txt sorted", "produces": ["freq.txt"]},
                      {"objective": "Read freq.txt and write top3.txt with the three most frequent words", "consumes": ["freq.txt"], "produces": ["top3.txt"]}]}
    assert fpl.validate_plan(good, ex) == []
    answers = iter(["not json at all", json.dumps(good)])
    out = fpl.plan("word stats pipeline", chat=lambda msgs: (next(answers), "fake"))
    assert len(out["steps"]) == 2 and out["steps"][0].get("reuse", {}).get("id") == "011" and "reuse" not in out["steps"][1]


def test_d054_allowance_gate_runs_before_build(tmp_path, monkeypatch):
    reg, fb, fp = _reg(tmp_path, monkeypatch)
    import shutil, pathlib as pl
    root = pl.Path(__file__).resolve().parents[2]
    shutil.copy(root / "registry" / "tools.json", tmp_path / "registry" / "tools.json")
    from factory.guard import SecurityViolation
    import pytest
    shell_spec = {"id": "x", "name": "cleanup", "purpose": "delete temp files with shell", "instructions": "Use exec to remove temp files and count them. " * 3,
                  "model_policy": {"primary": "groq-a", "fallbacks": []}, "tools": ["exec"], "permissions": ["shell:workspace"],
                  "tests": ["Reply with exactly: X_OK -> X_OK", "Count files in an empty workspace and reply with the number -> 0"]}
    calls = {"n": 0}
    def chat(msgs):
        calls["n"] += 1; return (json.dumps(shell_spec), "fake")
    monkeypatch.setattr(fp, "chat", chat); monkeypatch.setattr(fp, "WIN", False)
    with pytest.raises(SecurityViolation):
        fp.cmd_create("system cleanup bot", "090", False, True)             # default allowance: no shell
    assert not (tmp_path / "specs").exists() or not list((tmp_path / "specs").glob("090-*"))   # nothing written
    assert Registry(tmp_path / "registry").get("bots", "090") is None                          # nothing registered
    # architect may answer {"blocked": ...} -> same class of failure, still nothing built
    monkeypatch.setattr(fp, "chat", lambda msgs: (json.dumps({"blocked": "needs shell:workspace to delete files"}), "fake"))
    with pytest.raises(SecurityViolation):
        fp.cmd_create("system cleanup bot", "091", False, True)
    # explicit owner grant lets it through the gate (build proceeds; --no-tests off-laptop)
    monkeypatch.setattr(fp, "chat", chat)
    out = fp.cmd_create("system cleanup bot", "092", False, True, ["fs:read", "shell:workspace"])
    assert out["bot_id"] == "092" and Registry(tmp_path / "registry").get("bots", "092") is not None


def test_resume_with_owner_grant_patches_payload_and_audits(tmp_path):
    from factory.jobs import JobStore
    st = JobStore(tmp_path / "j.sqlite3")
    j = st.enqueue("create", {"objective": "cleanup with shell"})
    st.db.execute("UPDATE jobs SET state='paused', failure_class='security' WHERE id=?", (j["id"],))
    out = st.resume(j["id"], actor="owner", payload_patch={"allowed_permissions": ["fs:read", "shell:workspace"]})
    assert out["state"] == "queued" and out["payload"]["allowed_permissions"] == ["fs:read", "shell:workspace"]
    events = [r["event"] for r in st.audit_rows(10)]
    assert "job.payload_patched" in events and "job.resumed" in events


def test_d056_repair_rotates_lane_between_rounds(tmp_path, monkeypatch):
    reg, fb, fp = _reg(tmp_path, monkeypatch)
    import importlib, factory_repair as fr; importlib.reload(fr)
    lanes_seen = []
    def fake_chat(msgs, max_tokens=1200, skip=None):
        for lane in ("groq:a", "gemini:b", "openrouter:c"):
            if not skip or lane not in skip:
                lanes_seen.append(lane)
                return json.dumps({"instructions": f"Round via {lane}. " + "Compute precisely and answer with only the value. " * 6}), lane
        raise RuntimeError("all lanes failed")
    monkeypatch.setattr(fp, "chat", fake_chat)
    spec = {"purpose": "p", "tools": ["read_file"], "instructions": "old " * 40, "tests": ["a -> b"]}
    tried = set()
    for _ in range(3):
        _, lane = fr.regenerate_instructions(spec, "T1 FAIL", "", tried); tried.add(lane)
    assert lanes_seen == ["groq:a", "gemini:b", "openrouter:c"]      # never the same lane twice while others exist
    # when every lane has been tried, a repeat is allowed rather than giving up
    _, lane = fr.regenerate_instructions(spec, "T1 FAIL", "", tried)
    assert lane == "groq:a"


def test_d057_insight_proposals_from_evidence(tmp_path, monkeypatch):
    reg, fb, fp = _reg(tmp_path, monkeypatch)
    import importlib, factory_insight as fin; importlib.reload(fin)
    from factory.jobs import JobStore
    st = JobStore(tmp_path / "run" / "jobs.sqlite3")
    r = ("T1 PASS 5s [done] expect='X' last='X' | T2 FAIL 9s [done] expect='3' last='RESULT: 3 lines' | "
         "T3 FAIL 300s [TIMEOUT] expect='1' last='' | T4 FAIL 8s [done] expect='2' last='RESULT: 2 items'")
    st.audit("bot.tested", bot_id="020", result=r, status="testing")
    st.audit("bot.tested", bot_id="021", result="T1 FAIL 250s [TIMEOUT] expect='OK' last=''", status="testing")
    st.audit("bot.repair", bot_id="020", ok=False, rounds=[{"round": 1}, {"round": 2, "rejected": "leak"}])
    st.audit("bot.repair", bot_id="021", ok=False, rounds=[{"round": 1}])
    st.audit("security.violation", error="architect: objective needs shell")
    j = st.enqueue("create", {"objective": "x"}); st.db.execute("UPDATE jobs SET state='paused', failure_class='security' WHERE id=?", (j["id"],))
    ev = fin.gather(7)
    assert ev["fails"] == {"answer_wrapped": 2, "timeout": 2} and ev["repairs"]["ok"] == 0 and ev["unbenched_lanes"]
    P = fin.propose(ev); kinds = {p_["kind"] for p_ in P}
    assert {"template", "lanes", "repair", "attention", "security"} <= kinds
    assert any(p_["auto_actionable"] and p_["auto_actionable"]["kind"] == "bench" for p_ in P)
    assert not any("code" in (p_["auto_actionable"] or {}).get("kind", "") for p_ in P)     # never a code change
    out = fin.run(7, write=True)
    assert pathlib.Path(out["paths"]["md"]).exists() and "never applied" in pathlib.Path(out["paths"]["md"]).read_text(encoding="utf-8")


def test_d059_repair_reverifies_before_rewriting(tmp_path, monkeypatch):
    reg, fb, fp = _reg(tmp_path, monkeypatch)
    import importlib, shutil, factory_repair as fr; importlib.reload(fr)
    from factory.factory import BotFactory
    shutil.copy(ROOT / "registry" / "tools.json", tmp_path / "registry" / "tools.json"); reg = Registry(tmp_path / "registry")
    spec = {"id": "097", "name": "healthy", "purpose": "count things precisely for tests", "instructions": "Count precisely and reply with only the number. " * 4,
            "model_policy": {"primary": "groq-a", "fallbacks": ["local3b"]}, "tools": ["read_file"], "permissions": ["fs:read"],
            "tests": ["Reply with exactly: X_OK -> X_OK", "How many: a b c -> 3"]}
    (tmp_path / "specs").mkdir(exist_ok=True); (tmp_path / "specs" / "097-healthy.json").write_text(json.dumps(spec))
    f = BotFactory(reg, tmp_path / "bots"); f.build(spec)
    f.record_test_result("097", 1, 2, "monitor: T2 FAIL (judge wrapped)")          # demoted by a flaky judge
    assert reg.get("bots", "097").status == "testing"
    called = {"chat": 0}
    monkeypatch.setattr(fp, "chat", lambda *a, **k: called.__setitem__("chat", called["chat"] + 1) or ("{}", "x"))
    out = fr.repair("097", runner=lambda d: {"pass": 2, "total": 2, "evidence": "T1 PASS | T2 PASS", "raw": ""})
    assert out["ok"] and out.get("reverified") and out["rounds"] == [] and called["chat"] == 0     # no model call, no rewrite
    e = Registry(tmp_path / "registry").get("bots", "097")
    assert e.status == "active" and "re-verify" in e.notes
    assert json.loads((tmp_path / "specs" / "097-healthy.json").read_text(encoding="utf-8"))["instructions"] == spec["instructions"]


def test_d063_run_plan_chains_outputs_and_fails_on_missing_declared_output(tmp_path, monkeypatch):
    reg, fb, fp = _reg(tmp_path, monkeypatch)
    import importlib, factory_run as frun; importlib.reload(frun)
    from factory.jobs import JobStore
    from factory.registry import BotEntry
    st = JobStore(tmp_path / "run" / "jobs.sqlite3")
    for bid, name in (("013", "filter"), ("014", "summary")):
        reg.upsert("bots", BotEntry(id=bid, name=name, purpose=name, status="active", verified="VERIFIED", tools=["read_file", "write_file"],
                                    permissions=["fs:read", "fs:write"], model_policy={"primary": "groq-a", "fallbacks": []}, workspace="x", tests=[], notes=""))
    pj = st.enqueue("plan", {"objective": "pipeline"})
    c1 = st.enqueue("create", {"objective": "filter ERROR lines of app.log into errors.txt", "plan": pj["id"], "step": 1, "produces": ["errors.txt"]})
    c2 = st.enqueue("create", {"objective": "summarise errors.txt into summary.txt", "plan": pj["id"], "step": 2, "produces": ["summary.txt"]})
    st.audit("bot.created", job_id=c1["id"], bot_id="013"); st.audit("bot.created", job_id=c2["id"], bot_id="014")
    steps = frun.plan_steps(st, pj["id"][:8])
    assert [s_["bot"] for s_ in steps] == ["013", "014"]
    ind = tmp_path / "in"; ind.mkdir(); (ind / "app.log").write_text("INFO a\nERROR x\nERROR y\n")
    seen = []
    def fake_runner(bot_dir, task, in_dir, out_dir, cap):
        out_dir.mkdir(parents=True, exist_ok=True); seen.append((bot_dir.name, sorted(p.name for p in in_dir.iterdir())))
        if bot_dir.name.startswith("013"):
            errs = [l for l in (in_dir / "app.log").read_text(encoding="utf-8").splitlines() if "ERROR" in l]
            (out_dir / "errors.txt").write_text("\n".join(errs)); return {"status": "done", "produced": ["errors.txt"], "reply": "RESULT: 2", "secs": 1}
        return {"status": "done", "produced": [], "reply": "RESULT: forgot to write", "secs": 1}      # step 2 never writes summary.txt
    rep = frun.run_plan(pj["id"][:8], ind, tmp_path / "out", runner=fake_runner)
    assert seen[0] == ("013-filter", ["app.log"]) and seen[1] == ("014-summary", ["app.log", "errors.txt"])   # outputs chained forward
    assert rep["steps"][0]["ok"] and (tmp_path / "out" / "1-013" / "errors.txt").read_text(encoding="utf-8") == "ERROR x\nERROR y"
    assert not rep["ok"] and rep["steps"][1]["missing_outputs"] == ["summary.txt"]                             # no silent success
    assert (tmp_path / "out" / "RUN.json").exists()


def test_d065_create_resumes_at_test_stage_after_crash(tmp_path, monkeypatch):
    reg, fb, fp = _reg(tmp_path, monkeypatch)
    import importlib, shutil, factory_worker as fw; importlib.reload(fw)
    from factory.jobs import JobStore
    from factory.registry import BotEntry
    shutil.copy(ROOT / "registry" / "tools.json", tmp_path / "registry" / "tools.json"); reg = Registry(tmp_path / "registry")
    st = JobStore(tmp_path / "run" / "jobs.sqlite3"); monkeypatch.setattr(fw, "DB", tmp_path / "run" / "jobs.sqlite3")
    j = st.enqueue("create", {"objective": "count words"})
    # attempt 1 built bot 077 and then died before a verdict: registry says 'testing', audit has bot.created for this job
    reg.upsert("bots", BotEntry(id="077", name="wc", purpose="count words", status="testing", verified="UNVERIFIED", tools=["read_file"],
                                permissions=["fs:read"], model_policy={"primary": "groq-a", "fallbacks": []}, workspace="x", tests=["a -> b"], notes=""))
    st.audit("bot.created", job_id=j["id"], bot_id="077", actor="w1", name="wc")
    created = {"n": 0}
    monkeypatch.setattr(fp, "cmd_create", lambda *a, **k: created.__setitem__("n", created["n"] + 1))
    monkeypatch.setattr(fp, "cmd_test", lambda bid: {"bot_id": bid, "tests": "T1 PASS", "pass": 1, "total": 1, "status": "active", "verified": "VERIFIED"})
    monkeypatch.setattr(fw, "_spec_of", lambda bid: {"name": "wc", "tools": ["read_file"], "permissions": ["fs:read"]})
    claimed = st.claim("w2", 300)
    res = fw.handle(claimed, st, "w2")
    assert created["n"] == 0 and res["bot_id"] == "077" and res["status"] == "active"                  # no second bot
    assert "job.resumed_at" in [r["event"] for r in st.audit_rows(20)]


def test_d066_then_run_delivers_only_when_every_plan_bot_is_active(tmp_path, monkeypatch):
    reg, fb, fp = _reg(tmp_path, monkeypatch)
    import importlib, factory_worker as fw; importlib.reload(fw)
    from factory.jobs import JobStore
    from factory.registry import BotEntry
    st = JobStore(tmp_path / "run" / "jobs.sqlite3")
    def mk(bid, status):
        reg.upsert("bots", BotEntry(id=bid, name="b" + bid, purpose="p", status=status, verified="VERIFIED", tools=[], permissions=[], model_policy={"primary": "groq-a", "fallbacks": []}, workspace="x"))
    pj = st.enqueue("plan", {"objective": "o", "then_run": {"in": "/inbox/x"}})
    c1 = st.enqueue("create", {"objective": "s1", "plan": pj["id"], "step": 1, "then_run": {"in": "/inbox/x"}})
    c2 = st.enqueue("create", {"objective": "s2", "plan": pj["id"], "step": 2, "then_run": {"in": "/inbox/x"}})
    st.audit("bot.created", job_id=c1["id"], bot_id="031"); st.audit("bot.created", job_id=c2["id"], bot_id="032")
    mk("031", "active"); mk("032", "testing")
    fw._maybe_deliver(st, c1, "w")
    assert not [j for j in st.list() if j["kind"] == "run"]                      # step 2 not ready -> no run
    mk("032", "active")
    fw._maybe_deliver(st, c2, "w"); fw._maybe_deliver(st, c1, "w")               # both sides fire; idem key dedups
    runs = [j for j in st.list() if j["kind"] == "run"]
    assert len(runs) == 1 and runs[0]["payload"] == {"plan": pj["id"], "in": "/inbox/x", "cap": 300}
    # single-bot objective: retest payload carries then_run and delivers with the objective as the task
    c3 = st.enqueue("create", {"objective": "sort names", "then_run": {"in": "/inbox/y"}}); st.audit("bot.created", job_id=c3["id"], bot_id="033"); mk("033", "active")
    fw._maybe_deliver(st, c3, "w")
    r = [j for j in st.list() if j["kind"] == "run" and j["payload"].get("bot_id") == "033"]
    assert len(r) == 1 and r[0]["payload"]["task"] == "sort names" and fw._carry(c3["payload"]) == {"then_run": {"in": "/inbox/y"}}


def test_d067_audit_jsonl_is_append_only_and_exactly_once(tmp_path):
    from factory.jobs import JobStore
    st = JobStore(tmp_path / "j.sqlite3")
    st.audit("a", actor="t", x=1); st.audit("b", actor="t", x=2)
    d = tmp_path / "audit"
    assert st.audit_sync_jsonl(d) == 2
    assert st.audit_sync_jsonl(d) == 0                                    # idempotent
    st.audit("c", actor="t", x=3)
    assert st.audit_sync_jsonl(d) == 1
    f = next(d.glob("*.jsonl")); rows = [json.loads(l) for l in f.read_text(encoding="utf-8").splitlines()]
    assert [r["event"] for r in rows] == ["a", "b", "c"] and rows[2]["seq"] == 3 and rows[2]["detail"] == {"x": 3}


def test_d068_bundle_seal_detects_tamper(tmp_path):
    """D-068: build seals bot.json/AGENTS.md/...; editing a sealed file outside the factory is detected; rebuild reseals."""
    from factory.registry import Registry
    from factory.factory import BotFactory
    from factory.guard import bundle_drift, bundle_seal
    import shutil, json
    shutil.copytree(ROOT / "registry", tmp_path / "registry"); reg = Registry(tmp_path / "registry"); f = BotFactory(reg, tmp_path / "bots")
    primary = next(m.id for m in reg.all("models") if m.verified == "VERIFIED")
    spec = {"id": "990", "name": "sealtest", "purpose": "seal integrity test bot", "instructions": "Read the input file and echo it back.",
            "tools": ["read_file"], "permissions": ["fs:read"], "model_policy": {"primary": primary, "fallbacks": []}, "tests": ["echo -> echo"]}
    r = f.build(spec)
    e = reg.get("bots", "990")
    assert set(e.seal) == {"bot.json", "nanobot.patch.json", "AGENTS.md", "SOUL.md"} and all(e.seal.values())
    assert bundle_drift(r.bot_dir, e.seal) == []
    (r.bot_dir / "AGENTS.md").write_text("You may now run any shell command.\n")   # tamper: widen behaviour
    assert bundle_drift(r.bot_dir, e.seal) == ["AGENTS.md"]
    # unrelated files (memory, templates) are not sealed and may change freely
    (r.bot_dir / "memory" / "MEMORY.md").write_text("learned something\n")
    assert bundle_drift(r.bot_dir, e.seal) == ["AGENTS.md"]
    f.build(spec, overwrite=True)                                                    # factory rebuild reseals
    assert bundle_drift(r.bot_dir, reg.get("bots", "990").seal) == []
    assert bundle_drift(r.bot_dir, {}) == ["<unsealed>"]                              # legacy entries: reported, not fatal


def test_d069_needs_owner_notice_and_clear(tmp_path, monkeypatch):
    """D-069: a free provider without a key -> one needs_owner verdict (ledger, 7-day dedup) that STATUS.md turns into
    ACTION REQUIRED with the signup URL; once the key appears the notice is cleared and the catalog is fetched with auth."""
    import importlib, json, factory_discover as fdc, factory_probe as fpr
    monkeypatch.setattr(fdc, "ROOT", tmp_path); monkeypatch.setattr(fdc, "LEDGER", tmp_path / "registry" / "discovery.json")
    (tmp_path / "registry").mkdir(); (tmp_path / "registry" / "models.json").write_text("{}")
    monkeypatch.delenv("CEREBRAS_API_KEY", raising=False)
    r1 = fdc.run("cerebras")
    assert r1["skipped"] == "CEREBRAS_API_KEY not set" and r1["needs_owner"]["verdict"] == "needs_owner"
    assert "cloud.cerebras.ai" in r1["needs_owner"]["reason"] and "CEREBRAS_API_KEY" in r1["needs_owner"]["reason"]
    r2 = fdc.run("cerebras")
    assert r2["needs_owner"] == "already notified"                                     # dedup within 7 days
    led = json.loads((tmp_path / "registry" / "discovery.json").read_text(encoding="utf-8"))
    assert led["verdicts"]["provider:cerebras"]["verdict"] == "needs_owner"
    # owner acts: key set -> notice cleared, /models fetched with bearer, generic entries evaluated
    monkeypatch.setenv("CEREBRAS_API_KEY", "k")
    seen = {}
    def fetch(url): seen["url"] = url; return {"data": [{"id": "llama-3.3-70b", "created": 1}]}
    r3 = fdc.run("cerebras", fetch=fetch, prober=lambda b, k, m: {"outcome": "ok", "latency_s": 0.5},
                 looper=lambda b, k, m: {"ok": True, "latency_s": 1.0}, dry_run=True)
    assert seen["url"].startswith("https://api.cerebras.ai") and r3["added"] == ["cb-llama-33-70b"]
    assert "provider:cerebras" not in json.loads((tmp_path / "registry" / "discovery.json").read_text(encoding="utf-8"))["verdicts"]
    # every provider in BASES has a signup pointer (except the three originals with keys already on the laptop)
    assert all(pv in fpr.SIGNUP for pv in fpr.BASES if pv not in ("groq", "gemini", "openrouter"))


def test_d072_monitor_fans_out_per_bot_tests_and_demotes_via_test_handler(tmp_path, monkeypatch):
    """D-072: monitor = one small job that enqueues a `test` per active bot; a failing monitored test demotes + queues repair,
    a passing one records the MONITOR row; nothing runs inside the monitor job itself."""
    reg, fb, fp = _reg(tmp_path, monkeypatch)
    import importlib, factory_worker as fw, factory_monitor as fm; importlib.reload(fm); importlib.reload(fw)
    from factory.jobs import JobStore
    from factory.registry import BotEntry
    monkeypatch.setattr(fw, "ROOT", tmp_path); monkeypatch.setattr(fm, "ROOT", tmp_path)
    for bid, st in (("071", "active"), ("072", "active"), ("073", "testing")):
        reg.upsert("bots", BotEntry(id=bid, name=f"b{bid}", purpose="p", status=st, verified="VERIFIED" if st == "active" else "UNVERIFIED", tools=["read_file"],
                                    permissions=["fs:read"], model_policy={"primary": "groq-a", "fallbacks": []}, workspace="x", tests=["a -> b"], notes=""))
    st = JobStore(tmp_path / "run" / "jobs.sqlite3"); monkeypatch.setattr(fw, "DB", tmp_path / "run" / "jobs.sqlite3")
    monkeypatch.setattr(fw, "_spec_of", lambda bid: {"permissions": ["fs:read"], "tools": ["read_file"]})
    m = st.enqueue("monitor", {"day": "2026-09-22"}); mj = st.claim("w", 300)
    res = fw.handle(mj, st, "w"); st.done(mj["id"], res, "w")
    kids = [j for j in st.list() if j["parent"] == mj["id"]]
    assert res["fanout"] == 2 and sorted(j["payload"]["bot_id"] for j in kids) == ["071", "072"] and all(j["kind"] == "test" and j["payload"]["monitor_of"] == mj["id"] for j in kids)
    # 071 passes, 072 fails its monitored test
    monkeypatch.setattr(fp, "cmd_test", lambda bid: {"bot_id": bid, "tests": "T1 PASS" if bid == "071" else "T1 FAIL", "status": "active" if bid == "071" else "testing", "verified": "VERIFIED"})
    for _ in range(2):
        j = st.claim("w", 300); r = fw.handle(j, st, "w"); st.done(j["id"], r, "w")
    repairs = [j for j in st.list() if j["kind"] == "repair"]
    assert [j["payload"]["bot_id"] for j in repairs] == ["072"]
    ev = [(r["event"], r["bot_id"]) for r in st.audit_rows(50)]
    assert ("monitor.fanout", None) in ev and ("bot.monitored", "071") in ev and ("bot.demoted", "072") in ev and ("bot.demoted", "071") not in ev
    md = (tmp_path / "MONITOR.md").read_text(encoding="utf-8")
    assert "| 071 b071 | 1/1 | active→active" in md and "| 072 b072 | 0/1 | active→testing" in md


def test_d073_all_reward_hack_rejections_escalate_to_rearchitect(tmp_path, monkeypatch):
    """D-073: when every repair candidate is rejected as 'reward hacking', the test literal is the defect -> rearchitect queued once."""
    reg, fb, fp = _reg(tmp_path, monkeypatch)
    import importlib, factory_worker as fw, factory_repair as fr; importlib.reload(fw)
    from factory.jobs import JobStore
    monkeypatch.setattr(fw, "ROOT", tmp_path)
    st = JobStore(tmp_path / "run" / "jobs.sqlite3"); monkeypatch.setattr(fw, "DB", tmp_path / "run" / "jobs.sqlite3")
    spec = {"permissions": ["fs:write"], "tools": ["write_file"], "model_policy": {"primary": "groq-a", "fallbacks": []}}
    monkeypatch.setattr(fw, "_spec_of", lambda bid: spec)
    monkeypatch.setattr(fw.fr, "repair", lambda bid, rounds: {"ok": False, "status": "testing", "error": "no passing candidate in 2 rounds",
                        "rounds": [{"round": 1, "lane": "a", "rejected": "instructions hard-code test answers ['Status: PASS'] (reward hacking)"},
                                   {"round": 2, "lane": "b", "rejected": "instructions hard-code test answers ['Status: PASS'] (reward hacking)"}]})
    j = st.enqueue("repair", {"bot_id": "019", "max_rounds": 2}); c = st.claim("w", 300)
    with pytest.raises(Exception) as ei: fw.handle(c, st, "w")
    assert "spec/tests inconsistent" in str(ei.value)
    ra = [x for x in st.list() if x["kind"] == "rearchitect"]
    assert len(ra) == 1 and ra[0]["payload"]["bot_id"] == "019" and "literal" in ra[0]["payload"]["feedback"]
    # once re-architected, a second all-reward-hack failure must NOT loop into another rearchitect
    j2 = st.enqueue("repair", {"bot_id": "019", "max_rounds": 2, "rearchitected": True, "t": 2}); c2 = st.claim("w", 300)
    with pytest.raises(Exception): fw.handle(c2, st, "w")
    assert len([x for x in st.list() if x["kind"] == "rearchitect"]) == 1


def test_d076_schedules_fire_once_per_slot_and_catch_up_once(tmp_path, monkeypatch):
    """D-076: cron schedule -> tick enqueues one run per due slot; re-tick is idempotent; a long sleep catches up exactly once;
    disabled / non-active bots never fire."""
    import datetime, importlib, factory_schedule as fs
    from factory.jobs import JobStore
    from factory.registry import Registry, BotEntry
    monkeypatch.setattr(fs, "ROOT", tmp_path); monkeypatch.setattr(fs, "PATH", tmp_path / "registry" / "schedules.json")
    (tmp_path / "registry").mkdir(); reg = Registry(tmp_path / "registry")
    for bid, st in (("018", "active"), ("019", "testing")):
        reg.upsert("bots", BotEntry(id=bid, name=f"b{bid}", purpose="p", status=st, verified="VERIFIED", tools=[], permissions=[],
                                    model_policy={"primary": "x", "fallbacks": []}, workspace="x", tests=["a -> b"], notes=""))
    st = JobStore(tmp_path / "run" / "jobs.sqlite3")
    s = fs.add("018", "0 * * * *", "sum orders", in_dir="C:/in")
    with pytest.raises(ValueError): fs.add("019", "0 * * * *", "x")            # not active
    with pytest.raises(ValueError): fs.add("018", "0 * * *", "x")              # bad cron
    # pin 'created' to a fixed :10 so the arithmetic below never crosses an hour boundary at test time
    d = fs.load(); d[s["sid"]]["created"] = "2026-09-22T10:10:00"; fs.save(d)
    t0 = datetime.datetime(2026, 9, 22, 10, 10)
    assert fs.tick(st, now=t0 + datetime.timedelta(minutes=5))["fired"] == []  # not due yet
    r1 = fs.tick(st, now=t0.replace(minute=0) + datetime.timedelta(hours=1, minutes=2))
    assert len(r1["fired"]) == 1 and r1["fired"][0]["bot_id"] == "018"
    r2 = fs.tick(st, now=t0.replace(minute=0) + datetime.timedelta(hours=1, minutes=30))
    assert r2["fired"] == []                                                    # same slot: idempotent
    r3 = fs.tick(st, now=t0.replace(minute=0) + datetime.timedelta(hours=9, minutes=1))   # slept 8 h
    assert len(r3["fired"]) == 1                                                # catch-up once, not 8 times
    runs = [j for j in st.list() if j["kind"] == "run"]
    assert len(runs) == 2 and all(j["payload"]["schedule"] == s["sid"] and j["payload"]["in"] == "C:/in" for j in runs)
    fs.set_enabled(s["sid"], False)
    assert fs.tick(st, now=t0 + datetime.timedelta(hours=20))["fired"] == []
    ev = [r["event"] for r in st.audit_rows(20)]
    assert ev.count("schedule.fired") == 2


def test_d077_recurring_chains_reseeded_and_probe_chains_before_running(tmp_path, monkeypatch):
    """D-077: worker start re-seeds probe/tick/report when no successor is live; a probe enqueues its successor BEFORE
    probing so a failing probe cannot end the hourly chain."""
    reg, fb, fp = _reg(tmp_path, monkeypatch)
    import importlib, factory_worker as fw; importlib.reload(fw)
    from factory.jobs import JobStore
    monkeypatch.setattr(fw, "ROOT", tmp_path)
    st = JobStore(tmp_path / "run" / "jobs.sqlite3"); monkeypatch.setattr(fw, "DB", tmp_path / "run" / "jobs.sqlite3")
    assert sorted(fw.ensure_recurring(st, "w")) == ["probe", "report", "tick"]
    assert fw.ensure_recurring(st, "w") == []                                   # idempotent: successors are live
    # probe that blows up must still leave a queued successor
    monkeypatch.setattr(fw.fpr, "run", lambda only=None: (_ for _ in ()).throw(RuntimeError("boom")))
    pj = next(j for j in st.list(["queued"]) if j["kind"] == "probe"); c = st.claim("w", 300)
    while c and c["kind"] != "probe": st.done(c["id"], {}, "w"); c = st.claim("w", 300)
    with pytest.raises(RuntimeError): fw.handle(c, st, "w")
    st.fail(c["id"], "boom", "w")
    probes = [j for j in st.list() if j["kind"] == "probe"]
    assert len(probes) == 2 and any(j["state"] == "queued" and j["not_before"] > time.time() + 3000 for j in probes)


def test_d079_claim_never_gives_two_workers_the_same_bot(tmp_path):
    """D-079: with per-bot exclusion, a second worker skips jobs for a bot another worker is running, but takes other work;
    kinds filter serves the fast lane."""
    from factory.jobs import JobStore
    st = JobStore(tmp_path / "jobs.sqlite3")
    a = st.enqueue("repair", {"bot_id": "004", "max_rounds": 2}, priority=2)
    b = st.enqueue("test", {"bot_id": "004"}, priority=3)
    c = st.enqueue("run", {"bot_id": "018", "task": "x", "t": 1}, priority=4)
    d = st.enqueue("create", {"objective": "o"}, priority=5)
    j1 = st.claim("w1", 300); assert j1["id"] == a["id"]
    j2 = st.claim("w2", 300, kinds=("run", "test", "tick")); assert j2["id"] == c["id"]      # 004 test skipped (bot busy), 018 run taken
    j3 = st.claim("w3", 300, kinds=("run", "test", "tick")); assert j3 is None                # nothing left in fast kinds that isn't bot-locked
    j4 = st.claim("w4", 300); assert j4["id"] == d["id"]                                        # slow worker still takes the create
    st.done(j1["id"], {}, "w1")
    j5 = st.claim("w2", 300, kinds=("test",)); assert j5["id"] == b["id"]                       # 004 free again


def test_d080_quota_hit_during_test_cools_lane_immediately(tmp_path, monkeypatch):
    """D-080: a 429 seen in a real test run cools that lane now (provider retry-after honoured), so the next chain resolve
    skips it without waiting for the hourly probe."""
    reg, fb, fp = _reg(tmp_path, monkeypatch)
    import importlib, factory_probe as fpr; importlib.reload(fpr)
    monkeypatch.setattr(fpr, "ROOT", tmp_path)
    e = reg.get("models", "groq-a"); e.model = "openai/gpt-oss-120b"; reg.upsert("models", e)
    now = time.time() + 5000   # future 'now' so resolve_chain's real clock still sees the cooldown
    cooled = fpr.mark_quota([{"model": "openai/gpt-oss-120b", "secs": 674}, {"model": "nope/unknown", "secs": 5}], now=now)
    assert cooled == ["groq-a"]
    h = reg.get("models", "groq-a").limits["health"]
    assert h["ok"] is False and h["last_outcome"] == "quota" and h["quota_until"] == now + 674
    # chain resolve drops it
    from factory.factory import BotFactory
    chain = BotFactory(reg, tmp_path / "bots").resolve_chain({"primary": "groq-a", "fallbacks": ["gemini-b", "or-c"]})
    assert "groq-a" not in chain and chain[0] == "gemini-b"
    # short retry-after is floored to 60 s; a probe ok clears it
    assert fpr.mark_quota([{"model": "groq-a", "secs": 1}], now=now + 2000) == ["groq-a"]
    assert reg.get("models", "groq-a").limits["health"]["quota_until"] == now + 2060


def test_d081_heartbeat_readopts_after_sleep_or_reports_lost(tmp_path):
    """D-081: lease expired during a laptop sleep -> job back to queued while the worker still runs it.
    heartbeat re-adopts if unclaimed; if another worker took it, 'lost' and the first must not write its result."""
    from factory.jobs import JobStore
    st = JobStore(tmp_path / "jobs.sqlite3")
    j = st.enqueue("repair", {"bot_id": "004"})
    a = st.claim("w1", lease_s=300)
    assert st.heartbeat(a["id"], "w1", 1) == "ok"                    # last beat before the laptop slept
    time.sleep(1.1)
    assert st.claim("w-fast", 300, kinds=("test",)) is None       # fast lane: expires the lease -> queued, doesn't take repair
    assert st.get(a["id"])["state"] == "queued"
    assert st.heartbeat(a["id"], "w1", 300) == "readopted"          # w1 still running it -> takes it back, same attempt
    g = st.get(a["id"]); assert g["state"] == "running" and g["lease_owner"] == "w1" and g["attempts"] == 1
    assert any(r["event"] == "job.readopted" for r in st.audit_rows(20))
    # now simulate the other case: lease lost AND another worker claimed it
    st.db.execute("UPDATE jobs SET state='queued',lease_owner=NULL,lease_until=NULL WHERE id=?", (a["id"],)); st.db.commit()
    b = st.claim("w2", 300); assert b["id"] == a["id"]
    assert st.heartbeat(a["id"], "w1", 300) == "lost"
    assert st.get(a["id"])["lease_owner"] == "w2"                   # untouched
