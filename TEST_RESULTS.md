# TEST_RESULTS
## 2026-09-18 — core unit tests (Arena sandbox, Python 3.13, pytest)
`python -m pytest core/tests -q` → **19 passed**
Covers: registry round-trip/validation/corrupt-file/atomic-write; router capability+context filtering, local-first ranking, fallback on 429, cooldown + recovery, non-retryable errors do not fall through, all-fail trail, preferred model; bot-spec valid/high-risk-permission/system-shell-block/unknown-model-tool/bad-cron/malformed input.
Found & fixed: failure-count ranking bug (D-004).
Not yet run on laptop Python 3.11 — Phase 2 deploy step.

## 2026-09-18 — Phase 1 (laptop, owner report)
`nanobot agent -m "Reply with exactly: PHASE1_OK"` → `PHASE1_OK` (~150 s). WebUI up. Ollama localhost-only.

## 2026-09-18 — Phase 0 laptop benchmarks (run by Arena agent over SSH)
Raw JSON: benchmarks/2026-09-18/
| model | eval tok/s | prompt tok/s | RAM delta | tool-call score (5 tests, 300 s cap) |
|---|---|---|---|---|
| qwen2.5:3b-instruct-q4_K_M | 11.85 | 30.6 | ~2.0 GB | **1/5** — T1 correct but then looped; T2/T3 timeout loops; T4 wrote a generic script instead of acting; T5 wrong |
| qwen3:4b | 9.19 | 22.1 | ~3.0 GB | **1/5** — T1 correct then looped; T2–T5 all timeout loops (write missing_file.txt ×N, run_cli_app ×N, search "END OF FILE" ×N) |
Grok's earlier run of the same tests on 3B (maxToolIterations=200): 0/5, T2 ran 2032 s.
Failure pattern is identical across both: model completes or nearly completes the task, then cannot emit a final answer and loops re-invoking tools. This is a small-model agentic-protocol failure, not a nanobot bug.
Conclusion (D-007): no local model on this hardware can act as MASTER. Local models = cheap lanes only.

## 2026-09-18 — Security hardening applied (config sha 6105B7… → 69445C…)
restrictToWorkspace=true; maxToolIterations 200→25; exec.timeout 60→120 with 12 denyPatterns (format/diskpart/recursive delete of system paths/reg/netsh/shutdown/net user/iex-from-http); websocket allowFrom * → 127.0.0.1,::1; identity SOUL.md/AGENTS.md deployed; phase0_test.txt removed. Backup: C:\AI\Factory\config.json.bak-*.

## 2026-09-19 — Phase 3 provider probes + agent bench
See docs/FREE_PROVIDERS_2026-09-19.md. Key numbers: OVH gpt-oss-20b single-shot tool_call PASS 1.0 s; nanobot agent bench on same 0/5 (429 starvation). GitHub Models 410. Failover test (broken-primary → ovh → local4b) was staged in `scripts/windows/phase3-failover-test.ps1`; first attempt aborted by nanobot config validation (env-var placeholders for unset keys are hard errors — fixed by staging keyed lanes separately); second attempt interrupted by tunnel drop. (superseded — see 06:2x entry below.)

## 2026-09-19 — Tunnel
Supervisor deployed and verified: published `https://cleanup-operational-rim-precise.trycloudflare.com` to run/tunnel.txt at 03:07:33; SSH reconnected through it. Then the tunnel dropped at ~03:2x and did not republish for >3 min → supervisor restart path or laptop sleep/network is suspect. Sleep-on-AC disabled via powercfg during this session.

## 2026-09-19 06:2x — Phase 3 failover test PASSED (laptop, nanobot 0.3.5)
Script: `scripts/windows/phase3-failover-test.ps1` (laptop `tools\p6.ps1`). Config: primary preset `broken-primary` (model `does-not-exist-xyz`), fallbackModels `[ovh-gptoss20b, local4b]`. Command: `nanobot agent -m "Reply with exactly: FAILOVER_OK"`.
- Run 1: output ended `FAILOVER_OK` (qwen3 thinking visible above it). PASS.
- Run 2: elapsed **76 s**, output `FAILOVER_OK`. PASS.
- Which lane answered: Ollama server.log shows `POST /v1/chat/completions` 06:21:02 → 500 (1m29s), 06:22:46 → 200 (1m42s), 06:24:18 → 200 (1m08s); `ollama ps` = qwen3:4b loaded. So the chain went broken-primary → ovh-gptoss20b (403, see below) → **local4b answered**. VERIFIED: failover across 2 dead lanes to local works.
- Note: the first Ollama 500 after 1m29s = cold-load timeout on the first run; nanobot retried and succeeded.
- OVH anonymous: `tools/ovhprobe.py` from laptop AND sandbox → **HTTP 403 "Forbidden: authentication failed"** for gpt-oss-20b and Mistral-Small-3.2 (0.3–0.6 s). Keyless OVH is gone (was 429 at 03:xx, now 403). ovh-* presets marked BLOCKED.
- Production config after test: primary `local4b`, fallbackModels `[ovh-gptoss20b]` (kept as canary; harmless because failover is proven). Backup `config.json.bak-p7-*`.
- `nanobot status` on that config: `Model: qwen3:4b (preset: local4b)`, no validation errors.

## 2026-09-19 06:1x — Tunnel supervisor v2 (root cause + fix, verified)
Root cause of the 03:25 drop: laptop lost network at 03:45–06:00 (NetworkProfile events); cloudflared did NOT exit — it looped `ERR Register tunnel error ... "Unauthorized: Tunnel not found"` forever (quick tunnels are not resumable). v1 supervisor only restarted on process exit → zombie tunnel, no republish.
Second bug found while fixing: v2 logger was named `SL`, which is PowerShell's built-in alias for `Set-Location` → every log call silently did nothing (`supervisor.err` captured "Cannot find drive 'url https'"). Renamed to `Write-SupLog`.
v2 restarts on: ≥3 "Tunnel not found", no "Registered tunnel connection" within 90 s, no URL within 60 s, 3 consecutive external probes returning 530/no-route (every 60 s), or process exit; waits for `Test-Connection 1.1.1.1` before relaunching; kills only its own orphans (never the owner's manual cloudflared); task now has RestartCount 999/1 min, StartWhenAvailable, no time limit; stderr captured to `run\supervisor.err`.
Verification: kill-test `Stop-Process cloudflared` at 06:18:15 → `restart: cloudflared exited` → new URL `joined-eliminate-spirit-boc` 06:18:32 → published to GitHub 06:18:33 (attempt 1) → `~/bin/laptop hostname` from sandbox discovered the new URL and returned `LAPTOP-LRE6PSA8` with no human input. PASS.

## 2026-09-19 — core unit tests re-run (sandbox)
`pytest core/tests -q` → 19 passed in 0.08 s.
