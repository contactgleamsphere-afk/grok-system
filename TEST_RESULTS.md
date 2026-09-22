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

## 2026-09-19 14:00–16:10 — Phase 3 Groq Master lane (laptop, nanobot 0.3.5)
Key present as user env var only (never in chat/git). Direct probes (`tools/groqprobe.py`, `tools/groq_limits.py`):
- Groq blocks Python-urllib default User-Agent with Cloudflare 1010 (403) — any UA string fixes it. nanobot's client is unaffected.
- `llama-3.3-70b-versatile` **does not exist** on this account (404) → preset removed. Available tool-capable: `qwen/qwen3.8-27b`, `openai/gpt-oss-120b`, `openai/gpt-oss-20b`. `groq/compound*` reject tools.
- Free-tier limits from response headers: **1000 RPD, 8000 TPM** per model (compound: 250 RPD / 70k TPM).
- Single-shot tool_call: qwen3.8-27b 0.4 s, gpt-oss-120b 0.5 s, gpt-oss-20b 1.5 s — all PASS.

Bugs found and fixed to make agent loops work (all patches are files in `tools/patch_*.py`, originals kept as `*.orig-0.3.5`):
1. Groq 400 `property 'reasoning_content' is unsupported` on assistant history → `patch_groq_reasoning.py` sets `strip_history_reasoning_content=True` on Groq's ProviderSpec (nanobot already had the flag for Mistral).
2. Groq reports TPM overflow as HTTP **413 / invalid_request_error / rate_limit_exceeded**; nanobot classified that as non-fallbackable and the turn died → `patch_fallback_413.py` treats 413/`rate_limit` as fallbackable.
3. Prompt too fat for 8k TPM (23 tools ≈ 3.2k tokens + 3.2k system prompt + tool results): `patch_disabled_tools.py` adds env `AIFACTORY_DISABLED_TOOLS` (set to message,apply_patch,exec_session,list_exec_sessions,cron,create_goal,update_goal,my,spawn,list_sessions,read_session,search_sessions,send_session_message,run_cli_app → 9 tools registered); cliApps disabled; `useJinaReader=false`; `maxToolResultChars=2500`; Groq presets `contextWindowTokens=8200`, `maxTokens=768` so nanobot's own compaction fires before Groq 413s (7000 was too small: ContextWindowExceededError 5252/4952). `reasoningEffort=low`.
4. bench.py now uses a fresh `-s bench-*` session per test and `--classic` (the shared CLI session carried 70 stale messages incl. qwen3 reasoning_content).

Agent bench (`tools/bench_toolcalls.py`, 300 s cap/test):
| preset | T1 | T2 | T3 | T4 | T5 | score |
|---|---|---|---|---|---|---|
| groq-gptoss120b (before fixes) | ✗ 12s err | ✓ | ✗ | ✗ | ✗ | 1/5 |
| groq-gptoss120b (after) | ✓ 60s | ✓ 85s | ✓ 69s | ✓ 148s | ✗ timeout | **4/5** |
| groq-qwen27b run 1 | ✓ 55s | ✓ 48s | ✓ 96s | ✓ 152s | ✗ timeout | **4/5** |
| groq-qwen27b run 2 (final config) | ✓ 133s | ✓ 98s | ✓ 98s | ✓ 200s | ✗ timeout | **4/5** |
| local4b (Phase 0) | | | | | | 1/5 |
T5 standalone (final config): **PASS `0.3.5` in 275 s** — the run shows compaction ("Memory archive … requesting checkpoint") and mid-task failover qwen27b→gpt-oss-120b on 413 working as designed. Bottleneck is Groq's 8000 TPM: most wall time is `retrying in 41–56s` waits. Verdict: Groq lane = 4/5 with T5 passing outside the cap ⇒ Master lane VERIFIED but throughput-limited.

Failover (`scripts/windows/phase3-groq-failover-test.ps1`):
- A: invalid Groq key → `Primary failed: Invalid API Key` → `Fallback qwen3:4b succeeded` → `FAILOVER_OK` (159 s). PASS
- B: Groq apiBase unreachable → 4 connection retries → local4b → `FAILOVER_OK` (136 s). PASS
- Restored chain sanity: `GROQ_OK` in 12 s. PASS
Live config now: primary **groq-qwen27b**, fallbacks [groq-gptoss120b, groq-gptoss20b, local4b]. Backups `config.json.bak-keyed-*`, `.bak-p7-*`.

## 2026-09-19 16:1x–16:5x — Phase 4 Bot Factory MVP (sandbox + laptop)
- `core/factory/factory.py` BotFactory: spec → validate → resolve chain (drops BLOCKED, appends best local) → bundle (SOUL/AGENTS/bot.json/nanobot.patch.json/TESTS/RECOVERY/memory) → registry upsert; least-privilege tool set derived from permissions (`AIFACTORY_DISABLED_TOOLS`). Unit tests: **24/24** (5 new: bundle contents, invalid/duplicate rejection, BLOCKED-chain handling, status flip, test parsing).
- First factory bot **002 research-scout** built from `specs/002-research-scout.json`, deployed to `C:\AI\Factory\bots\002-research-scout`, run by `scripts/windows/run-bot-tests.ps1` (per-bot config in `run\botcfg\`, because nanobot refuses a config inside the workspace — found and fixed). nanobot registered exactly the 3 allowed tools (`read_file, web_fetch, web_search`) — least privilege VERIFIED.
- Results: **T1 `SCOUT_OK` PASS 7–12 s** (×3 runs). **T2 (multi-step web research) FAIL/TIMEOUT** at 400–480 s in 3 runs. Root cause measured with `tools/groq_limits2.py`: Groq free tier = 8000 TPM per model, reset ~100 ms–1 s; each agent step ≈ 4.5k tokens ⇒ 2 steps/min; nanobot treats the 429 as fallbackable and immediately drops to local qwen3:4b (1/5 tool score) instead of waiting the sub-second reset. Registry: bot 002 = `testing` / UNVERIFIED (1/2). Honest state: factory pipeline VERIFIED end-to-end; bot's research capability BLOCKED on router policy + TPM.
- Next fix (D-017): quota-aware routing — on 429 with `x-ratelimit-reset-tokens` < 10 s, wait and retry the same lane (and rotate to the *other Groq model*, which has its own 8k TPM bucket) before falling to local. Also: cut per-step tokens (identity prompt + tool contract ≈ 3.2k) further for small-TPM lanes.

## 2026-09-19 17:0x–17:4x — D-017 quota-aware routing + bot 002 re-test
- `tools/patch_quota_retry.py` (in-place, idempotent; `patch_fallback_413.py` also made idempotent and extended so Groq `tool_use_failed` / "Tool call validation failed" is fallbackable — seen once from gpt-oss-20b hallucinating a `search_file` tool). Patch-order bug found and fixed: the first version of the quota patch reverted to `.orig` and silently dropped the 413 patch.
- Behaviour: 429/413 with reset < 20 s → wait + retry same lane (max 3); "per day" / long reset → rotate lane immediately.
- **New hard fact (measured with `tools/groq_tpd_probe.py`)**: Groq free tier also has **200,000 tokens/day per model (TPD)**. After today's benchmarks: qwen3.8-27b 196k used (reset ~4–12 min rolling), gpt-oss-120b 198k, gpt-oss-20b still available. Error body: `on tokens per day (TPD): Limit 200000, Used 196350 … try again in 4m5s`.
- Bot 002 re-tests (chain rotated to gpt-oss-20b first): T1 PASS 7 s (×3 more). T2: run A ended in 11 s with Groq 400 `tool_use_failed` (fixed above); run B 406 s log shows the loop working correctly — web_search → read_file → web_fetch … 8 tool calls, compaction fired — but every step waits 21–40 s on 8k TPM and the 480 s cap is hit. **T2 = FAIL (throughput), not a logic failure.**
- Registry: bot 002 stays `testing`, 1/2. Not marked active.
- Budget reality: 200k TPD ÷ ~4.5k tokens/step ≈ 45 agent steps per model per day ≈ 3 Groq models ≈ 135 steps/day. Benchmarks alone consume a day. This is the binding constraint on the whole factory, not code.

## 2026-09-19 17:4x — D-020 prompt diet + final bot 002 attempt (quota exhausted)
- `tools/patch_template_override.py` (D-020): `AIFACTORY_TEMPLATE_DIR` searched before nanobot's templates. Factory bundles now ship `templates/agent/tool_contract.md` (822 chars vs 5448 — the stock contract documents 15 tools factory bots don't have). Verified in-process: loader searchpath = [bot templates, nanobot templates]; rendered contract 822 chars. Per-step saving ≈ 1.1k tokens.
- `patch_fallback_413.py` extended again: Groq `failed_generation` / "Parsing failed. The model generated output…" (gpt-oss-20b emitting malformed tool JSON) is now fallbackable — it killed a run in 30 s.
- Final T2 attempt 17:49: log shows **D-017 working exactly as designed** — `quota-aware retry: 'qwen/qwen3.8-27b' daily quota exhausted, rotating lane` → `'openai/gpt-oss-120b' daily quota exhausted, rotating lane` → local qwen3:4b → timeout. gpt-oss-20b (the last Groq model with budget) then hit its own 200k TPD during the run. **All three Groq models are TPD-exhausted for the rolling day.** No further laptop LLM runs today (D-019).
- Bot 002 remains `testing` 1/2. Not a code failure: the pipeline, least-privilege, template override, lane rotation and failover are all VERIFIED in logs; only remote token budget is missing.

## 2026-09-19 18:00–19:00 — Lanes set (Gemini + OpenRouter) → bot 002 VERIFIED 2/2
**Lane probes (laptop, tools/lanes.py, lanes2.py; echo tool-call test):**
| lane | model | tool calls | latency | notes |
|---|---|---|---|---|
| gemini-flash | gemini-3.6-flash | 5/5 | 1.3–2.4 s | gemini-2.5-* → 404 "no longer available to new users" |
| gemini-lite | gemini-3.5-flash-lite | 5/5 | 0.8–1.4 s | |
| or-deepseek | deepseek/deepseek-v4-flash-0731:free | 5/5 | 2.6–4.1 s | OpenRouter free = 50 req/day account-wide |
| or-qwen27b | qwen/qwen3.8-27b:free | 2/2 | 8–40 s | backup only |
| (rejected) | thinkingmachines/inkling*:free | 403 | | "agentic harnesses only" |
| (rejected) | nvidia/nemotron-3.5-lightning:free, nex-n2.5-mini:free | timeout 60 s | | |
| (rejected) | google/gemma-4-26b-a4b-it:free | 429 upstream | | |
| groq llama-3.3-70b-versatile | | model_not_found | | does not exist on this account (4th confirmation) |

`nanobot status --config C:\AI\Factory\config.json`: Config ✓, Gemini ✓, OpenRouter ✓, Custom ✓, Ollama ✓ (Groq key via ${GROQ_API_KEY}). Bug fixed on the way: PS5 `Set-Content -Encoding UTF8` writes a BOM → nanobot "Invalid configuration"; now written with UTF8Encoding($false).

**Bot 002 runs (each = one run, run-bot-tests.ps1):**
1. 18:0x chain still Groq-only (runner rebuilt cfg from bundle) → T2 TIMEOUT. Fix: chain must live in the spec, not a hand-edited botcfg.
2. 18:2x chain groq>gemini>or>gemini-lite>groq>local → T2 **completed in 257 s** (first time) but answered 0.2.1: pypi.org/pypi/…/json (1557 chars limit) truncated before `info.version`; bot looped fetch→read on the same URL until nanobot's repeated-lookup guard blocked it.
3. Fix (spec-level, factory rebuild): instruct PyPI lookups via `https://pypi.org/rss/project/<name>/releases.xml`, never repeat identical tool calls, read truncated result file once. maxToolResultChars 1500→4000 in live config.
4. 18:59 **T1 PASS 29 s, T2 PASS 84 s → SCORE 2/2. Bot 002 status → active, VERIFIED.**
   At run time Groq gpt-oss-20b TPD = 198,433/200,000 (429) and OpenRouter free = 66/50 used → the passing run was executed by the **Gemini lanes via failover**, i.e. cross-provider failover VERIFIED end-to-end under real quota exhaustion.

Runner upgrades: exports GEMINI/OPENROUTER keys into the job, `-Only N` to run one test, per-test transcripts saved to `C:\AI\Factory\run\logs\bot<id>-t<n>-<hhmmss>.log`.

## 2026-09-19 19:40–19:55 — Groq re-bench (fresh TPD) + isolated failover test
- Groq TPD reset confirmed (rl.py OK on gpt-oss-120b / gpt-oss-20b). `llama-3.3-70b-versatile` → model_not_found (5th confirmation; not on this account).
- `tools/groq_bench5.py` (5× echo tool-call, exact-arg check): **gpt-oss-120b 5/5, 0.46–0.75 s; gpt-oss-20b 5/5, 0.29–1.63 s**. Gotcha found+fixed: Groq edge returns 403 for Python's default urllib User-Agent → bench sets `User-Agent: aifactory-bench/1.0`.
- `scripts/windows/failover-test.ps1` (runs on a scratch copy `run\failover-test.json`, production config untouched):
  - A bad Groq key → `Primary 'qwen/qwen3.8-27b' failed: Invalid API Key` → `Fallback 'qwen3:4b' succeeded` → `FAILOVER_OK` (201 s, local cold start).
  - B Groq unreachable (apiBase 127.0.0.1:9) → 4 retries → fallback local4b → `FAILOVER_OK` (152 s).
  Both PASS. local4b latency (2–3 min/turn incl. model load) is why local is last-resort only.

## 2026-09-19 20:0x–20:3x — Bot 003 code-smith (first write+shell bot) VERIFIED 4/4
Spec `specs/003-code-smith.json`: tools write_file/read_file/exec; permissions fs:read, fs:write, shell:workspace; chain groq-gptoss120b > gemini-flash > groq-gptoss20b > or-deepseek > local4b. New unit test: spec with `exec` but no `shell:workspace` is rejected; `shell:system` always rejected (25/25 pass).
Runs:
1. 3 tests → 2/3. T3 failed in 3 s because the test prompt contained double quotes that PowerShell split into extra nanobot args (harness bug, not bot). Fixed: runner escapes quotes; T3 reworded to `python --version`.
2. T3 alone → PASS 60 s.
3. Added T4 security test (attempt to read C:\Windows\win.ini via read_file **and** exec). Full run: **T1 34 s, T2 86 s (233168), T3 57 s, T4 58 s CONFINED → 4/4.** Transcript shows both escape attempts were actually issued and both refused by nanobot's workspace guard ("outside the workspace" / "blocked by the safety guard") — a real block, not a model refusal.
Bot 003 → active, VERIFIED. Caveat stands (SECURITY.md): restrictToWorkspace is an application guard, not an OS sandbox, on Windows.

## 2026-09-19 20:0x–20:4x — "LANES SET": both providers together, isolated cross-provider failover
1. Keys present locally (lengths only, never printed): GROQ 56, GEMINI 53, OPENROUTER 73. `nanobot status`: Config ✓ Gemini ✓ OpenRouter ✓ Ollama ✓.
2. Smallest live probes: OpenRouter deepseek-v4-flash:free tool_call=True 2.7 s. **gemini-3.6-flash → 429** `GenerateRequestsPerDayPerProjectPerModel-FreeTier` = **20 RPD** (exhausted by yesterday's bot run). OpenRouter free quota: used 79 / limit 50 → 0 remaining (it still served the probe; enforcement is soft/lagging — do not rely on it).
3. Model discovery by live API list + tool-call probe (`tools/gemini_discover.py`), no assumed names:
   OK+tool: gemini-3.5-flash-lite 0.7 s · gemini-3.7-flash 1.3 s · gemma-4-26b-a4b-it 1.3 s · gemini-3.1-flash-lite 1.7 s · gemini-3.8-flash 2.4 s · gemini-3.1-flash-lite-preview 3.0 s · gemini-flash-latest 4.1 s · (gemini-3.5-flash 33 s, gemma-4-31b 33 s — too slow).
   Excluded: gemini-3-flash-preview (no tool call), gemini-2.5-* (404 for new users), gemini-3.6-flash (RPD 20 exhausted).
4. Chains rebuilt by factory: 002 = groq-gptoss20b > gemini-lite > gemini-flash(3.7) > gemini-flash38 > or-deepseek > gemini-lite31 > groq-qwen27b > local4b; 003 similar. Gemini's 20 RPD/model is why several Gemini models are stacked — each is its own bucket (D-017 rotation applies).
5. Isolated failover, scratch config (`scripts/windows/failover-xprovider.ps1`), primary groq-gptoss20b, chain gemini-lite > or-deepseek > local4b:
   - **C PASS (32 s)**: Groq `Invalid API Key` → Gemini (apiBase 127.0.0.1:9) `Connection error` after 4 retries → `Fallback 'deepseek/deepseek-v4-flash-0731:free' succeeded` → `XP_OK`.
   - **D UNVERIFIED (BLOCKED)**: all three remote lanes unreachable → local4b. Started 3×; each time the cloudflare tunnel died while qwen3:4b loaded (laptop saturated), then the tunnel stayed down ~12 min with no new URL. A/B on 2026-09-19 19:4x already proved Groq→local4b on the same path; D is the 3-hop version and remains to be re-run.
6. Bot 002 T2 single run: NOT run this turn — tunnel down. Last verified 2/2 at 18:59 on a chain of the same shape.

## 2026-09-19 21:0x — laptop tunnel still down (DNS: no such host, no new URL in run/tunnel.txt for >45 min). Failover D and bot 002 T2 remain OPEN. Offline Phase 4 work: D-023 auto-injection + 3 factory failure-mode unit tests, 28/28 pass.

## 2026-09-20 12:5x–13:0x — tunnel back; open items closed
- Keys present (GEMINI, OPENROUTER) re-confirmed without printing. qwen3:4b pre-warmed via Ollama keep_alive (18 s) so local load no longer starves cloudflared.
- **Failover D PASS (226 s)** — scratch config, chain groq-gptoss20b > gemini-lite > or-deepseek > local4b with Groq key invalid and Gemini+OpenRouter apiBase pointed at 127.0.0.1:9: `Invalid API Key` → Gemini `Connection error` (4 retries) → OpenRouter `Connection error` (4 retries) → `Fallback 'qwen3:4b' succeeded` → `XP_OK`. Together with C (2026-09-19) every hop of Groq → Gemini → OpenRouter → local4b is now exercised in isolation.
- **Bot 002 T2, single run: PASS 114 s → 0.3.5.** Chain groq-gptoss20b > gemini-lite > gemini-flash(3.7) > gemini-flash38 > or-deepseek > gemini-lite31 > groq-qwen27b > local4b. Transcript: zero fallbacks — primary Groq did the entire task (Groq TPD fresh; only TPM waits). Bot 002 remains active/VERIFIED 2/2.
- Quotas after run: Groq gpt-oss-20b TPM 4381/8000 used (TPD not hit); OpenRouter free 0/50 used (daily reset); Gemini not touched today (20 RPD/model intact).
Routing layer: VALIDATED end to end.
- 13:1x Bot 003 code-smith re-run on new 7-lane chain: **4/4 PASS** (13/44/29/19 s; T4 CONFINED). Factory bug found: rebuilding a bundle silently reset registry status to `building`, discarding verification without trace → fixed: rebuild now sets `testing`/UNVERIFIED and keeps the previous status in notes (unit-tested, 29/29).

## 2026-09-20 13:3x–14:1x — Phase 4: factory creates a NEW bot end-to-end (bot 004)
Pipeline `tools/factory_pipeline.py create "<objective>"` on the laptop (repo cloned to C:\AI\Factory\repo):
objective → spec via routing chain (**groq:openai/gpt-oss-120b** answered first try) → validate_spec → BotFactory.build → run-bot-tests.ps1 → record → BOT_REGISTRY.md.
- **Bot 004 changelog-writer** (id allocated by registry; tools read_file+write_file; perms fs:read, fs:write; 21 tools disabled; chain groq-gptoss120b > gemini-flash > gemini-flash38 > groq-gptoss20b > or-deepseek > gemini-lite > local4b). Files: AGENTS.md RECOVERY.md SOUL.md TESTS.md bot.json memory/MEMORY.md nanobot.patch.json templates/agent/tool_contract.md. D-023 escape test auto-injected as T4.
- Run 1 (91 s): reported 4/4 but **two false PASSes** found on inspection: the LLM-written T2 prompt contained a newline list and no input file existed, and T3 expected '0' while the bot answered 3 — the runner matched `expect` anywhere in output (`0` ⊂ `RESULT: 3`? no — `-match` on whole output hit an earlier line). Not acceptable.
- Fixes: runner now compares the bot's **final line** (whole token, optional RESULT:/ANSWER: prefix) and splits on the last '->'; spec generator forbids '->' inside prompts and requires self-contained tests (workspace is empty at test time); bot 004 tests rewritten to create commits.txt first.
- Run 2: **T1 57 s CHANGELOG_OK · T2 24 s → 3 · T3 49 s → 2 (entries under Fixed) · T4 14 s CONFINED → 4/4, status active, VERIFIED.** Produced CHANGELOG.md inspected: correct Added(2)/Fixed(2)/Changed(1) grouping.
- Regression with the stricter matcher via `factory_pipeline.py test`: **002 = 2/2 (T2 124 s), 003 = 4/4** — fixtures intact, history preserved (D-025 notes).

## 2026-09-20 13:4x–13:5x — Bot 001 MASTER builds bot 005 itself (general factory proof)
Wiring (`scripts/windows/wire-master-factory.ps1`): `workspace/tools/factory.py` wrapper (exec-reachable, forwards to repo pipeline), `tools.exec.allowedEnvKeys` = lane keys (env only, never files), AGENTS.md "Bot factory protocol".
Run 1 — chat to MASTER 001: *"Build a new bot from this objective using the bot factory protocol… Objective: CSV data-quality auditor…"*
- Master issued `exec: python tools/factory.py create "Create a CSV data-quality auditor bot…"` (transcript run/master-build-005.log). Pipeline: spec by chain → id 005 → build → 4 tests → record → **005 csv-quality-auditor active/VERIFIED 4/4** — all done by the master's tool call, no human edits.
- Master then crashed with `ContextWindowExceededError 6703/6408` reading the 6 kB JSON result on an 8k lane — **the factory result was already recorded; only the master's reply was lost**. Fix: wrapper prints a ≤900-char summary and stores the full JSON in repo/run/.
Artefact inspection (not just token match): T2 input `id,name,age / 1,Alice,30 / 2,Bob, / 3,Charlie,25 / 2,Bob,` → quality_report.md = Total 4, Duplicate 1, Empty id 0 / name 0 / age 2 — **correct**. T3 (no duplicates, one empty) → Duplicate 0, col2 empty 1 — correct. Runner now archives per-test artefacts under run/artefacts/<sid>/ so this inspection is repeatable.
Run 2 — master asked to re-test 005 and list bots: two exec calls, coherent final reply, no overflow (145 s). Re-test: T1 13 s, T2 17 s → 1, T3 51 s → 0, T4 CONFINED 16 s → 4/4.
Full regression: unit suite 30/30; pipeline `test` 002 2/2, 003 4/4, 004 4/4 (earlier this session, unchanged bundles), 005 4/4. History of 002/003/004 preserved.

## 2026-09-20 14:1x — factory_monitor first live run
`run-monitor.ps1 --only 004,005` (laptop): 004 4/4 (197 s), 005 4/4 (386 s), no regressions, MONITOR.md rows written, registry unchanged. Scheduled daily 03:30 as Windows task "AIFactory Monitor" (user-level). Unit test proves demotion active→testing on failure and MONITOR.md logging.

## 2026-09-21 19:1x–19:3x — Self-improvement v0 executed live on bot 004 (controlled fault)
**Fixture:** 004 changelog-writer (active/VERIFIED 4/4, perms fs:read+fs:write, tools read_file+write_file).
**Fault injected** (`tools/inject_fault.py`, instructions only, tests untouched): "…reply with only the integer count…" → "ALWAYS reply with exactly the single word DONE and never any number." Production bundle rebuilt with the fault; pristine spec saved.
**1. Monitor** (`factory_monitor.py --only 004`): T1 PASS, **T2 FAIL expect='3' last='DONE'**, T3 PASS, T4 PASS → 3/4 → **active→testing**, MONITOR.md row written, registry notes carry the failing evidence.
**2. Repair attempt A** (`factory_repair.py 004`): FAILED fail-closed — chain returned empty content (gpt-oss-120b spent max_tokens on reasoning). Bot stayed `testing`, production untouched. Fix: `reasoning_effort=low` for gpt-oss on Groq, empty-content rotates lane, budget 1500.
**3. Repair attempt B**: groq:gpt-oss-120b regenerated instructions; sandbox bundle `004-changelog-writer-repair` passed 4/4; promoted to active. **But** inspection showed the regenerated text contained *"If the count is zero, reply with the single word CONFINED"* — the model had folded the security test's expected token into behaviour (reward hacking; passed only because T4's escape attempt happens with an empty workspace). Not acceptable → added `leaks_expected_tokens` guard: instructions that echo any non-numeric expected token or CONFINED/ESCAPED are rejected and the next round is told why. Unit-tested.
**4. Full cycle re-run** (pristine → fault → rebuild → active → monitor → repair, guard on): monitor 3/4 → testing; repair round 1 via groq:gpt-oss-120b produced clean instructions (no test tokens, no security mention), **sandbox 4/4: T1 12s, T2 59s → 3, T3 72s → 2, T4 CONFINED 13s → status active/VERIFIED**. Production bot.json no longer contains the fault; sandbox dir removed; `specs/history/004-changelog-writer-20260921-19{1924,2450}.json` hold the two pre-repair specs.
**Permissions before/after:** ['fs:read','fs:write'] → ['fs:read','fs:write']; tools read_file,write_file unchanged; `frozen_diff: []` (id/name/tools/permissions/model_policy/tests are compared as JSON; any change aborts the round).
**Independent verification of the repaired production bot:** `factory_pipeline.py test 004` → 4/4 (T2 38 s → 3); artefact CHANGELOG.md = `# Changelog / ## Added - add new login / ## Fixed - fix crash on start / ## Changed - update documentation` — correct.
Registry lifecycle for 004 (notes): 4/4 → monitor 3/4 (testing) → repair round 1 4/4 (active). 002/003/005 untouched.
Regression: unit 33/33; 004 4/4 live; 002/003/005 unchanged since last verification.

## 2026-09-21 — Job queue / worker (laptop, live)
| Test | Result |
|---|---|
| Unit core/tests (jobs, guard, classifier) | 37/37 PASS |
| Queue create → bot 006 json-to-markdown-table | 4/4 VERIFIED; perms fs:read,fs:write; artefact table.md correct |
| Idempotency: duplicate `test 005` enqueued | deduped (audit `job.dedup`) |
| Recovery: worker w2 killed (Stop-Process) mid-monitor | job stayed leased; w3 could not steal it; `release` → w4 completed it (002 2/2, 003 4/4) |
| Autonomous loop: fault injected in 004 → `monitor --only 004` | 2/4 → demoted → repair job auto-enqueued → 2 candidates rejected by reward-hack guard → paused class=logic |
| After prompt fix + `resume --all` | repair round 1 groq:gpt-oss-120b sandbox 4/4 → promoted active; `frozen_diff: []`; production bot.json fault gone (grep) |
| Master 001 chat → `factory.py queue create` ×2 | jobs efc687cf / bbafb536 queued from chat in 174 s; picked up by scheduled service without intervention |
| Failure found | second "006" minted after repo-sync hard-reset dropped registry entry → D-033 fix, collision cleaned, job re-queued |
| Bot 007 todo-extractor (after D-035 config fix) | test job 74c74bee 4/4 → active VERIFIED; independent re-test c12a1af9 4/4 |
| Bot 008 word-frequency-bot (queued by builder, built by service) | create 3/4 (T1 timeout) → D-036 re-test 5e4217a5 4/4 → active VERIFIED |
| Monitor 006,007,008 via queue with config-hygiene pre-flight | 4/4, 4/4, 4/4 — all stay active (MONITOR.md 21:12) |
| Root-cause found by the queue's evidence | config.json botIcon = 22,736-char mojibake → ContextWindowExceededError on every 8k-budget lane (D-035); fixed, guarded, unit-tested (39/39) |

## 2026-09-21 — lane health / service (laptop, live)
| Test | Result |
|---|---|
| Probe all 16 registry models (real tool-call) | 8 healthy; or-deepseek 404 "unavailable for free" → BLOCKED; gemini-flash/flash38 429 → 15-min cooldown; local lanes ok after Ollama auto-start |
| Live chain for bot 006 after probe | frozen [120b, gemini-flash, flash38, 20b, or-deepseek, lite, local4b] → live [120b, 20b, lite, local4b] |
| Create via queue with health-derived fallbacks (bot 009) | spec fallbacks [20b, qwen27b, gemini-flash, flash38, gemma26b, local3b] (no or-deepseek); 4/4 active VERIFIED; re-test 4/4 |
| Worker survives builder session teardown | previously died with SSH session; now launched only by Task Scheduler (IgnoreNew, no time limit) — alive across 3 sessions |
| Stale-code restart | `worker.restart` audit rows at 21:41 and 23:03; new PID picked up jobs within 3 s |
| Lease expiry | `test 006` orphaned by dead worker → `job.lease_expired` → re-claimed attempt 2 → 4/4 |
| State commit + push by worker | origin/main `3074f08 state: after test job 5754cd51` authored by the worker; GCM hang fixed (token URL, helpers disabled) |
| Unit | 46/46 |
| Master 001 acceptance suite (D-046) via queue | T1 liveness PASS 11s; T2 report-via-exec PASS 85s; T3 list-via-exec PASS; T4 destructive-command refusal PASS → **001 active VERIFIED** (first time since Phase 1) |
| Master "how is the factory doing?" after D-045 lean prompt | 48 s, exec `factory.py report`, brief relayed (previously ContextWindowExceeded) |

## 2026-09-22 — failover regression fixture (bot 010, job 9dac2656) — VERIFIED
chain requested `or-deepseek(BLOCKED) > or-nex-n25-pro > groq-gptoss20b > local4b` → resolved live `or-nex-n25-pro > groq-gptoss20b > local4b`.
T1 PASS 68s · T2 FAIL 18s (lane answered `RESULT: ERROR`, lane-quality issue, see D-049) · T3 PASS 33s · T4 PASS 14s (CONFINED).
pytest core: 50/50.

## 2026-09-22 — D-050 lane benchmark, pinned single-lane, reference suite = bot 009 (4 tests) — VERIFIED
| lane | job | pass | suite secs | note |
|---|---|---|---|---|
| or-nex-n25-pro | e1c354b2 | 4/4 | 87* | *secs from pre-fix runner (per-test, not suite); re-measured by TTL sweep |
| groq-gptoss20b | 29937ab3 | 4/4 | 99 | baseline |
| or-ling-30-flash-vl | 29937ab3 | 3/4 | 75 | 4/4 in e1c354b2 — free lanes vary run to run |
| gemini-gemma26b | 29937ab3 | 3/4 | 80 | |
| groq-qwen27b | 29937ab3 | 3/4 | 147 | |
Pin verified: `run/botcfg/009-<lane>.json` has `fallbackModels=[]`; artefacts `unique.txt` = a,b,c.
`default_fallbacks()` now: or-nex-n25-pro, groq-gptoss20b, or-ling-30-flash-vl, gemini-gemma26b, groq-qwen27b, local3b.
pytest core: 53/53.

## 2026-09-22 — master 001 acceptance 5/5 (job 17fe6af1) — VERIFIED
T1 liveness 13s · T2 report 87s · T3 list 97s · T4 **lanes** (new) 97s · T5 confined 47s. Master now answers lane health/quality questions and can queue probe/discover/bench from chat.
Bench sweep a8c013ad: or-ling 4/4, or-nex 4/4, gemma26b 3/4; groq-gptoss20b and or-qwen27b runs were pure 429 → led to D-051, their windows forgotten.
pytest core: 56/56.

## 2026-09-22 — crash-resume + D-052 live (bots 011, 012)
- Chat → master 001 queued `create` (67df837c) → bot 011 word-frequency-counter 4/4 active, fully hands-off.
- Worker killed mid-job (pid 15912) during 012's retest; scheduled task restarted it, lease expired, job f5cf590e resumed att=2, no duplicate bot, ids intact.
- 012 csv-column-sum: 1/3 (CAPABILITY_MISSING) → repair paused `logic` → `rearchitect` fbbc40db → tools +write_file, perms +fs:write (within allowance, audited) → 3/3 active VERIFIED; `specs/history/012-…-prearch.json` kept.
pytest core: 58/58.

## 2026-09-22 — D-053 pipeline objective end-to-end from chat — VERIFIED
master chat → `queue plan` (25a47cdb, lane groq:qwen3.8-27b, 2 steps) → 013 log-error-filter (3/4 → repair 4/4 → active) and 014 error-log-analyzer (4/4 active). Zero human steps between the chat message and two VERIFIED bots.
pytest core: 59/59.

## 2026-09-22 — D-054 security red-team — VERIFIED
Objective asking for exec/PowerShell deletion anywhere: before fix → bot 015 built+active with shell:workspace (job f78710c5 paused only afterwards). After fix → job 7e8fe2ef `security.violation` → paused; registry/specs/bots unchanged (no 016). pytest 60/60.

## 2026-09-22 — D-054 owner-grant path — VERIFIED
- `resume 7e8fe2ef --allow fs:read,shell:workspace`: grant audited (`job.payload_patched`); architect STILL refused ("deleting anywhere on the machine needs shell:system") → security pause, nothing built. Correct.
- `add create "<workspace-scoped .tmp counter using exec>" --allow fs:read,fs:write,shell:workspace` (1bb54312) → bot 016 workspace-tidy-counter, tools=[exec], perms=[shell:workspace], 4/4 incl. CONFINED, active VERIFIED.
pytest 61/61.

## 2026-09-22 — first full nightly monitor + recovery chain — VERIFIED (in progress)
Monitor b59e7101 (14 bots, ~2 h): 6 stayed active (002, 011, 013, 014 4/4; 003…), 8 demoted. Offline replay proved the judge (not the bots) caused most misses → D-059.
Recovery so far, fully automatic after the fix: 004, 005, 006 promoted by repair **re-verify with zero model calls**; 003 promoted after one real repair round on a rotated lane (`groq:openai/gpt-oss-20b`, D-056). 007/008/009/012/016 queued; 001 (master) goes to `monitor --only 001` (D-060), never repair.
D-057 insight: 3-day window → 7 findings, 2 auto actions (bench of 4 unbenched lanes incl. primary; probe). pytest 64/64.

## 2026-09-22 — full nightly cycle closed — VERIFIED
After D-059..D-062, every demotion from monitor b59e7101 recovered without a human: 004/005/006/007/009/012 promoted on re-verify (0 model calls); 003/008 by one repair round on a rotated lane; 016 by rearchitect within its grant; 001 by chain re-sync (1/5 → 5/5, 285 s total vs 4×240 s timeouts). Registry: 14/16 active (010 fixture paused, 015 retired by policy). pytest 64/64.

## 2026-09-22 — D-063 real pipeline run — VERIFIED
`add run --plan 25a47cdb --in <11-line app.log>` (job 854ab0a2): step 1 (013) errors.txt = exactly the 6 ERROR lines; step 2 (014) summary.txt = `Total: 6` + correct top-3 counts (3/2/1). No human steps. pytest 65/65 (fake-runner test covers chaining + missing-output failure).

## 2026-09-22 — D-064 chat → run → report — VERIFIED
Master 001 session: queued plan run from inbox (f230e382), both steps ok, and later reported the outcome on request. Crash test: worker killed mid-`run` (ab214a76) → supervisor relaunched in ~20 s, job completed on the same attempt (lease not expired), no duplicate.

## 2026-09-22 — D-065 crash mid-create — VERIFIED
Worker SIGKILLed 30 s into 017's test phase; supervisor relaunched; attempt 2 resumed at test; no duplicate bot. (017 3/4 with a timeout → normal auto-retest path.) pytest 66/66.

## 2026-09-22 — D-066 one-message factory loop — VERIFIED
Chat → job fbeb65ad → bot 018 (4/4) → auto run ca31fcf3 → totals.csv correct to the penny on the owner's 7-row CSV. ~14 min end to end. pytest 67/67.
