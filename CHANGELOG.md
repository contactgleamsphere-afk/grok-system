# CHANGELOG
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
