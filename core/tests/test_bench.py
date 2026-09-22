import json
import datetime, sys, pathlib
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
    assert fp.default_fallbacks(reg) == ["or-c", "groq-a", "gemini-b", "local3b"]          # benchmarked first, by score; unbenched after
    assert [r["lane"] for r in fb.rank(reg)] == ["or-c", "groq-a"]


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
