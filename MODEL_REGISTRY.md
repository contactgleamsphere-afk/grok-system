<!-- generated from registry/models.json — edit the JSON, not this file -->
# models

| id | provider | model | capabilities | context_window | location | cost_per_1k | tokens_per_sec | ram_gb | tool_call_score | verified | notes | updated |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| local3b | ollama | qwen2.5:3b-instruct-q4_K_M | ['chat', 'summarise', 'classify'] | 32768 | local | 0.0 | 11.85 | 2.0 | 0.2 | VERIFIED | BENCHMARKED 2026-09-18: 11.85 tok/s. Tool-call test 1/5 (Grok run 0/5). Loops on web_search/search_sessions. UNSUITABLE AS MASTER. Keep for cheap classify/summarise only. | 2026-09-18T20:41:15+00:00 |
| local4b | ollama | qwen3:4b | ['chat', 'summarise', 'classify', 'code-small'] | 32768 | local | 0.0 | 9.19 | 3.0 | 0.2 | VERIFIED | BENCHMARKED 2026-09-18: 9.19 tok/s. Tool-call test 1/5 (T1 pass then loop; T2-T5 timeout at 300s). UNSUITABLE AS MASTER on this CPU. Better prose than 3B. | 2026-09-18T20:41:15+00:00 |
