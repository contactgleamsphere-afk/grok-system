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
    "shell": "shell:workspace", "github": "github:write", "browser": "browser", "write": "fs:write",
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
    bad = {x for x in perms if x not in ALLOWED_PERMISSIONS and not x.startswith("mcp:")}   # D-110: mcp:<server> grants
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
        if t.kind == "mcp" and "PROBATION" in (t.scope or ""):        # D-108/D-109: discovered, sandboxed, but NOT owner-approved
            problems.append(f"tool '{tid}' is on probation (owner approval required before any bot may use it)")
            continue
        if t.kind == "mcp" and f"mcp:{tid.split(':', 1)[-1]}" not in perms and tid not in perms:   # D-110: every MCP server is an explicit grant
            problems.append(f"tool '{tid}' is an MCP server; requires explicit permission '{tid}' in the spec")
        if t.risk == "high":
            for tag, needed in HIGH_RISK_TOOL_PERMISSION.items():
                if tag in t.provides and needed not in perms:
                    problems.append(f"tool '{tid}' is high-risk ({tag}); requires permission '{needed}'")

    fx = spec.get("fixtures") or []                          # D-111 test fixtures
    if not isinstance(fx, list) or len(fx) > 4:
        problems.append("fixtures must be a list of at most 4 files")
    else:
        for f in fx:
            if not isinstance(f, dict) or not re.match(r"^[A-Za-z0-9._-]{1,64}$", str(f.get("name", ""))) or str(f.get("name", "")).startswith("."):
                problems.append(f"fixture name must be a plain filename: {f!r}"[:120]); continue
            body = f.get("text") if "text" in f else f.get("sql")
            if not isinstance(body, str) or not body.strip() or len(body) > 4096 or ("text" in f) == ("sql" in f):
                problems.append(f"fixture {f.get('name')} needs exactly one of text|sql, 1..4096 chars")
            if "sql" in f and not str(f["name"]).endswith((".db", ".sqlite", ".sqlite3")):
                problems.append(f"sql fixture {f.get('name')} must be a .db/.sqlite file")
    if not isinstance(spec["tests"], list) or not spec["tests"]:
        problems.append("at least one test required")
    for s in spec.get("schedules", []):
        if not re.match(r"^(\S+\s+){4}\S+$", str(s)):
            problems.append(f"schedule '{s}' is not 5-field cron")
    return problems
