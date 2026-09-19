import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from factory.registry import Registry, ModelEntry, ToolEntry, BotEntry, RegistryError
from factory.router import (ModelRouter, RouterConfig, RateLimited, Unavailable,
                            BadRequest, AuthError)
from factory.botspec import validate_spec


# ---------------- fixtures ----------------
@pytest.fixture
def reg(tmp_path):
    r = Registry(tmp_path)
    r.upsert("models", ModelEntry("local3b", "ollama", "qwen2.5:3b-instruct-q4_K_M",
                                  ["chat", "tools"], 32768, tokens_per_sec=8, tool_call_score=0.4, verified="VERIFIED"))
    r.upsert("models", ModelEntry("deep", "ollama", "qwen3:8b",
                                  ["chat", "tools", "code"], 32768, tokens_per_sec=3, tool_call_score=0.8))
    r.upsert("models", ModelEntry("remote", "openrouter", "some/free-model",
                                  ["chat", "tools", "code", "vision"], 128000, location="remote",
                                  cost_per_1k=0.0, tokens_per_sec=40, tool_call_score=0.9))
    r.upsert("tools", ToolEntry("read_file", "builtin", ["filesystem"], risk="low", scope="workspace-only"))
    r.upsert("tools", ToolEntry("exec", "builtin", ["shell"], risk="high", scope="workspace-only"))
    r.upsert("tools", ToolEntry("web_search", "builtin", ["web_search"], risk="low"))
    return r


class FakeClock:
    t = 1000.0
    def __call__(self): return self.t
    def advance(self, s): self.t += s


# ---------------- registry ----------------
def test_registry_roundtrip_and_markdown(reg):
    assert reg.get("models", "local3b").provider == "ollama"
    assert len(reg.all("tools")) == 3
    md = reg.to_markdown("models")
    assert "| local3b |" in md or "local3b" in md

def test_registry_rejects_bad_states(reg):
    with pytest.raises(RegistryError):
        reg.upsert("models", ModelEntry("x", "ollama", "m", ["chat"], 1000, verified="MAYBE"))
    with pytest.raises(RegistryError):
        reg.upsert("tools", ToolEntry("t", "magic", ["x"]))
    with pytest.raises(RegistryError):
        reg.upsert("bots", BotEntry("9", "b", "p", "flying", {"primary": "a"}, [], [], "ws"))

def test_registry_corrupt_file_is_reported_not_swallowed(tmp_path):
    (tmp_path / "models.json").write_text("{not json", encoding="utf-8")
    with pytest.raises(RegistryError, match="corrupt"):
        Registry(tmp_path).load("models")

def test_registry_atomic_write_leaves_no_tmp(reg, tmp_path):
    assert not [p for p in tmp_path.iterdir() if p.suffix == ".tmp"]
    assert json.loads((tmp_path / "models.json").read_text())["deep"]["model"] == "qwen3:8b"


# ---------------- router: selection ----------------
def test_router_prefers_local_then_tool_score(reg):
    r = ModelRouter(reg.all("models"), transport=lambda m, p, **k: "ok")
    order = [m.id for m in r.candidates({"tools"})]
    assert order[:2] == ["deep", "local3b"]      # local first; deep has higher tool score
    assert order[-1] == "remote"

def test_router_filters_capability_and_context(reg):
    r = ModelRouter(reg.all("models"), transport=lambda m, p, **k: "ok")
    assert [m.id for m in r.candidates({"vision"})] == ["remote"]
    assert [m.id for m in r.candidates(set(), min_context=100000)] == ["remote"]
    with pytest.raises(Unavailable, match="no model satisfies"):
        r.run("hi", required={"video"})


# ---------------- router: fallback + recovery ----------------
def test_fallback_on_rate_limit_then_success(reg):
    calls = []
    def transport(m, p, **k):
        calls.append(m.id)
        if m.id == "deep":
            raise RateLimited("429")
        return f"answer from {m.id}"
    r = ModelRouter(reg.all("models"), transport)
    res = r.run("hi", required={"tools"})
    assert res.model_id == "local3b"
    assert res.attempts == [("deep", "RateLimited"), ("local3b", "ok")]

def test_cooldown_removes_flapping_model_then_recovers(reg):
    clk = FakeClock()
    def transport(m, p, **k):
        if m.id == "deep":
            raise Unavailable("connection refused")
        return "ok"
    r = ModelRouter(reg.all("models"), transport, RouterConfig(failure_threshold=2, cooldown_s=60), clock=clk)
    r.run("a", required={"tools"}); r.run("b", required={"tools"})
    assert r.status()["deep"]["available"] is False           # in cooldown after 2 failures
    assert [m.id for m in r.candidates({"tools"})][0] == "local3b"
    clk.advance(61)
    assert r.status()["deep"]["available"] is True             # recovered

def test_non_retryable_error_does_not_fall_through(reg):
    def transport(m, p, **k):
        raise BadRequest("context length exceeded")
    r = ModelRouter(reg.all("models"), transport)
    with pytest.raises(BadRequest):
        r.run("huge prompt")

def test_all_fail_raises_with_attempt_trail(reg):
    def transport(m, p, **k):
        raise AuthError("invalid key")
    r = ModelRouter(reg.all("models"), transport)
    with pytest.raises(Unavailable, match="all 3 attempts failed"):
        r.run("hi")

def test_preferred_model_is_tried_first(reg):
    seen = []
    r = ModelRouter(reg.all("models"), lambda m, p, **k: seen.append(m.id) or "ok")
    r.run("hi", preferred="remote")
    assert seen == ["remote"]


# ---------------- botspec: security + malformed input ----------------
def good_spec():
    return {
        "id": "002", "name": "research-scout", "purpose": "Daily competitor research and change alerts",
        "instructions": "Search the web every morning, summarise changes, write report to workspace.",
        "model_policy": {"primary": "local3b", "fallbacks": ["deep"]},
        "tools": ["web_search", "read_file"], "permissions": ["net:search", "fs:read"],
        "tests": ["produces report file"], "schedules": ["0 7 * * *"],
    }

def test_botspec_valid(reg):
    assert validate_spec(good_spec(), reg) == []

def test_botspec_high_risk_tool_needs_permission(reg):
    s = good_spec(); s["tools"].append("exec")
    probs = validate_spec(s, reg)
    assert any("high-risk" in p and "shell:workspace" in p for p in probs)
    s["permissions"].append("shell:workspace")
    assert validate_spec(s, reg) == []

def test_botspec_blocks_system_shell_and_unknowns(reg):
    s = good_spec(); s["permissions"] += ["shell:system", "root"]
    probs = validate_spec(s, reg)
    assert any("shell:system" in p for p in probs)
    assert any("unknown permissions" in p for p in probs)

def test_botspec_unknown_model_tool_and_bad_cron(reg):
    s = good_spec(); s["model_policy"]["primary"] = "gpt-9"; s["tools"].append("nuke"); s["schedules"] = ["daily"]
    probs = validate_spec(s, reg)
    assert len([p for p in probs if "not in model registry" in p]) == 1
    assert any("'nuke' not in tool registry" in p for p in probs)
    assert any("5-field cron" in p for p in probs)

@pytest.mark.parametrize("bad", [None, [], "spec", {"id": "1"}])
def test_botspec_malformed_inputs_do_not_crash(reg, bad):
    probs = validate_spec(bad, reg)
    assert probs and all(isinstance(p, str) for p in probs)


# ---------------- Phase 4: BotFactory ----------------
from factory.factory import BotFactory, FactoryError, parse_tests


def _spec(**over):
    s = {"id": "002", "name": "research-scout", "purpose": "Find and summarise free AI infrastructure offers",
         "instructions": "Search the web for free-tier AI compute; report provider, limits, signup requirement, source URL.",
         "model_policy": {"primary": "remote", "fallbacks": ["deep"]},
         "tools": ["web_search", "read_file"], "permissions": ["net:search", "fs:read"],
         "tests": ['Reply with exactly: SCOUT_OK -> SCOUT_OK']}
    s.update(over); return s


def test_factory_builds_bundle(reg, tmp_path):
    f = BotFactory(reg, tmp_path / "bots")
    r = f.build(_spec())
    assert r.chain == ["remote", "deep"]           # deep is local -> no extra local appended
    for name in ("SOUL.md", "AGENTS.md", "bot.json", "nanobot.patch.json", "TESTS.md", "RECOVERY.md", "memory/MEMORY.md", "templates/agent/tool_contract.md"):
        assert (r.bot_dir / name).exists(), name
    patch = json.loads((r.bot_dir / "nanobot.patch.json").read_text())
    assert patch["agents"]["defaults"]["modelPreset"] == "remote"
    disabled = patch["env"]["AIFACTORY_DISABLED_TOOLS"].split(",")
    assert "exec" in disabled and "write_file" in disabled and "web_fetch" in disabled   # not granted
    assert "web_search" not in disabled and "read_file" not in disabled                 # granted
    assert "spawn" in disabled and "message" in disabled                                # never granted
    assert patch["env"]["AIFACTORY_TEMPLATE_DIR"].endswith("templates")
    assert len((r.bot_dir / "templates/agent/tool_contract.md").read_text()) < 1200      # lean contract (D-020)
    bot = reg.get("bots", "002"); assert bot.status == "building" and bot.verified == "UNVERIFIED"


def test_factory_rejects_invalid_and_duplicates(reg, tmp_path):
    f = BotFactory(reg, tmp_path / "bots")
    with pytest.raises(FactoryError):
        f.build(_spec(tools=["exec"], permissions=["fs:read"]))   # high-risk tool without shell:workspace
    f.build(_spec())
    with pytest.raises(FactoryError):
        f.build(_spec())                                           # duplicate id
    f.build(_spec(), overwrite=True)                               # explicit overwrite ok


def test_factory_chain_drops_blocked_and_appends_local(reg, tmp_path):
    m = reg.get("models", "remote"); m.verified = "BLOCKED"; reg.upsert("models", m)
    f = BotFactory(reg, tmp_path / "bots")
    r = f.build(_spec(model_policy={"primary": "remote", "fallbacks": []}))
    assert r.chain == ["deep"]                                     # BLOCKED dropped, best local appended
    with pytest.raises(FactoryError):
        m2 = reg.get("models", "deep"); m2.verified = "BLOCKED"; reg.upsert("models", m2)
        m3 = reg.get("models", "local3b"); m3.verified = "BLOCKED"; reg.upsert("models", m3)
        f.build(_spec(id="003", name="x-bot", model_policy={"primary": "remote", "fallbacks": []}))


def test_factory_test_results_flip_status(reg, tmp_path):
    f = BotFactory(reg, tmp_path / "bots"); f.build(_spec())
    e = f.record_test_result("002", 1, 2, "one failed"); assert e.status == "testing" and e.verified == "UNVERIFIED"
    e = f.record_test_result("002", 2, 2, "all good");   assert e.status == "active" and e.verified == "VERIFIED"


def test_parse_tests():
    assert parse_tests(['Say hi -> hi', 'no arrow']) == [("Say hi", "hi"), ("no arrow", "")]


def test_spec_003_code_smith_requires_shell_permission():
    import json, pathlib
    from core.factory.botspec import validate_spec
    from core.factory.registry import Registry
    reg = Registry(pathlib.Path(__file__).resolve().parents[2] / "registry")
    spec = json.loads((pathlib.Path(__file__).resolve().parents[2] / "specs" / "003-code-smith.json").read_text())
    assert validate_spec(spec, reg) == []
    bad = dict(spec, permissions=["fs:read", "fs:write"])   # exec without shell:workspace
    assert any("exec" in p or "shell" in p for p in validate_spec(bad, reg))
    worse = dict(spec, permissions=["fs:read", "fs:write", "shell:system"])
    assert validate_spec(worse, reg)  # shell:system never allowed
