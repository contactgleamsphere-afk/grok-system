# Free model-provider verification — 2026-09-19 (live probes from Arena sandbox + laptop)
Probe = OpenAI-compatible chat.completions with one `read_file` tool; PASS = model returned a correct `tool_calls` entry.

| Provider | Auth | Result | Notes |
|---|---|---|---|
| GitHub Models | GitHub PAT | **DEAD** — HTTP 410 `github_models_retirement_brownout` | being retired; remove from all plans |
| OVHcloud AI Endpoints (anonymous) | none | **PASS** `gpt-oss-20b` 1.0 s, `Mistral-Small-3.2-24B` 1.1 s; `Llama-3.3-70B`, `Qwen3.6-27B`, `Qwen3-Coder-30B-A3B` exist but 429 under burst | 24-model catalog incl. whisper, embeddings, SDXL. Per-IP/min anonymous quota is tight: first call from a fresh IP often 429s; sustained agent loops starve. Keyed OVH (free signup) lifts limits. |
| Pollinations | none | 502 on all models | down at probe time |
| Kilo Gateway | none | 401 PAID_MODEL_AUTH_REQUIRED | sign-in required |
| LLM7 | optional token | 401 Missing API key (keyless routes withdrawn); one 429 | not viable keyless |
| Groq | free key, no card | not probed (needs key) | 30 RPM / 14.4k RPD; llama-3.3-70b, gpt-oss-120b, qwen3-32b — tool calling documented |
| OpenRouter | free key, no card | not probed (needs key) | `openrouter/free` auto-route; 50 req/day keyless-credit tier |
| Google AI Studio | free key, no card | not probed (needs key) | gemini-2.5-flash; tools+vision; low RPD on newest models |
| Cerebras / NVIDIA NIM / Mistral / Cloudflare Workers AI | free key | not probed | candidates for router breadth |

## nanobot agent benchmark (5 tool tests, 300 s cap) — laptop
| preset | model | score | failure mode |
|---|---|---|---|
| local3b | qwen2.5:3b | 1/5 | tool loop |
| local4b | qwen3:4b | 1/5 | tool loop |
| ovh-gptoss20b | gpt-oss-20b via OVH anon | **0/5** | every test timed out mid-reasoning; output shows the model reasoning in text ("the assistant should output two tool calls") instead of emitting tool_calls — consistent with OVH 429s inside nanobot's multi-step loop plus gpt-oss reasoning-channel handling; llm_calls table logged NO agent calls (only `dream`), i.e. requests never completed |

## Decision D-010
Anonymous OVH is a valid **emergency fallback**, not a Master lane: rate limits break agentic loops. The Master lane requires a keyed free tier (Groq primary, OpenRouter + Gemini breadth). Keys are owner-signup only; they will be entered on the laptop via environment variables (`GROQ_API_KEY`, `OPENROUTER_API_KEY`, `GEMINI_API_KEY`) — never in config, never in chat. Staged preset block: `config.keyed-lanes.staged.json` (laptop) / `config/laptop/keyed-lanes.staged.json` (repo).
