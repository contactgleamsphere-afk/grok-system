# CHANGELOG

## 2026-09-24 — outage recovery: liveness, sync safety, retest honesty, chain top-up, canary
- D-100 report leads with FACTORY liveness (running/stalled/idle-blocked) from worker heartbeat; master brief shows it.
- D-101 repo-sync: file lock, `merge -X ours`, never `reset --hard` (a lost registry commit re-flipped 002); slot-keyed housekeeping jobs (monitor/probe/report/tick/insight/bench) run once per slot; 23 duplicate sweep tests cancelled. `C:\AI\Factory\tools\repo-sync.ps1` is now a shim to the repo copy.
- D-102 master test run distinguishes timeouts from misses: all-timeout = inconclusive, no demotion; T6 matcher uses cron fields, not `cron=`.
- D-103 `resolve_chain` tops up to ≥2 healthy remote lanes when policy lanes are retired/blocked (bots no longer collapse to local and get falsely "repaired").
- D-104 ATTENTION: liveness first; settled paused/retired bots collapse to a count; BLOCKED reasons one line.
- D-105 probe → canary `monitor --only` for bots whose primary lane just went BLOCKED.
- D-107 Phase 5 memory MVP: factory-written bounded run memory per bot (live: 012).
- D-108/109/110 **tool capability discovery, end to end**: official MCP registry → PyPI/npm/GitHub facts → evidence rules (licence, recency, archived, deps, local-stdio-only) → throw-away sandbox handshake with secrets stripped → probation in `registry/tools.json` → capability gaps from the architect auto-enqueue discovery → owner-only `approve-tool` (persistent install, re-handshake) → explicit per-bot grant `mcp:<slug>` enforced by validate_spec and the repair boundary guard.
- D-111 declared test fixtures (text / SQLite-from-SQL) materialised before every test; D-112 `mcp_launch.py` runs servers inside the bot workspace, `rebuild` job; D-113 tests must name their fixtures.
- **Bot 026 sqlite-query-bot: first bot using a discovered MCP server — 4/4 VERIFIED, active (03:50).** On the way the security boundary fired correctly three times (two architect over-reach pauses, one repair rejected for adding shell access).
- Live evidence: 006 demoted 01:36 → auto-repaired (gpt-oss-20b, sandbox 4/4) → active 01:46; 007 re-verified 01:51; audit hash chain verified on 319 rows, tamper drill pinpoints seq 1069. Tests: 101 pass (repo + laptop).

## 2026-09-22 — discovery pipeline live, presets mirror, failover proof
- D-047 `discover` job: OpenRouter free catalogue → filter → real probe + tool loop → probation. Live run added `or-ling-30-flash-vl`, `or-nex-n25-pro` (both VERIFIED after 2 clean probes); `nex-n2.5-mini` rejected; `or-deepseek` retired from presets.
- D-048 `factory_presets.py`: nanobot `modelPresets` mirrors the registry (17 presets), pruned stale `or-deepseek` and `broken-primary`.
- D-065 create crash-resume (no duplicate bots); D-066 `--then-run` delivery.
- D-063/064 bots do real work (`run` on bots/plans, outputs chained) and the owner drives it from master chat (inbox/<name>, `job <id>`, `runs`).
- D-062 master chain auto-synced from routing policy (cross-provider). D-061 rearchitect keeps granted permissions. D-060 master re-verified not repaired.
- D-059 judge reads the full RESULT block (Rich wrapping caused false demotions); repair re-verifies before rewriting.
- D-058 bench-driven primary within daily-budget constraints.
- D-057 `factory_insight.py` weekly self-review → `proposals/<date>.md`; `insight` job kind.
- D-056 repair rounds rotate lanes.
- D-055 nightly monitor task fixed (battery/catch-up/repo script) and made scheduler-independent via the daily report job.
- D-054 allowance gate moved before build; architect can return `blocked`; `--allow` for owner grants; bot 015 (shell without grant) retired. Red-team re-run paused with nothing created.
- D-053 `factory_plan.py` + `plan` job: compound objectives → N single-purpose creates with reuse of existing bots; master 001 uses `queue plan` for pipelines. Bot template hardened against fixture fabrication.
- D-052 `spec_consistency` + `rearchitect` job: tools/tests mismatches caught at architect time; repair fails closed on them; bounded, audited re-architect from the original objective (bot 012 recovered live).
- D-051 quota-aware runner/bench/monitor: 429s never count as quality failures or trigger repair; rolling 3-run bench window; BLOCKED `custom` (OVH) presets pruned from config; master 001 `lanes` command + queue probe/discover/bench.
- D-050 `factory_bench.py` + worker `bench` kind: pinned single-lane quality scores on the 009 reference suite; `default_fallbacks()` ranked by score. Runner gained `-Lane`; RUNNER path moved to the repo copy; 57 scratch scripts archived to `C:\AI\Factory\tools\_archive`.
- D-049 bot 010 failover fixture: BLOCKED primary dropped live, 3/4 on fallback lane; documents lane-quality gap → `benchmark` job is next.
## 2026-09-18
- Phase 1 verified on laptop (owner report).
- Added core/factory: registry.py, router.py, botspec.py + 19 tests (all pass).
- Added registry/*.json (models, tools, bots) and generated *_REGISTRY.md.
- Added BUILD_STATE, DECISIONS, CHANGELOG, TEST_RESULTS, RECOVERY, COMPONENT_REGISTRY.
- Added config/laptop/SOUL.md, AGENTS.md (Master 001 identity — not yet deployed).
- Added scripts/windows/install-phase1.ps1; docs/phases/PHASE0 + PHASE2 prompts.
- Fixed config/nanobot.example.json (`baseUrl` → `apiBase`, added presets/guards).
- Grok scaffold (docs/, stack/) retained as research reference.
## 2026-09-18 (evening)
- Laptop SSH access established (cloudflared quick tunnel + key auth); persistent scheduled task added.
- Phase 0 executed: live audit, RAM profile, speed + tool-call benchmarks for qwen2.5:3b and qwen3:4b (both 1/5).
- Config hardened (see TEST_RESULTS). Master 001 identity deployed to workspace.
- qwen3:4b pulled. Registries updated with measured numbers. D-007..D-009.
## 2026-09-19
- Tunnel supervisor (auto-restart + URL publish to run/tunnel.txt) deployed as scheduled task; sleep-on-AC disabled; reconnect helper scripts/laptop-ssh.sh.
- Provider research + live probes: GitHub Models dead; OVH anonymous passes single-shot tool calls; wired ovh-gptoss20b/ovh-mistral24b/ovh-llama70b presets; production chain = ovh → local4b.
- Agent bench on ovh-gptoss20b: 0/5 (429 starvation). D-010: keyed lanes staged (Groq/OpenRouter/Gemini) via ${ENV} placeholders; apply-keyed-lanes.ps1.
- Failover test scripted; not yet passed (config validation, then tunnel drop).
## 2026-09-19 (06:xx)
- Tunnel supervisor v2: health-checked restart (zombie 'Tunnel not found' loop was the 03:25 outage), `SL` alias bug fixed, task hardened (RestartCount/StartWhenAvailable/stderr capture). Kill-test + self-discovery PASS.
- Phase 3 failover test PASSED (broken → ovh(403) → local4b, FAILOVER_OK). OVH anonymous now 403 → ovh-* marked BLOCKED; live config primary local4b.
- Added tools/bench_toolcalls.py (from laptop), tools/lastcalls.py, tools/ovhprobe.py. core tests 19/19.
## 2026-09-19 (afternoon) — Phase 3 complete
- Groq keyed Master lane live (groq-qwen27b primary; gpt-oss-120b/20b fallbacks; local4b last). Agent bench 4/5 ×3 runs; T5 passes standalone; failover A/B PASS.
- Removed groq-llama70b (404 on account). Added groq-qwen27b, groq-gptoss20b presets.
- nanobot patches: Groq strip reasoning_content; 413 → fallbackable; AIFACTORY_DISABLED_TOOLS env. Config slimmed for 8k TPM.
- New tools: groqprobe.py, groq_limits.py, session_dump.py, patch_*.py; scripts: set-primary.ps1, groq-tpm-fit.ps1, phase3-groq-failover-test.ps1. apply-keyed-lanes.ps1 made ASCII-only (PS5.1 parse bug on em-dash).
## 2026-09-19 (evening) — Phase 4 MVP
- core/factory/factory.py (BotFactory), tools/factory_cli.py, specs/002-research-scout.json, bots/002-research-scout bundle, scripts/windows/run-bot-tests.ps1. 24/24 tests. BOT_REGISTRY regenerated (002 = testing).
## 2026-09-19 (night)
- D-017 quota-aware retry patch (tools/patch_quota_retry.py); patch scripts made order-independent/idempotent; tool_use_failed now fallbackable. Measured Groq 200k TPD/model → D-019/D-020. bot 002 spec chain rotated (gpt-oss-20b first). tools/groq_tpd_probe.py.
## 2026-09-19 (late)
- D-020 template override patch + lean tool_contract in every bot bundle (BotFactory writes templates/, nanobot.patch.json exports AIFACTORY_TEMPLATE_DIR; run-bot-tests.ps1 honours it). failed_generation fallbackable. 24/24 tests.
## 2026-09-19 (evening) — lanes + bot 002 VERIFIED
- Gemini (gemini-3.6-flash, gemini-3.5-flash-lite) and OpenRouter (deepseek-v4-flash:free, qwen3.8-27b:free) lanes added to laptop config + registry/models.json with measured tool-call scores; ModelEntry gains `limits` dict.
- Bot 002 research-scout chain now spans 3 providers + local; spec instructions hardened (PyPI RSS, no repeated tool calls). Bot 002 = **active / VERIFIED 2/2**.
- run-bot-tests.ps1: keys for all lanes, `-Only`, saved transcripts. Config writes BOM-free.
- 19:5x Groq re-bench 5/5 both models (fresh TPD); isolated failover test A+B PASS; bench UA fix; failover-test.ps1 now uses scratch config.
- 20:3x Bot 003 code-smith (write_file/read_file/exec, shell:workspace) built by factory, VERIFIED 4/4 incl. workspace-escape security test. Runner escapes quotes in test prompts.
- 20:4x Gemini model discovery by live probe (7 tool-capable models, RPD=20/model/project measured); presets gemini-flash→3.7-flash, +flash38/lite31/gemma26b; chains rebuilt; cross-provider failover C PASS (Groq→Gemini→OpenRouter); D blocked by tunnel outage.
- D-023 implemented: BotFactory.with_mandatory_tests auto-injects the workspace-escape test for any spec with fs:write/shell:*; factory failure-mode tests (unknown model, unknown tool, remote-only chain gets local appended, duplicate id). 28/28.
- 2026-09-20 13:0x failover D PASS (3 remote lanes down → local4b); bot 002 T2 PASS 114 s on the new 8-lane chain; routing layer validated. Ollama pre-warm added to RECOVERY.
- Bot 003 re-verified 4/4 on new chain; BotFactory rebuild now demotes to `testing` and preserves prior verification in notes instead of silently resetting to `building`.
- 2026-09-20 14:1x **Bot 004 changelog-writer created by the factory from a plain-English objective**, 4/4 VERIFIED; factory_pipeline.py (create/test/spec); runner matches final line only (closes false-PASS hole); repo mirrored to laptop C:\AI\Factory\repo via tools/repo-sync.ps1.
- 2026-09-20 13:5x **MASTER 001 built bot 005 csv-quality-auditor from a chat objective via exec → factory pipeline** (4/4 VERIFIED, artefacts inspected). Master wrapper compacts output (8k-context safe); runner archives per-test artefacts.
- factory_monitor.py + nightly task: automatic re-verification of active bots with demotion on failure (MONITOR.md). First live run clean (004, 005).
- 2026-09-21 self-improvement v0 live: factory_repair.py (demote→regenerate instructions only→sandbox→promote) ran end-to-end on bot 004 with an injected fault; reward-hacking guard added after a live candidate echoed the security token; frozen-field guard; lane rotation on empty content.
- 2026-09-21 (evening) **Job queue + worker service (D-031..D-034):** core/factory/jobs.py (SQLite WAL, leases, idempotency, priority, failure-class retry, audit table → AUDIT.md), core/factory/guard.py (boundary guard), tools/factory_worker.py (`run|add|status|jobs|resume|cancel|release|audit`). Live proof on laptop: bot 006 json-to-markdown-table created by a queued job (4/4 VERIFIED); worker killed mid-job → lease held → released → drained by next worker; monitor 004 demoted → auto-enqueued repair → paused (logic) → prompt fixed (expected answers withheld from repair model; liveness-token exemption) → resumed → 4/4 active, fault gone. Master 001 now queues bots from chat (`factory.py queue create`); worker registered as scheduled task; nightly monitor enqueues instead of running inline. Bot 007 todo-extractor created by the service from a master-queued job. Unit tests 37/37.
- Fixed: id collision (second "006") caused by repo-sync hard-reset — D-033.
- 2026-09-21 (night) Bot 007 todo-extractor 4/4 VERIFIED after D-035 fix; bot 008 word-frequency-bot built (3/4 first run, T1 timeout) → re-test queued via D-036; worker accepts 8-char job ids; unit tests 38/38.
- 2026-09-21 (late) **Lane health + service hardening (D-037..D-043):** hourly real tool-call probe per model (or-deepseek auto-BLOCKED: withdrawn from OpenRouter free tier; Gemini flash lanes quota-cooled 15 min); chains, builder lanes and new-spec fallbacks derive from live health; runner re-resolves chains per run; Ollama auto-start; worker restarts on code change; heartbeat leases (5 min); worker commits+pushes factory state after every job (token URL, no credential helper — GCM prompt had hung it); task registered with IgnoreNew/no time limit/restart. Bot 009 line-dedupe-bot built 4/4 by the service from a queued objective with a health-derived fallback list. Unit tests 46/46.
- 2026-09-21 (23:xx) D-044 factory_report + daily STATUS.md + master `report`; D-045 lean canonical AGENTS.md (3.5 KB stale → 1.2 KB); D-046 master acceptance suite — 001 active VERIFIED 4/4. 47/47 unit tests.

- D-068: bundle integrity seal (guard.bundle_seal/bundle_drift, BotEntry.seal; run/test enforce). tools/repo-sync.ps1 on laptop is now a shim to the repo script.
- D-069: providers cerebras/nvidia/mistral; needs_owner notices in STATUS.md; probe fans out discover; retire lanes gone ≥3 days.
- D-070 master approve; D-071 keep-awake; D-072 monitor fan-out (per-bot test jobs). 72 tests.
- D-076 schedules (cron/tick), D-077 recurring-chain resilience, D-073/075 test-literal + timeout rules. 76 tests.
- D-078 demote→repair, D-079 fast-lane second worker + per-bot claim exclusion + git-state lock, D-080 event-driven lane cooldown (QUOTAHIT). Master acceptance 7 tests. 78 tests.
- D-081 lease re-adoption after sleep + fast-lane self-respawn, D-082 inconclusive repair rounds re-run, D-083 master integrity seal. 81 tests.
- D-084 discovery quota deferral, D-085 bench timeouts, D-086 outage-sweep guard, D-087 Groq ctx, D-088 daily-cap cooldown, D-089 repo-sync autostash. Bot 021. 85 tests.
- D-090 bench cooling skip, D-091 audit hash chain, D-092 builder 429 cooling. Bots 022/023 + first real plan run. 88 tests.
- D-093..D-099: shell-test gate, enqueue validation, bench-ranked builder lanes, weak-lane exclusion, objective-aware reuse, mixed-plan run fix, semantic boundary guard. Bots 024/025. 95 tests.
- 2026-09-25 D-120 tooldisc keyword fan-out + evidence ordering + policy filter + `revoke-tool`; mcp:playwright-mcp on probation; self-test gate retry.
- 2026-09-24 D-118 infra scout (registry/infra.json, docs/INFRA.md, weekly `scout`), D-119 GitHub Actions CI + laptop watchdog issue; tooldisc npm window 240 s.
- 2026-09-24 D-116/D-116b/D-117: tick + fast-worker tunnel self-heal (schtasks /Run when URL=530 and no supervisor); supervisor HTTPS-first net check (cap 300 s) and `tools\tunnel-supervisor.ps1` shim to the repo script; nightly factory canary job (`canary`, `factory_pipeline.py canary`), report flag `FACTORY CANARY FAILED`, `BotFactory.build(register=False, out_dir=)`. 110 unit tests.
