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
