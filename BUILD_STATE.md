# BUILD_STATE

_Last updated: 2026-09-18 — by Arena agent (architect/builder). Source of truth for "what actually exists"._

## Phase table
| Phase | Name | Status | Evidence |
|---|---|---|---|
| 0 | Discovery, baseline, tool-call test | ✅ DONE (Arena over SSH) | TEST_RESULTS.md, benchmarks/2026-09-18 |
| 1 | Foundation: nanobot 0.3.5 + Ollama + qwen2.5:3b | ✅ VERIFIED | owner report 2026-09-18: `PHASE1_OK`, WebUI 127.0.0.1:8765 |
| 2 | Core: registries, router, bot-spec contract, Master identity, security hardening | ✅ identity deployed + config hardened on laptop; core code tested in sandbox | config/laptop/config.current.json |
| 3 | Model router: remote free-tier Master lane + local cheap lanes | **NEXT — BLOCKED on owner signups (see below)** | D-007 |
| 4 | Tool layer / MCP | pending | |
| 5 | Memory | pending | |
| 6 | Coding agent | pending | |
| 7 | Browser agent | pending | |
| 8 | Bot Factory (spec → running bot) | pending | botspec validator exists |
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

## INFERRED
- 7B/8B Q4 runs on the laptop but slowly and RAM-tight.
- nanobot on Windows runs `exec` without OS sandbox (docs state this; not observed).

## UNVERIFIED
- qwen2.5:3b tool-calling reliability (Phase 0 measures it).
- qwen3:4b availability/perf on this CPU.
- What consumes ~10 GB RAM at idle.

## BLOCKED
- Phase 3 Master lane: needs owner to create free-tier API key(s) — human signup, cannot be automated legitimately.
- Port 3000 JARVIS X service: owner decision.

## Known debt
- GitHub PAT previously exposed in a Grok chat → rotate/revoke the old one.
- `capability-audit-probe` repo + draft PR to delete.
- config/nanobot.example.json had wrong key `baseUrl` (Grok) → fixed to `apiBase`.
