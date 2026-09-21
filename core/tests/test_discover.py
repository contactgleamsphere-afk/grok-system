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
    cfg = tmp_path / "config.json"; cfg.write_text(json.dumps({"modelPresets": {"or-old": {"model": "old/one:free", "provider": "openrouter"}}, "providers": {"openrouter": {"apiKey": "${K}"}}}))
    import importlib, factory_presets as fps; importlib.reload(fps)
    added, removed = fps.sync(cfg)
    c = json.loads(cfg.read_text())
    assert added == ["or-new"] and removed == ["or-old"] and "or-new" in c["modelPresets"] and c["providers"]["openrouter"]["apiKey"] == "${K}"
