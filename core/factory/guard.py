"""Security boundary check for every registry mutation (D-032).

`assert_no_silent_expansion(before, after, allow_expansion=False)` compares two bot specs/entries and raises
SecurityViolation if permissions, tools, model_policy, network or shell exposure grew without an explicit,
owner-authorised expansion flag. Used by the worker around create/repair/promote so no code path — including
future self-improvement — can widen a bot's blast radius quietly. Also snapshots the resolved nanobot patch
(disabled tools + env) so a bundle rebuild can't re-enable tools behind the spec's back.
"""
from __future__ import annotations
import json
from typing import Any

NET_PERMS = {"net:search", "net:fetch", "net:any"}
SHELL_PERMS = {"shell:workspace", "shell:system"}
CRED_KEYS = ("api_key", "apikey", "token", "secret", "password", "GROQ_API_KEY", "GEMINI_API_KEY", "OPENROUTER_API_KEY")


class SecurityViolation(Exception):
    pass


def _s(x) -> set:
    return set(x or [])


def diff_boundaries(before: dict, after: dict) -> dict[str, Any]:
    b_p, a_p = _s(before.get("permissions")), _s(after.get("permissions"))
    b_t, a_t = _s(before.get("tools")), _s(after.get("tools"))
    out: dict[str, Any] = {}
    if a_p - b_p: out["permissions_added"] = sorted(a_p - b_p)
    if a_t - b_t: out["tools_added"] = sorted(a_t - b_t)
    if (a_p & NET_PERMS) - (b_p & NET_PERMS): out["network_expanded"] = sorted((a_p & NET_PERMS) - (b_p & NET_PERMS))
    if (a_p & SHELL_PERMS) - (b_p & SHELL_PERMS): out["shell_expanded"] = sorted((a_p & SHELL_PERMS) - (b_p & SHELL_PERMS))
    bm, am = before.get("model_policy") or {}, after.get("model_policy") or {}
    if json.dumps(bm, sort_keys=True) != json.dumps(am, sort_keys=True): out["model_policy_changed"] = {"before": bm, "after": am}
    # credentials must never appear in a spec/bundle
    blob = json.dumps(after, default=str)
    leaked = [k for k in CRED_KEYS if k.lower() in blob.lower() and k not in ("api_key", "apikey", "token", "secret", "password")]
    for k in ("gsk_", "AIza", "sk-or-v1-", "ghp_", "github_pat_"):
        if k in blob: leaked.append(k + "…")
    if leaked: out["credential_material"] = leaked
    b_env, a_env = (before.get("env") or {}), (after.get("env") or {})
    b_dis, a_dis = _s((b_env.get("AIFACTORY_DISABLED_TOOLS") or "").split(",")), _s((a_env.get("AIFACTORY_DISABLED_TOOLS") or "").split(","))
    if b_dis and (b_dis - a_dis) - {""}: out["tools_reenabled_in_bundle"] = sorted((b_dis - a_dis) - {""})
    return out


def assert_no_silent_expansion(before: dict, after: dict, *, allow_expansion: bool = False, context: str = "") -> dict:
    d = diff_boundaries(before, after)
    if "credential_material" in d:
        raise SecurityViolation(f"{context}: credential material in spec/bundle: {d['credential_material']}")
    widening = {k: v for k, v in d.items() if k != "model_policy_changed"} if allow_expansion is False else {}
    if widening:
        raise SecurityViolation(f"{context}: silent boundary expansion {json.dumps(widening)}")
    return d


# D-035: runtime config hygiene — silent bloat in config.json eats the model context budget of every bot test.
CONFIG_MAX_BYTES = 60_000
CONFIG_MAX_STR = 2_000


def config_hygiene(config: dict, size_bytes: int) -> list[str]:
    """Return a list of problems (empty = healthy). Pure function; caller supplies the parsed config and file size."""
    problems = []
    if size_bytes > CONFIG_MAX_BYTES:
        problems.append(f"config.json is {size_bytes} bytes (> {CONFIG_MAX_BYTES})")

    def walk(o, path=""):
        if isinstance(o, dict):
            for k, v in o.items(): walk(v, f"{path}/{k}")
        elif isinstance(o, list):
            for i, v in enumerate(o): walk(v, f"{path}[{i}]")
        elif isinstance(o, str) and len(o) > CONFIG_MAX_STR:
            problems.append(f"{path} is a {len(o)}-char string (> {CONFIG_MAX_STR}); mojibake/bloat?")
    walk(config)
    icon = (config.get("agents", {}).get("defaults", {}) or {}).get("botIcon", "")
    if len(icon) > 8:
        problems.append(f"agents.defaults.botIcon is {len(icon)} chars (should be one glyph)")
    return problems


# D-068: bundle integrity. The security-relevant files of a bot bundle are sealed after build/rearchitect; anything
# (a repair candidate that escaped its sandbox, a stray edit, malware) that changes them makes the bot unrunnable
# until re-sealed by the factory itself. The seal lives in the registry entry (git), not in the bundle.
SEALED_FILES = ("bot.json", "nanobot.patch.json", "AGENTS.md", "SOUL.md")


def bundle_seal(bot_dir) -> dict:
    import hashlib, pathlib
    bot_dir = pathlib.Path(bot_dir); out = {}
    for name in SEALED_FILES:
        f = bot_dir / name
        out[name] = hashlib.sha256(f.read_bytes()).hexdigest()[:24] if f.exists() else None
    return out


def bundle_drift(bot_dir, seal: dict | None) -> list[str]:
    """Names of sealed files whose content differs from the recorded seal. Empty seal = never sealed (reported as such)."""
    if not seal:
        return ["<unsealed>"]
    now = bundle_seal(bot_dir)
    return [k for k in SEALED_FILES if now.get(k) != seal.get(k)]
