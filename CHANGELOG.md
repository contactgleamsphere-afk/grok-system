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
