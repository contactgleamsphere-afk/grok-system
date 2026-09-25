# Architecture

## Principles

1. Local OpenAI-compatible inference is the only mandatory “brain”.
2. Agent harness is swappable; tools speak MCP where possible.
3. Coding, research, and browser lanes are separate processes/services.
4. No component is adopted on stars alone — licence, activity, local-model path, and security are checked first.
5. Paid APIs are optional accelerators, never defaults.

## Logical diagram

```
Interfaces
  nanobot WebUI / CLI
  Aider / Cline / Continue
  Optional AnythingLLM
        │
        ▼
Orchestrator (nanobot)
  planning · multi-agent · Dream memory · cron · MCP gateway
        │
   ┌────┼────────────────┐
   ▼    ▼                ▼
Coding  Research      Browser
Aider   gpt-researcher browser-use
OpenHands*  Haystack*  Playwright / playwright-mcp
openinterpreter
        │
        ▼
Model gateway: Ollama (:11434)  [optional llama.cpp / LocalAI / vLLM]
        │
        ▼
Optional memory store: Qdrant/Chroma + local embeddings
        │
        ▼
Host: laptop or VPS (Docker recommended for sandboxes)
```

\* OpenHands / heavy compose stacks wait until Docker exists on the host.

## Trust boundaries

| Zone | Trust | Notes |
|------|-------|-------|
| Model server | High | Keep on localhost; no public `:11434` |
| Orchestrator | High | Can run shell — treat as root-equivalent for the OS user |
| Browser profile | Medium | Isolate from daily browser profile |
| MCP filesystem/shell | High risk | Least privilege paths only |
| GitHub PAT | Secret | Fine-grained; rotate if leaked to chat |

## Evolution path

1. **v0** — docs + pins (this scaffold)
2. **v1** — Ollama + nanobot + Aider on one host, zero cloud keys
3. **v2** — MCP tools + browser-use + AnythingLLM RAG
4. **v3** — OpenHands Docker sandbox + Letta/mem0 + research lane
5. **v4** — Self-improvement loop (skill discovery, repo evaluation pipeline)

## Factory execution path (2026-09-22)
```
owner CLI / master 001 chat / scheduled tasks ──add──▶ run/jobs.sqlite3 (JobStore: lease 5 min + heartbeat, idem, priority, retry, audit)
                                                              │ claim
                                                 factory_worker.py (scheduled task; single instance via run/worker.lock; restarts on code change)
   bot lifecycle                                              ├─ create      → cmd_create (architect LLM → validate_spec + spec_consistency) → build → test → guard
                                                              ├─ test        → cmd_test (all-429 = inconclusive → retest +2h; else fail twice → repair)
                                                              ├─ monitor     → factory_monitor (nightly; quota-aware) → demoted? → repair
                                                              ├─ repair      → factory_repair (instructions only, sandbox, frozen perms) → guard
                                                              │                  └─ inconsistent spec → logic pause → one automatic rearchitect
                                                              ├─ rearchitect → cmd_rearchitect (from ORIGINAL objective, allowance-bounded, diff audited)
   model lanes                                                ├─ probe       → factory_probe (hourly; health, probation, BLOCK) → presets sync
                                                              │                  └─ lane BLOCKED or <5 healthy → discover
                                                              ├─ discover    → factory_discover (catalogue → sandbox tool loop → INFERRED probation) → bench
                                                              ├─ bench       → factory_bench (pinned single-lane reference suite, rolling 3, quota-aware)
                                                              │                  → limits.bench → default_fallbacks() ranking
   reporting                                                  └─ report      → STATUS.md (+ daily stale bench sweep)
                                             failure → classify (transient/quota/model/logic/security) → retry / route / pause
                                             every event → audit table → AUDIT.md ; state files → git (laptop state commits)
```

## Memory layer (2026-09-24, D-107 — MVP)
- Per-bot: `bots/<id>/memory/MEMORY.md` is loaded by nanobot into every context. The **factory** writes it (one factual
  line per real `run`: time, task, outcome, produced files, lane), bounded to 12 lines so free-tier context budgets are
  respected (D-035). Bots do not self-edit memory; tests never write it; it sits outside the bundle seal (D-068).
- Factory-level memory is the audit chain (`run/jobs.sqlite3` + `audit/*.jsonl`, hash-chained) and the registries.
- Vector memory (Qdrant/Chroma + local embeddings) remains an optional later capability; nothing in the loop needs it yet.

## Self-healing loop (as proven live 2026-09-24)
probe (hourly) → lane BLOCKED → presets synced, chain top-up (D-103), canary monitor of affected bots (D-105)
→ test FAIL (quality) → demote → repair (rounds rotate lanes, D-056; re-verify first, D-059; sandbox 4/4; boundary diff
empty, D-099) → promote. Availability misses (429/timeout/5xx/empty, D-051/D-075/D-106) are inconclusive, never demote.

## Tool discovery, tunnel resilience, factory self-test, infra scout (2026-09-24, D-108–D-118)
- **TOOL layer — MCP pipeline** (`tools/factory_tooldisc.py`, `tools/mcp_launch.py`): official MCP registry → filter
  (stdio, pypi/npm, licence, release age) → sandbox handshake in a throw-away venv / npm cache with a secrets-stripped
  env → `registry/tool_candidates.json` → PROBATION entry in `registry/tools.json` (`mcp:<slug>`), persistent install
  under `C:\AI\Factory\mcp\<slug>`. Attachment to a bot requires `approve-tool mcp:<slug>` (owner, CLI only; the master
  bot cannot approve). `mcp_launch.py` starts the server in the bot workspace so relative paths resolve inside it
  (known limitation: absolute paths outside the workspace are not blocked by the launcher — the boundary guard is).
  npm candidates get a 240 s handshake window (cold npx), pypi 120 s.
- **INFRASTRUCTURE — tunnel**: `scripts/windows/tunnel-supervisor.ps1` (executed by task `AIFactory-Tunnel` via the
  `tools\tunnel-supervisor.ps1` shim) probes the published URL, waits for internet with an HTTPS check (ICMP fallback,
  300 s cap), restarts cloudflared and republishes `run/tunnel.txt` through git. Backstop in CORE: worker tick /
  fast-worker start call `tunnel_selfheal()` (schtasks /Run only when URL=530 and no supervisor process).
- **FACTORY self-test**: nightly `canary` job — architect → bundle → acceptance runner on a fixed objective in a
  scratch dir (`BotFactory.build(register=False)`); verdict `factory.canary` in the audit; FAIL is the first line of
  ATTENTION. Bots are monitored by `monitor`; the factory is monitored by `canary`.
- **INFRASTRUCTURE — scout**: `tools/factory_scout.py` → `registry/infra.json` + `docs/INFRA.md`: every £0 resource
  (LLM API / compute / hosting / storage), how obtained, what we hold (validated), owner action list. Weekly `scout`.
- **Master "tools" command** (`config/laptop/workspace/tools/factory.py tools`): read-only view of registered/probation
  tools for the master bot; approval stays owner-only.

## Self-improvement stage 2 and outage forensics (2026-09-25, D-121/D-122)
- **FACTORY — selfpatch** (`tools/factory_selfpatch.py`): proposal → LLM draft (find/replace edits) → envelope →
  worktree `run/selfpatch/<slug>` on branch `proposal/<date>-<slug>` → pytest → push → PR. Weekly insight enqueues ≤1;
  owner can request one (`add selfpatch --request "…"`). GitHub PR = review gate, Actions CI = second sandbox.
- **CORE — outage record** (`record_outage()` at worker start): silence >30 min → `factory.outage` with cause from
  Windows power/boot events; surfaced in STATUS for 24 h.
