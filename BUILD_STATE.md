# BUILD_STATE

_Last updated: 2026-09-25 02:40 — by Arena agent (architect/builder). Source of truth for "what actually exists"._

## Phase table (rewritten 2026-09-25 against live evidence; history below is kept as written)
| Layer / phase | Status | Evidence |
|---|---|---|
| 0–1 Foundation: nanobot 0.3.5 + Ollama + local models, laptop as host | ✅ VERIFIED | TEST_RESULTS 2026-09-18/19 |
| 2 CORE: registries (bots/models/tools/schedules/infra), bot-spec contract, boundary guard, seals, audit hash chain | ✅ VERIFIED | core/tests (117), D-031/032/068/091/099, D-123 CI verify |
| 3 MODEL router: 12 healthy lanes (groq/gemini/local; openrouter cooled), hourly probe, quota cooldown, bench-ranked chains, discovery + probation + retirement | ✅ VERIFIED live daily | STATUS.md lanes, D-042/050/058/069/095/096/115 |
| 4 TOOL layer: builtins + MCP pipeline (registry → sandbox → probation → owner approve/revoke), policy filter | ✅ VERIFIED live (mcp-sqlite tools; playwright-mcp on probation) | D-108–D-114, D-120 |
| 5 MEMORY: factory-written run memory per bot (MVP) | 🟡 MVP VERIFIED | D-107 |
| 6 Coding agent | ⬜ not started (bots have exec:workspace only; no coding-agent bot type) | — |
| 7 Browser agent | 🟡 tool discovered (`mcp:playwright-mcp`, Apache-2.0) — awaiting owner `approve-tool`, then a browser-capable bot | D-120 |
| 8 FACTORY: objective → spec → bundle → tests → register → monitor → repair/rearchitect/rebuild; plans; schedules; canary | ✅ VERIFIED live (26 bots, 24 active) | BOT_REGISTRY.md, D-065–D-117 |
| 9 Multimodal | ⬜ not started | — |
| 10 Deployment: laptop-only (scheduled tasks, tunnel supervisor, self-heal); off-laptop CI + watchdog on GitHub Actions | 🟡 single host by design; 12 free hosts inventoried for the owner | D-116/119, docs/INFRA.md |
| 11 Monitoring: nightly monitor, hourly tick, STATUS.md, liveness, outage forensics, watchdog issue | ✅ VERIFIED live | D-100/104/121, D-119 |
| 12 Self-improvement: weekly self-review → proposals → auto-actions for approved mechanisms; code changes as PRs only | ✅ stage 1 VERIFIED live; 🟡 stage 2 (PR) VERIFIED unit + real git, first live PR pending laptop return | D-057, D-122 |
| Master 001 (chat → factory) | ✅ 9/9 acceptance live 2026-09-25 00:07 (10th test added for selfpatch) | scripts/windows/run-master-tests.ps1 |

**Open owner items (nothing blocks the factory):** approve `mcp:playwright-mcp`; keep the laptop on mains (two battery/power outages 24–25 Sep); optional free signups listed in docs/INFRA.md (Cerebras, NVIDIA, Mistral first).

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

## 2026-09-22 — factory loop closed, hardened (D-065..D-069) — VERIFIED
- 18 bots in registry (17 active). One chat message → build → verify → auto-run on owner data → result file, no human (D-066, bot 018 totals.csv).
- Crash mid-create resumes at the test stage without duplicate bots (D-065). Durable audit trail `audit/YYYY-MM.jsonl` in git, 421+ events (D-067).
- Bundle integrity: sealed bot files hashed in the registry; tampered bundles cannot run or earn "active" (D-068, live-tested on bot 018).
- Free-first scout covers OpenRouter + Cerebras + NVIDIA + Mistral; missing keys → `ACTION REQUIRED (owner)` lines in STATUS.md with signup URLs; lanes gone ≥3 days retire automatically (D-069). or-deepseek retires ~2026-09-25.
- Owner-grant path exercised live via master chat (D-070): blocked → asked → approved → bot 020 workspace-file-lister 3/3 active.
- Worker: keep-awake during jobs (D-071), monitor fan-out to per-bot test jobs (D-072), reward-hack→rearchitect escalation + phrase-literal test rejection (D-073), self-test gate with pytest on the laptop (D-074, 74/74 on both Py3.13 and laptop Py3.11), timeouts inconclusive (D-075).
- 20 bots in registry. Legacy phase-1..3 scripts archived under scripts/windows/archive/.
- Schedules (D-076): cron → hourly tick → run jobs, idempotent per slot; live-proven twice on bot 018; daily 07:00 schedule active.
- Recurring chains self-heal (D-077): probe chains its successor first; worker re-seeds probe/tick/report on start. Root cause of today's timeout wave (stale lane health after the probe chain died 21 Sep) fixed; hourly probe live again (job 322482f0 → 60d56672).
- D-078: any test that demotes an ACTIVE bot queues a repair (audit `bot.demoted`).
- D-079: two workers — `svc-` (all kinds) + `fast-` (--fast-lane: run/test/tick/probe/report/discover); `JobStore.claim` never hands two workers the same bot; git state commits serialized by run/git-state.lock. Master 001 acceptance now 7 tests, 7/7 live.
- D-080: a 429 seen during any test/run cools that lane immediately (`QUOTAHIT` → `mark_quota`, provider retry-after honoured) instead of waiting for the hourly probe.
- D-081: laptop sleep mid-job is safe — `heartbeat()` re-adopts an expired lease (`job.readopted`) or discards an orphaned result; fast-lane worker respawns itself on code change (`--respawn`). Power plan: standby 0 / lid does nothing on AC.
- D-082: quota/timeout-bound sandbox scores in repair are inconclusive → same candidate re-run once after lanes cooled.
- D-083: master 001 sealed (AGENTS.md, tools/factory.py, config tools.exec); `test 001` refuses on drift; wire script reseals. Live: tamper detected → restore → drift [].
- D-084 discovery defers on account quota (13 verdicts un-rejected); D-085 bench timeouts = availability; D-086 all-remote-error sweep = local outage (health untouched, re-probe 10 min); D-087 Groq preset ctx 16384 (local governor was pre-empting fallback); D-088 daily-cap 429 → ≥1 h cooldown that survives probe ok; D-089 repo-sync autostash + selftest.json untracked (no more hard-reset on dirty tree).
- Bot 021 email-line-counter created from master chat (`queue create`) → 4/4 VERIFIED in 4 min while the slow worker held 004's repair (D-079 live proof). 004 repaired → active (D-080/082 path: round 1 on gpt-oss-20b 4/4). 20/21 active (010 paused, 015 retired).
- **Full autonomous loop proven on real data (23:00–23:17):** chat objective → plan 197bb3e5 (2 steps) → bots 022 csv-refund-filter + 023 refund-summarizer built, tested 4/4, VERIFIED → plan run on a real orders.csv → refunded.csv (3 correct rows) + summary.txt `39.5` (correct). 22/23 active.
- D-090 bench skips cooling/BLOCKED lanes; D-091 audit JSONL hash chain (`audit-verify`); D-092 builder-side 429s cool lanes.
- D-093 shell-needing tests rejected at architect time unless exec+shell:workspace granted (bot 019 class closed; bot 024 built under explicit grant, 3/3). D-094 empty/flag objectives refused at enqueue.
- D-095 builder lanes (architect/planner/repair) ranked by measured bench quality; D-096 `is_weak()` (<50% over ≥8 tests) auto-excluded from new chains, reversible.
- D-097 planner reuse against original objective: 3-stage plan 593061c9 reused 022+023, built only 025; D-098 mixed plan run fixed (KeyError) → real run produced refunded.csv/summary.txt/summary_upper.txt = 39.5.
- D-099 repair + architect reject *semantic* boundary expansion in instructions (shell/net/paths/credentials/model choice) — 0 false positives on 23 live specs. D-087 proven live after Groq TPD reset.
- 25 bots (010 paused, 015 retired). **25 h laptop outage survived unattended** (schedule caught up once, no false lane damage, nightly cycle ran). Post-mortem fixes D-100 (report liveness), D-101 (git sync can never discard state; slot jobs once), D-102 (master timeouts inconclusive), D-103 (chain top-up when policy lanes retired), D-104 (attention signal/noise), D-105 (canary monitor on BLOCKED primary). 101 unit tests (repo + laptop). **Repair loop proven live 2026-09-24 without human input: 006, 007, 014 demoted→repaired→active (014 needed a D-056 lane rotation); master 001 retested 7/7.** Tunnel rotation self-healed. **Tool/MCP capability discovery pipeline live (D-108..D-113): bot 026 is the first bot running an owner-approved, sandbox-verified MCP server (4/4 VERIFIED).** 107 unit tests.

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
- (D-019 resolved 2026-09-20: OPENROUTER/GEMINI keys set as User env; lanes live.)
- Port 3000 JARVIS X service: owner decision.

## Known debt
- GitHub PAT previously exposed in a Grok chat → rotate/revoke the old one.
- `capability-audit-probe` repo + draft PR to delete.
- config/nanobot.example.json had wrong key `baseUrl` (Grok) → fixed to `apiBase`.

## Latest (2026-09-22)
- D-047/D-048 live; D-049 failover proven (bot 010). Next: `benchmark` job kind for lane quality_score.
