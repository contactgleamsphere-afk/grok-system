# BUILD_STATE

_Last updated: 2026-09-21 — by Arena agent (architect/builder). Source of truth for "what actually exists"._

## Phase table
| Phase | Name | Status | Evidence |
|---|---|---|---|
| 0 | Discovery, baseline, tool-call test | ✅ DONE (Arena over SSH) | TEST_RESULTS.md, benchmarks/2026-09-18 |
| 1 | Foundation: nanobot 0.3.5 + Ollama + qwen2.5:3b | ✅ VERIFIED | owner report 2026-09-18: `PHASE1_OK`, WebUI 127.0.0.1:8765 |
| 2 | Core: registries, router, bot-spec contract, Master identity, security hardening | ✅ identity deployed + config hardened on laptop; core code tested in sandbox | config/laptop/config.current.json |
| 3 | Model router: keyed free-tier Master lane + OVH anon + local | 🟡 IN PROGRESS — OVH lanes live; keyed lanes staged; **failover test not yet passed** | docs/FREE_PROVIDERS_2026-09-19.md, D-010 |
| 4 | Tool layer / MCP | pending | |
| 5 | Memory | pending | |
| 6 | Coding agent | pending | |
| 7 | Browser agent | pending | |
| 8 | Bot Factory (spec → running bot) | ✅ VERIFIED (002–007) | BOT_REGISTRY.md, AUDIT.md |
| 10–11 | Monitoring + Self-improvement v0 (queue-driven) | ✅ VERIFIED live 2026-09-21 | TEST_RESULTS.md, D-029..D-034 |
| 9–12 | Multimodal, Deployment, Monitoring, Self-improvement | pending | |

## VERIFIED
- Laptop LAPTOP-LRE6PSA8: Win 11 Home 26200, Ryzen 5 7520U 4c/8t, ~14 GB RAM, Radeon 610M iGPU, 288 GB free, Python 3.11.9, Node 24.19, Git 2.55, no Docker, no WSL.
- Ollama 0.34.1 @ 127.0.0.1:11434, model qwen2.5:3b-instruct-q4_K_M.
- nanobot-ai 0.3.5 in C:\AI\Factory\.venv; config C:\AI\Factory\config.json (UTF-8 no BOM; contextWindowTokens=32768); workspace C:\AI\Factory\workspace; WebUI 127.0.0.1:8765; gateway health 127.0.0.1:18790/health.
- One-shot reply ≈150 s on 3B (CPU).
- nanobot built-in tools registered: exec, read_file, write_file, web_search (others INFERRED).
- GitHub: account contactgleamsphere-afk; repos `grok-system` (public, this) and `capability-audit-probe` (private, bootstrap artefact).
- Arena sandbox has GitHub access (PAT exp 2026-10-18) AND laptop SSH access via cloudflared tunnel (key auth, user joshp).
- Models on laptop: qwen2.5:3b (11.85 tok/s), qwen3:4b (9.19 tok/s). Both 1/5 on tool tests.
- nanobot status shows OAuth logins present for OpenAI Codex, xAI Grok, GitHub Copilot (owner's accounts; docs say OAuth providers are not valid automatic fallbacks).
- core/ tests: 19/19 pass (Python 3.13 sandbox). Not yet run on laptop Python 3.11.

## PHASE 4 (Bot Factory) — IN PROGRESS, MVP VERIFIED
- BotFactory core + CLI + laptop runner work end-to-end; bot 002 research-scout built, deployed, least-privilege tool set enforced, T1 PASS ×6; T2 (7-step web research) BLOCKED by Groq free-tier throughput: 8k TPM + **200k tokens/day per model** (measured; two of three models exhausted today). D-017 quota-aware routing and D-020 lean templates implemented & verified in logs. Gemini + OpenRouter lanes live (VERIFIED). **Bot 002 research-scout: active, VERIFIED 2/2** — first factory-made bot passing all acceptance tests, with cross-provider failover proven under real quota exhaustion. Phase 4 MVP gate: PASSED — two factory-made bots VERIFIED (002 research-scout 2/2 read-only/network; 003 code-smith 4/4 write+shell incl. security test). Next: factory-level failure tests (bad spec, missing model, tool not in registry) as unit tests; bot 001 master wiring to spawn/run factory bots; Gemini RPD measured = 20/model/project (D-024). Failover D PASS and bot 002 T2 PASS on 2026-09-20 — **routing layer Groq → Gemini → OpenRouter → local4b VALIDATED** (C+D isolated, plus live quota rotation 09-19). **Phase 4 end-to-end PROVEN: `factory_pipeline.py create` turned a plain-English objective into bot 004 changelog-writer, built, tested 4/4 and recorded VERIFIED without human editing of the bundle.** Three factory bots active (002, 003, 004). **Bot 001 master now creates bots from chat objectives via exec → factory pipeline (bot 005 csv-quality-auditor, 4/4 VERIFIED, artefacts inspected).** Four factory bots active. Monitoring live: factory_monitor.py re-tests active bots nightly (03:30 task), demotes on failure, logs MONITOR.md. **Self-improvement v0 live (D-029/D-030):** monitor demotes → factory_repair regenerates instructions via the chain → sandbox 4/4 → active; executed end-to-end on bot 004 with an injected fault, permissions provably unchanged. Nightly task now: monitor, then repair any demoted bot (run-monitor.ps1). **2026-09-21 evening — job queue + persistent worker service (D-031..D-034):** all factory work (create/test/repair/monitor) goes through `run/jobs.sqlite3`; leases, idempotency, failure-class retries, full audit trail (AUDIT.md). Master 001 queues bots from chat; the "AIFactory Worker" scheduled task executes them. Proven: crash recovery, dedup, autonomous demote→repair→promote with guard, bots 006, 007, 008 built from queued jobs — all 4/4 VERIFIED and re-confirmed by a queued monitor run (21:12). **All nine bots active & VERIFIED (001 master + 002–009)**; master has a real acceptance suite (D-046) and answers status questions from `factory.py report` (D-044/D-045). **Lane health is measured hourly (D-037)** and every chain follows it (D-040/D-042); worker is a self-restarting service that commits+pushes state after every job (D-039/D-041/D-043). **Found & fixed via the queue's own evidence:** config.json botIcon mojibake eating the model context budget (D-035).

## VERIFIED (added 2026-09-19 16:xx) — PHASE 3 COMPLETE
- Master lane = Groq (key as user env var). groq-qwen27b 4/5 agent bench (T5 passes at 275 s standalone); groq-gptoss120b 4/5. Failover on bad key and on network failure → local4b PASS. Chain: groq-qwen27b → groq-gptoss120b → groq-gptoss20b → local4b.
- Groq free tier = 8000 TPM/model: prompt slimmed (9 tools), presets ctx 8200/max 768, compaction verified firing.
- nanobot 0.3.5 patched (3 patches, reproducible via tools/patch_*.py; originals kept). Upstream-able.

## VERIFIED (added 2026-09-19 06:xx)
- Failover: broken-primary → dead remote → local4b answers (`FAILOVER_OK`, 76 s). Phase 3 failover criterion met.
- Tunnel supervisor v2 self-heals (kill test) and republishes; sandbox self-discovers URL via run/tunnel.txt.
- Laptop config live: primary local4b, fallback [ovh-gptoss20b]; keyed lanes staged in config.keyed-lanes.staged.json.

## INFERRED
- 7B/8B Q4 runs on the laptop but slowly and RAM-tight.
- nanobot on Windows runs `exec` without OS sandbox (docs state this; not observed).

## UNVERIFIED
- Full-reboot survival of the job queue is INFERRED only (SQLite WAL + leases + lease-expiry proven with killed workers; worker task starts at logon, tunnel at boot as SYSTEM). A real reboot test needs owner consent (laptop in use).
- qwen2.5:3b tool-calling reliability (Phase 0 measures it).
- qwen3:4b availability/perf on this CPU.
- What consumes ~10 GB RAM at idle.

## BLOCKED
- **Now required, not optional** (D-019): OPENROUTER_API_KEY / GEMINI_API_KEY not set (staged in config.keyed-lanes.staged.json; apply-keyed-lanes.ps1 picks them up automatically).
- Port 3000 JARVIS X service: owner decision.

## Known debt
- GitHub PAT previously exposed in a Grok chat → rotate/revoke the old one.
- `capability-audit-probe` repo + draft PR to delete.
- config/nanobot.example.json had wrong key `baseUrl` (Grok) → fixed to `apiBase`.
