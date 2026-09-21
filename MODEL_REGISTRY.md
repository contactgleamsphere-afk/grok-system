# MODEL_REGISTRY

_generated 2026-09-19 from registry/models.json_

| id | provider | model | location | tools score | verified | limits | notes |
|---|---|---|---|---|---|---|---|
| gemini-flash | gemini | gemini-3.6-flash | remote | 1.0 | VERIFIED | {"rpd_note": "AI Studio free tier; per-model RPD low on newest models - RESEARCH-REQUIRED exact numbers"} | STAGED — needs GEMINI_API_KEY (AI Studio, no card). VERIFIED 2026-09-19: OpenAI-compat endpoint, 5/5 tool calls, 1.3-2.4s. gemini-2.5-* return 404 for new users |
| groq-gptoss120b | groq | openai/gpt-oss-120b | remote | 0.8 | VERIFIED | {} | Groq free tier. Tool call PASS 0.5s. Agent bench 4/5 (T1-T4 60-148s, T5 timeout). Same 8000 TPM cap. Fallback #1. DAILY CAP measured 2026-09-19: 200,000 tokens/ |
| groq-gptoss20b | groq | openai/gpt-oss-20b | remote | None | INFERRED | {} | Groq free tier. Tool call PASS 1.5s. Seen once returning malformed tool-call JSON (tool_use_failed). Fallback #2. Agent bench not run. DAILY CAP measured 2026-0 |
| groq-qwen27b | groq | qwen/qwen3.8-27b | remote | 0.8 | VERIFIED | {} | Groq free tier. Tool call PASS 0.4s. nanobot 5-test agent bench 4/5 twice (T5 web-research passes standalone in 275s; times out at 300s cap in bench). Free-tier |
| local3b | ollama | qwen2.5:3b-instruct-q4_K_M | local | 0.2 | VERIFIED | {} | BENCHMARKED 2026-09-18: 11.85 tok/s. Tool-call test 1/5 (Grok run 0/5). Loops on web_search/search_sessions. UNSUITABLE AS MASTER. Keep for cheap classify/summa |
| local4b | ollama | qwen3:4b | local | 0.2 | VERIFIED | {} | BENCHMARKED 2026-09-18: 9.19 tok/s. Tool-call test 1/5 (T1 pass then loop; T2-T5 timeout at 300s). UNSUITABLE AS MASTER on this CPU. Better prose than 3B. |
| ovh-gptoss20b | custom | gpt-oss-20b | remote | 0.0 | BLOCKED | {} | OVH anonymous endpoint. Single-shot tool_call PASS (1.0s). nanobot 5-test agent bench 0/5 — 429 starvation inside multi-step loops. EMERGENCY FALLBACK ONLY (D-0 |
| ovh-llama70b | custom | Meta-Llama-3_3-70B-Instruct | remote | None | BLOCKED | {} | OVH anonymous; exists in catalog; 429 on every probe attempt. 2026-09-19 06:2x: anonymous access now returns HTTP 403 "authentication failed" from BOTH laptop a |
| ovh-mistral24b | custom | Mistral-Small-3.2-24B-Instruct-2506 | remote | None | BLOCKED | {} | OVH anonymous. Single-shot tool_call PASS 1.1s. Agent bench not run (rate limits). 2026-09-19 06:2x: anonymous access now returns HTTP 403 "authentication faile |
| gemini-lite | gemini | gemini-3.5-flash-lite | remote | 1.0 | VERIFIED | {"rpd_note": "AI Studio free tier; per-model RPD low on newest models - RESEARCH-REQUIRED exact numbers"} | VERIFIED 2026-09-19: 5/5 tool calls, 0.8-1.4s. Cheapest Gemini lane. |
| or-deepseek | openrouter | deepseek/deepseek-v4-flash-0731:free | remote | 1.0 | VERIFIED | {"rpd": 50, "rpd_scope": "account-wide across all :free models"} | VERIFIED 2026-09-19: 5/5 tool calls, 2.6-4.1s. OpenRouter free tier 50 req/day shared across :free models (key endpoint reports used/limit). |
| or-qwen27b | openrouter | qwen/qwen3.8-27b:free | remote | 1.0 | VERIFIED | {"rpd": 50, "rpd_scope": "account-wide across all :free models"} | VERIFIED 2026-09-19: 2/2 tool calls but slow/variable (8-40s). Backup only. |

### 2026-09-22 discovery additions (D-047)
| lane | model | probe | notes |
|---|---|---|---|
| or-nex-n25-pro | nex-agi/nex-n2.5-pro:free | VERIFIED (1.5 s, tool loop ok) | quality gap on 010 T2 (refused file write) — tail of fallbacks until benchmarked |
| or-ling-30-flash-vl | inclusionai/ling-3.0-flash-vl:free | VERIFIED (2.8 s, tool loop ok) | vision-capable; not yet used by any bot |
| or-deepseek | — | BLOCKED, removed from nanobot presets | retired |
