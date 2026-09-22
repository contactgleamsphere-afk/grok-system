import json, sys, pathlib, time
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from factory.registry import Registry, ModelEntry

CATALOG = {"data": [
    {"id": "new/good:free", "context_length": 200000, "supported_parameters": ["tools"], "created": 300},
    {"id": "new/notools:free", "context_length": 200000, "supported_parameters": [], "created": 290},
    {"id": "new/small:free", "context_length": 8000, "supported_parameters": ["tools"], "created": 280},
    {"id": "new/badloop:free", "context_length": 100000, "supported_parameters": ["tools"], "created": 270},
    {"id": "paid/model", "context_length": 100000, "supported_parameters": ["tools"], "created": 260},
]}


def _setup(tmp_path, monkeypatch):
    monkeypatch.setenv("AIFACTORY_REPO", str(tmp_path)); (tmp_path / "registry").mkdir()
    monkeypatch.setenv("OPENROUTER_API_KEY", "x")
    reg = Registry(tmp_path / "registry")
    reg.upsert("models", ModelEntry(id="or-old", provider="openrouter", model="old/one:free", capabilities=["chat", "tools"], context_window=32000, location="remote", verified="BLOCKED"))
    import importlib, factory_probe, factory_discover as fd; importlib.reload(factory_probe); importlib.reload(fd)
    return reg, fd


def test_discover_evaluate_sandbox_integrate(tmp_path, monkeypatch):
    reg, fd = _setup(tmp_path, monkeypatch)
    prober = lambda base, key, model: {"outcome": "ok", "latency_s": 1.0}
    looper = lambda base, key, model: {"ok": model != "new/badloop:free", "reason": "final answer 'nope'", "latency_s": 2.0}
    out = fd.run("openrouter", 5, fetch=lambda url: CATALOG, prober=prober, looper=looper)
    assert out["added"] == ["or-good"]
    v = {x["model"]: x["verdict"] for x in out["verdicts"]}
    assert v["new/good:free"] == "approved" and v["new/badloop:free"] == "rejected" and v["new/notools:free"] == "filtered"
    e = Registry(tmp_path / "registry").get("models", "or-good")
    assert e.verified == "INFERRED" and e.limits["health"]["probation"] == 2
    # ledger prevents re-testing the rejected model
    out2 = fd.run("openrouter", 5, fetch=lambda url: CATALOG, prober=prober, looper=looper)
    assert out2["added"] == [] and not any(x["model"] == "new/badloop:free" and x["verdict"] == "rejected" for x in out2["verdicts"])
    # probation: two clean probes -> VERIFIED
    import factory_probe as fp
    for _ in range(2):
        fp.run(only={"or-good"}, prober_remote=lambda *a: {"outcome": "ok", "latency_s": 0.9})
    assert Registry(tmp_path / "registry").get("models", "or-good").verified == "VERIFIED"


def test_presets_sync_adds_and_removes(tmp_path, monkeypatch):
    reg, fd = _setup(tmp_path, monkeypatch)
    reg.upsert("models", ModelEntry(id="or-new", provider="openrouter", model="n/x:free", capabilities=["chat", "tools"], context_window=32000, location="remote", verified="INFERRED"))
    reg.upsert("models", ModelEntry(id="ovh-x", provider="custom", model="x", capabilities=["chat", "tools"], context_window=32000, location="remote", verified="BLOCKED"))
    reg.upsert("models", ModelEntry(id="ovh-y", provider="custom", model="y", capabilities=["chat", "tools"], context_window=32000, location="remote", verified="INFERRED"))
    cfg = tmp_path / "config.json"; cfg.write_text(json.dumps({"modelPresets": {"or-old": {"model": "old/one:free", "provider": "openrouter"}, "ovh-x": {"model": "x", "provider": "custom"}}, "providers": {"openrouter": {"apiKey": "${K}"}}}))
    import importlib, factory_presets as fps; importlib.reload(fps)
    added, removed = fps.sync(cfg)
    c = json.loads(cfg.read_text(encoding="utf-8"))
    assert added == ["or-new"] and sorted(removed) == ["or-old", "ovh-x"] and "or-new" in c["modelPresets"] and c["providers"]["openrouter"]["apiKey"] == "${K}"
    assert "ovh-y" not in c["modelPresets"]     # BLOCKED custom lanes are pruned, but custom lanes are never auto-added


def test_probation_lane_blocked_on_first_failure(tmp_path, monkeypatch):
    reg, fd = _setup(tmp_path, monkeypatch)
    reg.upsert("models", ModelEntry(id="or-p", provider="openrouter", model="p/x:free", capabilities=["chat", "tools"], context_window=32000, location="remote",
                                    verified="INFERRED", limits={"health": {"probation": 2}}))
    import factory_probe as fp
    fp.run(only={"or-p"}, prober_remote=lambda *a: {"outcome": "error", "detail": "timeout"})
    assert Registry(tmp_path / "registry").get("models", "or-p").verified == "BLOCKED"


def test_d084_quota_during_discovery_defers_instead_of_rejecting(tmp_path, monkeypatch):
    """D-084: a 429 on the account during discovery must not brand the model 'rejected' for 7 days. It is deferred
    (6 h), the provider is skipped for the rest of the window, and after expiry the same slug is evaluated again."""
    reg, fd = _setup(tmp_path, monkeypatch)
    prober = lambda base, key, model: {"outcome": "quota", "detail": "rate limit exceeded: free-models-per-day"}
    looper = lambda base, key, model: {"ok": True, "latency_s": 1.0}
    out = fd.run("openrouter", 5, fetch=lambda url: CATALOG, prober=prober, looper=looper)
    assert out["added"] == [] and out["provider_quota"] is True
    assert [x["verdict"] for x in out["verdicts"] if x["model"] == "new/good:free"] == ["deferred"]
    led = json.loads((tmp_path / "registry" / "discovery.json").read_text())
    assert led["verdicts"]["openrouter:new/good:free"]["verdict"] == "deferred" and "provider-quota:openrouter" in led["verdicts"]
    assert "new/badloop:free" not in " ".join(led["verdicts"])           # probing stopped at the first 429
    # within the window: provider skipped entirely (no API spend)
    out2 = fd.run("openrouter", 5, fetch=lambda url: CATALOG, prober=prober, looper=looper)
    assert "daily free cap" in out2["skipped"]
    # window over: candidate is evaluated again and, with a healthy account, integrated
    for k, v in led["verdicts"].items(): v["until"] = time.time() - 1
    (tmp_path / "registry" / "discovery.json").write_text(json.dumps(led))
    out3 = fd.run("openrouter", 5, fetch=lambda url: CATALOG, prober=lambda b, k, m: {"outcome": "ok", "latency_s": 1.0}, looper=looper)
    assert "or-good" in out3["added"]


def test_d086_whole_sweep_error_is_network_outage_not_lane_health(tmp_path, monkeypatch):
    """D-086: every remote lane erroring in one sweep (>=2 providers) = local network down; health must not change."""
    reg, fd = _setup(tmp_path, monkeypatch)
    monkeypatch.setenv("GROQ_API_KEY", "x"); monkeypatch.setenv("GEMINI_API_KEY", "x")
    reg.upsert("models", ModelEntry(id="g1", provider="groq", model="a", capabilities=["chat", "tools"], context_window=32000, location="remote", verified="VERIFIED", limits={"health": {"ok": True, "failures": 0, "last_outcome": "ok"}}))
    reg.upsert("models", ModelEntry(id="m1", provider="gemini", model="b", capabilities=["chat", "tools"], context_window=32000, location="remote", verified="VERIFIED", limits={"health": {"ok": True, "failures": 2, "last_outcome": "ok"}}))
    import factory_probe as fp
    out = fp.run(only={"g1", "m1"}, prober_remote=lambda *a: {"outcome": "error", "detail": "URLError"})
    assert out["network_down"] is True and out["changed"] == []
    m = Registry(tmp_path / "registry").get("models", "m1")
    assert m.limits["health"]["failures"] == 2 and m.verified == "VERIFIED"        # would have been BLOCKED at 3
    # a single provider erroring is still a real signal
    out2 = fp.run(only={"g1", "m1"}, prober_remote=lambda base, key, model: {"outcome": "error", "detail": "500"} if model == "b" else {"outcome": "ok", "latency_s": 1})
    assert not out2.get("network_down") and Registry(tmp_path / "registry").get("models", "m1").verified == "BLOCKED"
