"""Machine-readable registries.

Design rules:
- Plain JSON on disk (portable, diffable, git-friendly). No database dependency.
- Every entry carries `verified` (VERIFIED | INFERRED | UNVERIFIED | BLOCKED) and `updated`.
- Validation is strict: unknown status values or missing required fields raise.
- Atomic writes (tmp + rename) so a crash never leaves a half-written registry.
"""
from __future__ import annotations

import json
import os
import tempfile
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

VERIFICATION_STATES = ("VERIFIED", "INFERRED", "UNVERIFIED", "BLOCKED")


class RegistryError(ValueError):
    pass


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


@dataclass
class ModelEntry:
    id: str                      # preset/name used by the router, e.g. "local3b"
    provider: str                # "ollama", "openrouter", ...
    model: str                   # provider model id
    capabilities: list[str]      # e.g. ["chat", "tools", "code"]
    context_window: int
    location: str = "local"      # local | remote
    cost_per_1k: float = 0.0
    tokens_per_sec: float | None = None
    ram_gb: float | None = None
    tool_call_score: float | None = None   # 0..1 from measured tests
    verified: str = "UNVERIFIED"
    notes: str = ""
    updated: str = field(default_factory=_now)

    def validate(self) -> None:
        if not self.id or not self.provider or not self.model:
            raise RegistryError("model entry needs id, provider, model")
        if self.verified not in VERIFICATION_STATES:
            raise RegistryError(f"bad verified state {self.verified!r}")
        if self.context_window <= 0:
            raise RegistryError("context_window must be > 0")
        if self.location not in ("local", "remote"):
            raise RegistryError("location must be local|remote")
        if self.tool_call_score is not None and not 0 <= self.tool_call_score <= 1:
            raise RegistryError("tool_call_score must be 0..1")


@dataclass
class ToolEntry:
    id: str
    kind: str                    # builtin | mcp | cli | api
    provides: list[str]          # capability tags: "filesystem", "shell", "web_search", "github"...
    risk: str = "medium"         # low | medium | high  (high = RCE/credential class)
    scope: str = ""              # e.g. "workspace-only"
    verified: str = "UNVERIFIED"
    notes: str = ""
    updated: str = field(default_factory=_now)

    def validate(self) -> None:
        if self.kind not in ("builtin", "mcp", "cli", "api"):
            raise RegistryError(f"bad tool kind {self.kind!r}")
        if self.risk not in ("low", "medium", "high"):
            raise RegistryError("risk must be low|medium|high")
        if self.verified not in VERIFICATION_STATES:
            raise RegistryError(f"bad verified state {self.verified!r}")


@dataclass
class BotEntry:
    id: str                      # "001"
    name: str
    purpose: str
    status: str                  # planned | building | testing | active | paused | retired
    model_policy: dict[str, Any] # {"primary": "local3b", "fallbacks": [...]} 
    tools: list[str]
    permissions: list[str]
    workspace: str
    version: str = "0.1.0"
    schedules: list[str] = field(default_factory=list)
    tests: list[str] = field(default_factory=list)
    verified: str = "UNVERIFIED"
    notes: str = ""
    updated: str = field(default_factory=_now)

    def validate(self) -> None:
        if self.status not in ("planned", "building", "testing", "active", "paused", "retired"):
            raise RegistryError(f"bad bot status {self.status!r}")
        if "primary" not in self.model_policy:
            raise RegistryError("model_policy needs 'primary'")
        if self.verified not in VERIFICATION_STATES:
            raise RegistryError(f"bad verified state {self.verified!r}")


_KINDS = {"models": ModelEntry, "tools": ToolEntry, "bots": BotEntry}


class Registry:
    """One JSON file per kind under `root`."""

    def __init__(self, root: str | os.PathLike):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def _path(self, kind: str) -> Path:
        if kind not in _KINDS:
            raise RegistryError(f"unknown registry kind {kind!r}")
        return self.root / f"{kind}.json"

    def load(self, kind: str) -> dict[str, Any]:
        p = self._path(kind)
        if not p.exists():
            return {}
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            raise RegistryError(f"{p} is corrupt: {e}") from e
        if not isinstance(data, dict):
            raise RegistryError(f"{p} must contain a JSON object")
        return data

    def _save(self, kind: str, data: dict[str, Any]) -> None:
        p = self._path(kind)
        fd, tmp = tempfile.mkstemp(dir=p.parent, prefix=f".{kind}.", suffix=".tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, sort_keys=True)
                f.write("\n")
            os.replace(tmp, p)
        finally:
            if os.path.exists(tmp):
                os.unlink(tmp)

    def upsert(self, kind: str, entry) -> None:
        cls = _KINDS[kind]
        if not isinstance(entry, cls):
            raise RegistryError(f"{kind} expects {cls.__name__}")
        entry.validate()
        entry.updated = _now()
        data = self.load(kind)
        data[entry.id] = asdict(entry)
        self._save(kind, data)

    def get(self, kind: str, id_: str):
        raw = self.load(kind).get(id_)
        return _KINDS[kind](**raw) if raw else None

    def all(self, kind: str) -> list:
        cls = _KINDS[kind]
        return [cls(**v) for v in self.load(kind).values()]

    def remove(self, kind: str, id_: str) -> bool:
        data = self.load(kind)
        if id_ not in data:
            return False
        del data[id_]
        self._save(kind, data)
        return True

    def to_markdown(self, kind: str) -> str:
        rows = self.all(kind)
        if not rows:
            return f"# {kind}\n\n_(empty)_\n"
        keys = list(asdict(rows[0]).keys())
        out = [f"# {kind}", "", "| " + " | ".join(keys) + " |", "|" + "---|" * len(keys)]
        for r in rows:
            d = asdict(r)
            out.append("| " + " | ".join(str(d[k]).replace("|", "\\|") for k in keys) + " |")
        return "\n".join(out) + "\n"
