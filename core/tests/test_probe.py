import json, sys, pathlib, os
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from factory.registry import Registry, ModelEntry


def _reg(tmp_path):
    r = Registry(tmp_path)
    for i, (mid, prov) in enumerate([("a", "groq"), ("b", "gemini"), ("c", "gemini"), ("l", "ollama")]):
        r.upsert("models", ModelEntry(id=mid, provider=prov, model=f"m-{mid}", capabilities=["chat", "tools"], context_window=8000,
                                      location="local" if prov == "ollama" else "remote", verified="VERIFIED", tool_call_score=1.0))
    return r


def test_probe_classifies_and_self_heals(tmp_path, monkeypatch):
    monkeypatch.setenv("AIFACTORY_REPO", str(tmp_path)); (tmp_path / "registry").mkdir()
    reg = _reg(tmp_path / "registry")
    import importlib, factory_probe as fp; importlib.reload(fp)
    for k in ("GROQ_API_KEY", "GEMINI_API_KEY"): monkeypatch.setenv(k, "x")
    outcomes = {"m-a": {"outcome": "ok", "latency_s": 0.5}, "m-b": {"outcome": "gone", "http": 404, "detail": "no longer available"},
                "m-c": {"outcome": "quota", "http": 429}}
    out = fp.run(prober_remote=lambda base, key, model: outcomes[model], prober_local=lambda m: {"outcome": "ok"})
    reg = Registry(tmp_path / "registry")
    assert reg.get("models", "b").verified == "BLOCKED" and reg.get("models", "b").limits["health"]["blocked_by"] == "probe"
    assert reg.get("models", "c").verified == "VERIFIED" and reg.get("models", "c").limits["health"]["quota_until"] > 0
    assert set(out["healthy"]) == {"a", "l"} and [c["id"] for c in out["changed"]] == ["b"]
    # chain resolution skips BLOCKED and quota-cooled lanes but keeps a local tail
    from factory.factory import BotFactory
    chain = BotFactory(reg, tmp_path / "bots").resolve_chain({"primary": "a", "fallbacks": ["b", "c", "l"]})
    assert chain == ["a", "l"]
    # model b comes back -> self-heal to VERIFIED
    outcomes["m-b"] = {"outcome": "ok", "latency_s": 1.0}
    fp.run(prober_remote=lambda base, key, model: outcomes[model], prober_local=lambda m: {"outcome": "ok"})
    assert Registry(tmp_path / "registry").get("models", "b").verified == "VERIFIED"


def test_probe_error_blocks_after_three(tmp_path, monkeypatch):
    monkeypatch.setenv("AIFACTORY_REPO", str(tmp_path)); (tmp_path / "registry").mkdir(); _reg(tmp_path / "registry")
    import importlib, factory_probe as fp; importlib.reload(fp)
    monkeypatch.setenv("GROQ_API_KEY", "x"); monkeypatch.setenv("GEMINI_API_KEY", "x")
    for n in range(3):
        fp.run(only={"a"}, prober_remote=lambda *a: {"outcome": "error", "detail": "timeout"})
    assert Registry(tmp_path / "registry").get("models", "a").verified == "BLOCKED"


def test_live_chain_drops_blocked(tmp_path, monkeypatch):
    monkeypatch.setenv("AIFACTORY_REPO", str(tmp_path)); (tmp_path / "registry").mkdir()
    reg = _reg(tmp_path / "registry")
    b = reg.get("models", "b"); b.verified = "BLOCKED"; reg.upsert("models", b)
    bot = tmp_path / "bots" / "009-x"; bot.mkdir(parents=True)
    (bot / "bot.json").write_text(json.dumps({"model_policy": {"primary": "a", "fallbacks": ["b", "c"]}, "resolved_chain": ["a", "b", "c", "l"]}))
    import importlib, factory_chain as fc; importlib.reload(fc)
    out = fc.live_chain(bot)
    assert out["source"] == "live" and out["primary"] == "a" and out["fallbacks"] == ["c", "l"]


def test_live_lanes_and_default_fallbacks_follow_health(tmp_path, monkeypatch):
    monkeypatch.setenv("AIFACTORY_REPO", str(tmp_path)); (tmp_path / "registry").mkdir()
    reg = _reg(tmp_path / "registry")
    b = reg.get("models", "b"); b.verified = "BLOCKED"; reg.upsert("models", b)
    c = reg.get("models", "c"); c.limits = {"health": {"quota_until": 9e12}}; reg.upsert("models", c)
    import importlib, factory_pipeline as fp; importlib.reload(fp)
    lanes = fp.live_lanes()
    assert [m for _, _, _, m in lanes] == ["m-a", "m-l"]
    assert fp.default_fallbacks(Registry(tmp_path / "registry")) == ["a", "c", "l"]   # quota-cooled c still a valid *policy* member
