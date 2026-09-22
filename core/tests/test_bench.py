import datetime, sys, pathlib
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
