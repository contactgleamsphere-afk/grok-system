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
    assert json.loads((tmp_path / "models.json").read_text(encoding="utf-8"))["deep"]["model"] == "qwen3:8b"


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
    patch = json.loads((r.bot_dir / "nanobot.patch.json").read_text(encoding="utf-8"))
    assert patch["agents"]["defaults"]["modelPreset"] == "remote"
    disabled = patch["env"]["AIFACTORY_DISABLED_TOOLS"].split(",")
    assert "exec" in disabled and "write_file" in disabled and "web_fetch" in disabled   # not granted
    assert "web_search" not in disabled and "read_file" not in disabled                 # granted
    assert "spawn" in disabled and "message" in disabled                                # never granted
    assert patch["env"]["AIFACTORY_TEMPLATE_DIR"].endswith("templates")
    assert len((r.bot_dir / "templates/agent/tool_contract.md").read_text(encoding="utf-8")) < 1200      # lean contract (D-020)
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
    spec = json.loads((pathlib.Path(__file__).resolve().parents[2] / "specs" / "003-code-smith.json").read_text(encoding="utf-8"))
    assert validate_spec(spec, reg) == []
    bad = dict(spec, permissions=["fs:read", "fs:write"])   # exec without shell:workspace
    assert any("exec" in p or "shell" in p for p in validate_spec(bad, reg))
    worse = dict(spec, permissions=["fs:read", "fs:write", "shell:system"])
    assert validate_spec(worse, reg)  # shell:system never allowed


def _reg_and_factory(tmp_path):
    import pathlib, shutil
    from core.factory.registry import Registry
    from core.factory.factory import BotFactory
    root = pathlib.Path(__file__).resolve().parents[2]
    d = tmp_path / "realreg"; shutil.copytree(root / "registry", d / "registry")
    r = Registry(d / "registry"); return r, BotFactory(r, d / "bots")


def _rspec(**over):
    base = {"id": "099", "name": "tmp-bot", "purpose": "temporary test bot for unit tests only",
            "instructions": "Do nothing dangerous. This is a unit-test spec with enough words to pass validation.",
            "model_policy": {"primary": "groq-gptoss20b", "fallbacks": ["local4b"]},
            "tools": ["read_file"], "permissions": ["fs:read"],
            "tests": ["Reply with exactly: OK -> OK"]}
    base.update(over); return base


def test_d023_escape_test_injected_for_write_and_shell(tmp_path):
    reg, f = _reg_and_factory(tmp_path)
    r = f.build(_rspec(tools=["write_file", "read_file", "exec"], permissions=["fs:read", "fs:write", "shell:workspace"]))
    import json
    tests = json.loads((r.bot_dir / "bot.json").read_text(encoding="utf-8"))["tests"]
    assert any(t.endswith("-> CONFINED") and "exec" in t for t in tests)
    r2 = f.build(_rspec(id="098", tools=["write_file", "read_file"], permissions=["fs:read", "fs:write"]))
    t2 = json.loads((r2.bot_dir / "bot.json").read_text(encoding="utf-8"))["tests"]
    assert any(t.endswith("-> CONFINED") and "exec" not in t for t in t2)


def test_d023_not_injected_for_readonly_bot(tmp_path):
    reg, f = _reg_and_factory(tmp_path)
    r = f.build(_rspec())
    import json
    assert not any("CONFINED" in t for t in json.loads((r.bot_dir / "bot.json").read_text(encoding="utf-8"))["tests"])


def test_factory_failure_modes(tmp_path):
    import pytest
    from core.factory.factory import FactoryError
    reg, f = _reg_and_factory(tmp_path)
    with pytest.raises(FactoryError, match="not in model registry"):
        f.build(_rspec(model_policy={"primary": "does-not-exist", "fallbacks": ["local4b"]}))
    with pytest.raises(FactoryError, match="tool"):
        f.build(_rspec(tools=["browser_nuke"]))
    # a chain with no local model gets one appended automatically (never remote-only)
    r = f.build(_rspec(id="097", model_policy={"primary": "groq-gptoss20b", "fallbacks": ["gemini-lite"]}))
    assert r.chain[-1].startswith("local")
    f.build(_rspec())
    with pytest.raises(FactoryError, match="already exists"):
        f.build(_rspec())


def test_rebuild_demotes_to_testing_and_keeps_history(tmp_path):
    reg, f = _reg_and_factory(tmp_path)
    f.build(_rspec()); f.record_test_result("099", 1, 1, "ok")
    assert reg.get("bots", "099").status == "active"
    f.build(_rspec(), overwrite=True)
    e = reg.get("bots", "099")
    assert e.status == "testing" and e.verified == "UNVERIFIED" and "previous: active/VERIFIED" in e.notes


def test_pipeline_objective_to_spec_with_fake_llm(tmp_path, monkeypatch):
    import json, sys, pathlib, importlib
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
    fp = importlib.import_module("factory_pipeline")
    reg, f = _reg_and_factory(tmp_path)
    good = {"id": "999", "name": "unit-tally", "purpose": "count words in text given by the user, for unit tests",
            "instructions": "You count words. When given text, reply with only the integer number of whitespace-separated words. Never use tools other than read_file. Never guess; count precisely.",
            "model_policy": {"primary": "groq-gptoss120b", "fallbacks": ["gemini-flash", "local4b"]},
            "tools": ["read_file"], "permissions": ["fs:read"],
            "tests": ["Reply with exactly: TALLY_OK -> TALLY_OK", "How many words: the quick brown fox -> 4"], "notes": "unit"}
    bad = dict(good, tools=["exec"], permissions=["fs:read"])            # first answer: exec without shell perm
    answers = iter(["garbage not json", json.dumps(bad), json.dumps(good)])
    monkeypatch.setattr(fp, "chat", lambda msgs, max_tokens=1200: (next(answers), "fake:lane"))
    spec, lane = fp.objective_to_spec("count words", reg, "099")
    assert lane == "fake:lane" and spec["id"] == "099" and spec["tools"] == ["read_file"]
    assert fp.next_id(reg) == f"{max(int(b.id) for b in reg.all('bots')) + 1:03d}"
    r = f.build(spec)
    assert (r.bot_dir / "bot.json").exists() and r.chain[-1] == "local4b"


def test_monitor_demotes_failed_bot_and_keeps_passing(tmp_path, monkeypatch):
    import sys, pathlib, importlib, json
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
    fm = importlib.import_module("factory_monitor"); fp = importlib.import_module("factory_pipeline")
    reg, f = _reg_and_factory(tmp_path)
    monkeypatch.setattr(fm, "ROOT", reg.root.parent); monkeypatch.setattr(fp, "WIN", False)
    f.build(_rspec(id="097", name="pass-bot")); f.record_test_result("097", 1, 1, "ok")
    f.build(_rspec(id="098", name="fail-bot")); f.record_test_result("098", 1, 1, "ok")
    fake = lambda bot_dir: {"pass": 0 if "fail-bot" in str(bot_dir) else 1, "total": 1, "evidence": "fake"}
    out = fm.monitor(only={"097", "098"}, runner=fake)
    assert out["ok"] is False and out["regressed"] == ["098"]
    assert reg.get("bots", "097").status == "active" and reg.get("bots", "098").status == "testing"
    assert "098 fail-bot" in (reg.root.parent / "MONITOR.md").read_text(encoding="utf-8")


def test_monitor_quota_failures_are_inconclusive_not_demotions(tmp_path, monkeypatch):
    import sys, pathlib, importlib
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
    fm = importlib.import_module("factory_monitor"); fp = importlib.import_module("factory_pipeline")
    reg, f = _reg_and_factory(tmp_path)
    monkeypatch.setattr(fm, "ROOT", reg.root.parent); monkeypatch.setattr(fp, "WIN", False)
    f.build(_rspec(id="095", name="quota-bot")); f.record_test_result("095", 1, 1, "ok")
    fake = lambda bot_dir: {"pass": 0, "total": 2, "quota": 2, "evidence": "429s"}      # all failures were rate limits
    out = fm.monitor(only={"095"}, runner=fake)
    assert out["ok"] is True and out["inconclusive"] == ["095"] and out["rows"][0]["inconclusive"]
    assert reg.get("bots", "095").status == "active"                                    # NOT demoted, no repair
    fake2 = lambda bot_dir: {"pass": 0, "total": 2, "quota": 1, "evidence": "1 real fail"}   # one genuine failure -> demote
    out = fm.monitor(only={"095"}, runner=fake2)
    assert out["regressed"] == ["095"] and reg.get("bots", "095").status == "testing"


def test_repair_rejects_permission_expansion_and_promotes_on_pass(tmp_path, monkeypatch):
    import sys, pathlib, importlib, json
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
    fr = importlib.import_module("factory_repair"); fp = importlib.import_module("factory_pipeline")
    reg, f = _reg_and_factory(tmp_path); root = reg.root.parent
    monkeypatch.setattr(fr, "ROOT", root); monkeypatch.setattr(fp, "WIN", False)
    (root / "specs").mkdir(exist_ok=True)
    spec = _rspec(id="096", name="fix-me"); f.build(spec); f.record_test_result("096", 1, 1, "ok")
    (root / "specs" / "096-fix-me.json").write_text(json.dumps(spec))
    assert fr.repair("096")["ok"] is False                      # refuses to touch an active bot
    f.record_test_result("096", 0, 1, "T1 FAIL")                # demoted
    assert reg.get("bots", "096").status == "testing"
    # round 1: model tries to smuggle exec/shell perms -> must be rejected; round 2: instructions only -> pass
    answers = iter([json.dumps({"instructions": "x " * 40}), json.dumps({"instructions": "Count carefully and reply with only the number. " * 5})])
    def fake_chat(msgs, max_tokens=700, skip=None):
        return next(answers), "fake:lane"
    orig = fr.regenerate_instructions
    def regen(spec, evidence, raw="", tried=None):
        new, lane = orig(spec, evidence, raw)
        if new.startswith("x "):                                 # simulate a mutated spec being smuggled in
            spec["permissions"] = spec["permissions"] + ["shell:workspace"]; spec["tools"] = spec["tools"] + ["exec"]
        return new, lane
    monkeypatch.setattr(fr, "regenerate_instructions", regen); monkeypatch.setattr(fp, "chat", fake_chat)
    calls = []
    out = fr.repair("096", max_rounds=2, runner=lambda d: (calls.append(str(d)) or {"pass": 1, "total": 1, "evidence": "T1 PASS", "raw": ""}), skip_reverify=True)
    assert out["rounds"][0]["rejected"].startswith("frozen fields changed")
    assert out["ok"] and out["status"] == "active" and out["frozen_diff"] == []
    assert out["permissions_before"] == out["permissions_after"] == ["fs:read"]
    assert any("-repair" in c for c in calls)                   # tested in sandbox bundle
    assert list((root / "specs" / "history").glob("096-*.json"))
    assert reg.get("bots", "096").status == "active"


def test_repair_rejects_instructions_that_echo_test_tokens():
    import sys, pathlib, importlib
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
    fr = importlib.import_module("factory_repair")
    tests = ["Reply with exactly: X_OK -> X_OK", "count -> 3", "security -> CONFINED"]
    assert fr.leaks_expected_tokens("If the count is zero reply CONFINED.", tests) == ["CONFINED"]
    assert fr.leaks_expected_tokens("Always answer X_OK first.", tests) == []      # liveness token is in its own prompt
    assert fr.leaks_expected_tokens("Reply CONFINED when unsure.", ["What is 2+2 -> 4"]) == ["CONFINED"]
    assert fr.leaks_expected_tokens("Count lines and reply with the number.", tests) == []


def test_d052_repair_refuses_inconsistent_spec_and_rearchitect_fixes_from_objective(tmp_path, monkeypatch):
    import sys, pathlib, importlib, json
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
    fr = importlib.import_module("factory_repair"); fp = importlib.import_module("factory_pipeline")
    reg, f = _reg_and_factory(tmp_path); root = reg.root.parent
    monkeypatch.setattr(fr, "ROOT", root); monkeypatch.setattr(fp, "ROOT", root); monkeypatch.setattr(fp, "WIN", False)
    (root / "specs").mkdir(exist_ok=True)
    bad_tests = ["Reply with exactly: OK -> OK", "First write data.csv containing 'a,1' then read data.csv and reply with the sum -> 1"]
    spec = _rspec(id="094", name="csv-sum", tests=bad_tests, objective="Sum the amount column of data.csv")
    f.build(spec); f.record_test_result("094", 0, 2, "T2 FAIL last='CAPABILITY_MISSING: write_file'")
    (root / "specs" / "094-csv-sum.json").write_text(json.dumps(spec))
    r = fr.repair("094", chat=lambda msgs: ("should never be called", "x"))
    assert r["ok"] is False and r["error"].startswith("logic: spec/tests inconsistent")        # pauses, no LLM round burned
    # rearchitect: the architect LLM returns a consistent spec; identity is preserved, old spec archived, perms bounded
    good = {**spec, "name": "model-picked-name", "tools": ["read_file", "write_file"], "permissions": ["fs:read", "fs:write"], "id": "999"}
    seen = {}
    def chat(msgs):
        seen["prompt"] = msgs[0]["content"]; return (json.dumps(good), "fake-lane")
    monkeypatch.setattr(fp, "chat", chat)
    out = fp.cmd_rearchitect("094", allowed_permissions=["fs:read", "fs:write"])
    assert out["ok"] and out["spec"]["id"] == "094" and out["spec"]["name"] == "csv-sum"
    assert "Sum the amount column" in seen["prompt"] and "REJECTED" in seen["prompt"]
    assert out["boundary_diff"]["tools"]["after"] == ["read_file", "write_file"]
    assert list((root / "specs" / "history").glob("094-csv-sum-*-prearch.json"))
    # allowance is enforced: a spec wanting shell is refused even though the model asked for it
    monkeypatch.setattr(fp, "chat", lambda msgs: (json.dumps({**good, "tools": ["read_file", "write_file", "exec"], "permissions": ["fs:read", "fs:write", "shell:workspace"]}), "fake"))
    import pytest
    from factory.guard import SecurityViolation
    with pytest.raises(SecurityViolation):
        fp.cmd_rearchitect("094", allowed_permissions=["fs:read", "fs:write"])
