"""Model router.

Selection = filter by required capabilities + context size, then rank by
(health, tool_call_score, tokens_per_sec, cost, local-first). Fallback = ordered
retry over the ranked candidates on *retryable* failures only. A model that
keeps failing is put in cooldown so one dead provider cannot stall every request.

Provider transport is injected (callable) so the router is unit-testable without
network and can front nanobot, raw OpenAI-compatible endpoints, or anything else.
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Callable, Iterable, Protocol

from .registry import ModelEntry


class ProviderError(Exception):
    """Base. `retryable` decides whether the router moves to the next model."""
    retryable = True


class RateLimited(ProviderError):
    retryable = True


class Unavailable(ProviderError):          # connection refused, 5xx, timeout
    retryable = True


class AuthError(ProviderError):            # bad/expired key -> skip provider
    retryable = True


class BadRequest(ProviderError):           # malformed prompt, context overflow -> do NOT retry elsewhere
    retryable = False


class ContentRefused(ProviderError):
    retryable = False


class Transport(Protocol):
    def __call__(self, model: ModelEntry, prompt: str, **kw) -> str: ...


@dataclass
class Health:
    failures: int = 0
    successes: int = 0
    cooldown_until: float = 0.0
    last_error: str = ""

    def available(self, now: float) -> bool:
        return now >= self.cooldown_until


@dataclass
class RouteResult:
    text: str
    model_id: str
    attempts: list[tuple[str, str]] = field(default_factory=list)  # (model_id, outcome)
    elapsed_s: float = 0.0


@dataclass
class RouterConfig:
    max_attempts: int = 3
    failure_threshold: int = 2       # consecutive failures before cooldown
    cooldown_s: float = 60.0
    prefer_local: bool = True


class ModelRouter:
    def __init__(self, models: Iterable[ModelEntry], transport: Transport,
                 config: RouterConfig | None = None, clock: Callable[[], float] = time.monotonic):
        self.models = {m.id: m for m in models}
        self.transport = transport
        self.cfg = config or RouterConfig()
        self.clock = clock
        self.health: dict[str, Health] = {mid: Health() for mid in self.models}

    # ---------- selection ----------
    def candidates(self, required: set[str] | None = None, min_context: int = 0) -> list[ModelEntry]:
        required = required or set()
        now = self.clock()
        pool = [m for m in self.models.values()
                if required.issubset(set(m.capabilities))
                and m.context_window >= min_context
                and self.health[m.id].available(now)]

        def rank(m: ModelEntry):
            # NOTE: do not rank on raw failure count. A single transient failure would
            # permanently demote a model below its peers, so it would never be retried,
            # never reach the cooldown threshold, and never recover. Cooldown handles
            # exclusion; ranking stays capability/quality based.
            return (
                0 if (self.cfg.prefer_local and m.location == "local") else 1,
                -(m.tool_call_score or 0.0) if "tools" in required else 0,
                -(m.tokens_per_sec or 0.0),
                m.cost_per_1k,
            )
        return sorted(pool, key=rank)

    # ---------- execution ----------
    def run(self, prompt: str, required: set[str] | None = None, min_context: int = 0,
            preferred: str | None = None, **kw) -> RouteResult:
        start = self.clock()
        order = self.candidates(required, min_context)
        if preferred and preferred in self.models:
            order = [self.models[preferred]] + [m for m in order if m.id != preferred]
        if not order:
            raise Unavailable(
                f"no model satisfies capabilities={sorted(required or [])} context>={min_context} "
                f"(all in cooldown or none registered)")

        attempts: list[tuple[str, str]] = []
        last_exc: Exception | None = None
        for m in order[: self.cfg.max_attempts]:
            h = self.health[m.id]
            try:
                text = self.transport(m, prompt, **kw)
            except ProviderError as e:
                last_exc = e
                h.failures += 1
                h.last_error = f"{type(e).__name__}: {e}"
                attempts.append((m.id, type(e).__name__))
                if h.failures >= self.cfg.failure_threshold:
                    h.cooldown_until = self.clock() + self.cfg.cooldown_s
                if not e.retryable:
                    raise
                continue
            h.failures = 0
            h.successes += 1
            attempts.append((m.id, "ok"))
            return RouteResult(text=text, model_id=m.id, attempts=attempts,
                               elapsed_s=self.clock() - start)
        raise Unavailable(f"all {len(attempts)} attempts failed: {attempts}") from last_exc

    def status(self) -> dict[str, dict]:
        now = self.clock()
        return {mid: {"available": h.available(now), "failures": h.failures,
                      "successes": h.successes, "last_error": h.last_error}
                for mid, h in self.health.items()}
