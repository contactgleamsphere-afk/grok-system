"""Bot specification — the Bot Factory's input contract.

A spec is a plain dict (loaded from JSON/YAML). `validate_spec` returns a list of
problems (empty = valid) instead of raising so the factory can report all issues
at once to a human or an LLM that produced the spec.

Least-privilege is enforced here: a bot may only request tools that exist in the
tool registry, and high-risk tools require an explicit `permissions` grant.
"""
from __future__ import annotations

import re
from typing import Any

from .registry import Registry

REQUIRED = ("id", "name", "purpose", "instructions", "model_policy", "tools", "permissions", "tests")
ID_RE = re.compile(r"^[0-9]{3}$")
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{1,40}$")
ALLOWED_PERMISSIONS = {
    "fs:read", "fs:write", "shell:workspace", "shell:system",
    "net:fetch", "net:search", "github:read", "github:write", "browser", "schedule",
}
HIGH_RISK_TOOL_PERMISSION = {  # tool risk "high" needs one of these explicitly
    "shell": "shell:workspace", "github": "github:write", "browser": "browser",
}


def validate_spec(spec: dict[str, Any], registry: Registry) -> list[str]:
    problems: list[str] = []
    if not isinstance(spec, dict):
        return ["spec must be an object"]
    for k in REQUIRED:
        if k not in spec:
            problems.append(f"missing field: {k}")
    if problems:
        return problems

    if not ID_RE.match(str(spec["id"])):
        problems.append("id must be 3 digits, e.g. '002'")
    if not NAME_RE.match(str(spec["name"])):
        problems.append("name must be lowercase slug (a-z, 0-9, -), 2-41 chars")
    if len(str(spec["purpose"]).strip()) < 10:
        problems.append("purpose too short")
    if len(str(spec["instructions"]).strip()) < 20:
        problems.append("instructions too short")

    mp = spec["model_policy"]
    models = {m.id for m in registry.all("models")}
    if not isinstance(mp, dict) or "primary" not in mp:
        problems.append("model_policy.primary required")
    else:
        if mp["primary"] not in models:
            problems.append(f"model_policy.primary '{mp['primary']}' not in model registry")
        for fb in mp.get("fallbacks", []):
            if fb not in models:
                problems.append(f"fallback '{fb}' not in model registry")

    perms = set(spec["permissions"])
    bad = perms - ALLOWED_PERMISSIONS
    if bad:
        problems.append(f"unknown permissions: {sorted(bad)}")
    if "shell:system" in perms:
        problems.append("shell:system is not grantable to factory-made bots")

    tools = {t.id: t for t in registry.all("tools")}
    for tid in spec["tools"]:
        t = tools.get(tid)
        if t is None:
            problems.append(f"tool '{tid}' not in tool registry")
            continue
        if t.risk == "high":
            for tag, needed in HIGH_RISK_TOOL_PERMISSION.items():
                if tag in t.provides and needed not in perms:
                    problems.append(f"tool '{tid}' is high-risk ({tag}); requires permission '{needed}'")

    if not isinstance(spec["tests"], list) or not spec["tests"]:
        problems.append("at least one test required")
    for s in spec.get("schedules", []):
        if not re.match(r"^(\S+\s+){4}\S+$", str(s)):
            problems.append(f"schedule '{s}' is not 5-field cron")
    return problems
