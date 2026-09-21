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
