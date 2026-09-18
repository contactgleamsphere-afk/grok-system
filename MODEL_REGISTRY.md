<!-- generated from registry/models.json by core/factory/registry.py — edit the JSON, not this file -->
# models

| id | provider | model | capabilities | context_window | location | cost_per_1k | tokens_per_sec | ram_gb | tool_call_score | verified | notes | updated |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| local3b | ollama | qwen2.5:3b-instruct-q4_K_M | ['chat', 'tools'] | 32768 | local | 0.0 | None | 2.0 | None | VERIFIED | Phase 1: one-shot reply OK (~150s). contextWindowTokens must be 32768 (8192 -> ContextWindowExceededError). tok/s + tool-call score: PENDING Phase 0 benchmark. | 2026-09-18T17:28:28+00:00 |
| qwen3-4b-candidate | ollama | qwen3:4b | ['chat', 'tools', 'code'] | 32768 | local | 0.0 | None | None | None | UNVERIFIED | Candidate for Phase 0 comparison. Not pulled yet. | 2026-09-18T17:28:28+00:00 |
