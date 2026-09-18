# TEST_RESULTS
## 2026-09-18 — core unit tests (Arena sandbox, Python 3.13, pytest)
`python -m pytest core/tests -q` → **19 passed**
Covers: registry round-trip/validation/corrupt-file/atomic-write; router capability+context filtering, local-first ranking, fallback on 429, cooldown + recovery, non-retryable errors do not fall through, all-fail trail, preferred model; bot-spec valid/high-risk-permission/system-shell-block/unknown-model-tool/bad-cron/malformed input.
Found & fixed: failure-count ranking bug (D-004).
Not yet run on laptop Python 3.11 — Phase 2 deploy step.

## 2026-09-18 — Phase 1 (laptop, owner report)
`nanobot agent -m "Reply with exactly: PHASE1_OK"` → `PHASE1_OK` (~150 s). WebUI up. Ollama localhost-only.
