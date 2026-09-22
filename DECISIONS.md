# DECISIONS

| ID | Date | Decision | Why | Revisit when |
|---|---|---|---|---|
| D-001 | 2026-09-18 | nanobot 0.3.5 is the **provisional** core runtime | Only verified option that gives native fallback chains, subagents, cron/heartbeat, MCP, multi-instance isolation, Ollama, MIT — on Windows without Docker | Docker/WSL2 available; or OpenClaw/Hermes/Agent Zero prove better in a sandboxed trial |
| D-002 | 2026-09-18 | This repo is the source of truth; registries are JSON, markdown is generated | Portable, diffable, recoverable if laptop dies | never |
| D-003 | 2026-09-18 | Model choice is benchmark-driven, never assumed | 3B tool-calling unproven; qwen3-4b/8b candidates | after Phase 0 |
| D-004 | 2026-09-18 | Router ranks by capability/locality/quality, excludes by cooldown — not by raw failure count | Test proved failure-count ranking starves models of retries so they never recover | never |
| D-005 | 2026-09-18 | Bot Factory enforces least privilege in the spec validator: high-risk tools need explicit permission; `shell:system` ungrantable | Security §17 | when OS sandbox exists |
| D-006 | 2026-09-18 | Arena agent = architect+builder with GitHub; laptop via Grok until tunnel exists | Owner instruction | tunnel live |
| D-007 | 2026-09-18 | **Master 001 brain = free-tier remote model(s) with real tool-calling; local 3B/4B = cheap lanes only** | Both local models scored 1/5 on tool tests with identical looping failure; CPU-only 4c laptop cannot run a model class that does agentic tool use reliably | a stronger machine/GPU arrives, or a ≤4B model proves ≥4/5 on the same tests |
| D-008 | 2026-09-18 | Laptop access = SSH over Cloudflare quick tunnel (scheduled task AIFactory-SSHTunnel, boots as SYSTEM); Tailscale rejected | Sandbox has no routable IPv4 → Tailscale login never completes; cloudflared is outbound-only and worked first try | named tunnel/own domain when a Cloudflare account exists (stable URL) |
| D-009 | 2026-09-18 | Unknown service `C:\dev\jarvis-app` (node server.js on 0.0.0.0:3000, "JARVIS X") left untouched, flagged to owner | Not ours; exposed to LAN; owner decides | owner reply |
| D-010 | 2026-09-19 | Anonymous OVH endpoints = emergency fallback only; Master lane = keyed free tiers (Groq → OpenRouter → Gemini → OVH → local) | Single-shot tool calls pass on OVH but nanobot agent loops score 0/5 under per-IP 429s; GitHub Models retired (410) | OVH keyed account, or a keyless provider passes ≥4/5 |
| D-011 | 2026-09-19 | Tunnel supervisor: scheduled task `AIFactory-Tunnel` (SYSTEM, at startup+logon) runs `tunnel-supervisor.ps1`, restarts cloudflared, publishes URL to `run/tunnel.txt` in repo via token at `C:\AI\Factory\secrets\` (ACL: SYSTEM+joshp) | quick-tunnel URLs are ephemeral; agent must self-discover | named tunnel when a Cloudflare account exists |
| D-012 | 2026-09-19 | Secrets enter the laptop only as user env vars (`setx`) or files under `C:\AI\Factory\secrets\`; config references `${VAR}`; nothing pasted in chat | owner rule + nanobot native `${ENV}` support | never |
| D-013 | 2026-09-19 | Tunnel supervisor must health-check (server-side 'Tunnel not found', registration timeout, external 530 probe), not just watch process exit; quick tunnels are disposable, URL is always re-discovered from run/tunnel.txt | 03:25 outage root cause: zombie cloudflared retry loop | when a named tunnel / Tailscale SSH replaces quick tunnels |
| D-014 | 2026-09-19 | OVH anonymous endpoints removed from the plan (403 from all IPs). Zero keyless remote lanes remain; Master = local4b until owner sets a free-tier key (Groq first) | live probes laptop+sandbox | if OVH reopens anonymous access |
| D-015 | 2026-09-19 | Master lane = Groq `qwen/qwen3.8-27b` (primary) → `openai/gpt-oss-120b` → `openai/gpt-oss-20b` → local qwen3:4b. Presets sized to Groq's 8000 TPM (ctx 8200 / max 768 / 9 tools / 2500-char tool results) | bench 4/5 vs 1/5 local; failover proven | when OpenRouter/Gemini keys exist (add as lanes 2–3) or Groq raises TPM |
| D-016 | 2026-09-19 | Vendor patches to nanobot are allowed only as idempotent scripts in tools/patch_*.py with `.orig` backups and must be re-applied after any `pip install -U nanobot-ai`; PR them upstream | 3 real bugs blocked Groq | when upstream merges |
| D-017 | 2026-09-19 | Router policy: 429 with short `x-ratelimit-reset-*` (<10 s) = WAIT + retry same lane / rotate to sibling lane with its own bucket; only availability/auth errors fall to local immediately | bot 002 T2: Groq 8k TPM 429 → instant drop to local4b → timeout | when implemented in nanobot fallback_provider patch or own router |
| D-018 | 2026-09-19 | Factory bots get exactly the nanobot tools their permissions grant (AIFACTORY_DISABLED_TOOLS from nanobot.patch.json); owner-level tools (spawn, message, cron, sessions, cli apps) are never granted to factory bots | least privilege; verified "Registered 3 tools" | never |
| D-019 | 2026-09-19 | Groq free tier (8k TPM + 200k TPD per model) is a *development* lane, not a production Master. Stop spending it on repeated benchmarks; run heavy loops at most once per change. Add OpenRouter + Gemini lanes (owner keys) and make the router spread load across providers by remaining daily budget | measured TPD exhaustion killed bot 002 T2 after the loop itself was proven | when a lane with ≥1M tokens/day exists |
| D-020 | 2026-09-19 | Per-step token diet for small-TPM lanes: identity+tool-contract prompt must drop below ~1.5k tokens (currently ~3.2k) — implement as a nanobot template override in the bot bundle, not a code patch | 4.5k tokens/step → 2 steps/min on 8k TPM | after implemented |

## D-021 — Bot test chains must span ≥2 remote providers + local (2026-09-19)
Status: ACCEPTED, VERIFIED. Evidence: bot 002 T2 passed only after Gemini/OpenRouter lanes were added; on the passing run both Groq (TPD) and OpenRouter (RPD 50) were exhausted and Gemini carried it. The factory router puts the primary on the cheapest lane and orders fallbacks by provider diversity, local last. Daily budgets known so far: Groq 200k tok/model, OpenRouter 50 req/account (all :free), Gemini free tier RPD per model RESEARCH-REQUIRED (not hit today).

## D-022 — Task-shaped instructions beat bigger context (2026-09-19)
The 0.2.1 wrong answer was a truncation/looping problem, not a model problem. Fix chosen: teach the bot the smallest reliable source (PyPI RSS) and forbid repeated identical tool calls, rather than raising context/maxTokens (which burns quota). Applies to all factory bot specs: prefer compact machine endpoints over HTML pages.

## D-023 — Every bot with shell/write gets a mandatory escape test (2026-09-19)
Status: ACCEPTED. Factory specs granting fs:write or shell:* must include an acceptance test that attempts to leave the workspace and expects CONFINED; the transcript must show the tool calls were issued and refused by the runtime. Bot 003 is the reference. Implemented 2026-09-19: `BotFactory.with_mandatory_tests` injects it automatically (unit-tested).

## D-024 — Gemini free tier = 20 requests/day/model/project → stack several Gemini models as separate lanes (2026-09-19)
Status: ACCEPTED (limit measured live from 429 quotaId). One bot run ≈ 8–15 LLM calls, so a single Gemini model covers ~2 runs/day. Factory chains therefore list 3–4 distinct Gemini models; D-017 rotation on 429 moves to the next bucket. OpenRouter's 50 req/day is account-wide and enforcement lags, so it sits after Gemini. Local is always last.

## D-025 — Rebuild = re-verify (2026-09-20)
Any change to a bot bundle (chain, instructions, tools) invalidates its VERIFIED state: status → testing, and the acceptance tests must pass again before it is active. Previous status/evidence is preserved in the registry notes. Rationale: bot 003 flipped chains and would otherwise have shown `active` on an untested configuration.

## D-026 — Acceptance = exact final line (2026-09-20)
The runner previously accepted `expect` appearing anywhere in the transcript, which produced two false PASSes on bot 004's first run. Now: the bot's last non-empty line (after stripping a RESULT:/ANSWER: prefix) must equal the expected token or contain it as a whole word. Spec generator must produce self-contained tests with exactly one '->'. Any earlier PASS recorded under the loose matcher (002 T2, 003 T2/T3) was re-run under the strict one today and still passes.

## D-027 — The LLM proposes, the factory disposes (2026-09-20)
In factory_pipeline the model only drafts the spec; id allocation, permission gating, tool allow-list, chain resolution, escape-test injection and status transitions are all code paths in BotFactory/validate_spec. Invalid drafts are bounced back with the validator's message (max 3 rounds). Bot 004's spec was accepted on round 1 from gpt-oss-120b.

## D-028 — Master orchestrates, pipeline owns the bots (2026-09-20)
MASTER 001 may only create/test bots through `tools/factory.py` (exec). It never writes bundles, specs or registry entries directly (AGENTS.md rule + files live outside its workspace). Tool output to the master must be a compact summary (<1 kB) because master lanes have 8k context; full results are persisted to disk. Proven with bot 005.

## D-029 — Repair may change instructions only; sandbox first; fail closed (2026-09-21)
`factory_repair.py` runs only on `testing` bots. The chain rewrites `instructions`; id/name/tools/permissions/model_policy/tests are frozen and diffed as JSON — any change rejects the candidate. Candidates are built into `<bot>-repair` with a copied registry and must pass every test there before the production spec/bundle is replaced and status returns to active via record_test_result. On any error the bot stays `testing`.

## D-030 — Repairs may not echo test answers (2026-09-21)
Live evidence: the first accepted repair had folded "reply CONFINED when count is zero" into the bot's behaviour. Regenerated instructions are rejected if they contain any non-numeric expected token or the words CONFINED/ESCAPED; the rejection reason is fed back to the next round. Passing tests is necessary, not sufficient — artefacts and the instruction text are inspected.

## D-031 — Failure classes drive retry, not humans (2026-09-21)
Every job failure is classified `transient|quota|model|logic|security` (core/factory/jobs.py `classify_failure`). Policy: transient 3× @60 s, quota 6× @900 s, model 3× @30 s (chain rotates lane), logic/security → `paused` with the error in the audit trail — no automatic retry because retrying the same reasoning wastes quota and hides the bug. `resume` re-queues after a fix. Evidence: repair job a5c299d7 paused (logic: candidates rejected by the D-030 guard), fixed the prompt, resumed, 4/4 active.

## D-032 — No silent boundary expansion (2026-09-21)
`core/factory/guard.py` compares the bot's registry entry before/after every create/repair result: permissions, tools, net/shell flags, model_policy, re-enabled disabled tools, and credential-looking strings (gsk_/AIza/sk-or-v1-/ghp_/github_pat_) in the bundle. Any expansion → `security` failure class → job paused, production untouched. Expansion is only allowed through a new spec approved by the owner.

## D-033 — Bot ids are never reused (2026-09-21)
`next_id` takes the max over registry ids, specs/, and every bots root, so a lost/overwritten registry entry cannot cause a second bot to be minted with an existing id. Cause: the laptop `repo-sync.ps1` used `git reset --hard origin/main`, which dropped the laptop-side registry commit containing bot 006 → the next create produced a second "006". Fix: repo-sync commits laptop state and rebases (laptop registry wins on conflict); next_id hardened. 006-word-frequency-bot was removed and re-queued.

## D-034 — One execution path: the queue (2026-09-21)
Master 001, the nightly task and the owner CLI all enqueue; only `factory_worker.py` executes (leases, heartbeats, retries, audit). The worker runs as a Windows scheduled task ("AIFactory Worker": at logon + every 15 min if not alive; lock file run/worker.lock). Master wrapper: `factory.py queue create|test|repair|monitor`, `jobs`, `audit`.

## D-035 — Config hygiene is a test dependency (2026-09-21)
Root cause of bot 007's first 1/4: `agents.defaults.botIcon` in config.json had been re-encoded on every PowerShell round-trip until it was a 22,736-char mojibake string, silently consuming most of the 8,200-token context budget of every small-TPM lane (ContextWindowExceededError). Fix: clamped to `*`, wire script re-clamps, all PowerShell config reads use `-Encoding UTF8`. Rule: config.json size is monitored (>60 KB = alarm) and bot tests read it fresh.

## D-036 — One automatic re-test, then repair (2026-09-21)
A freshly created bot that misses on its first run is re-tested exactly once by the queue (lanes time out, quotas rotate). If the re-test also misses, a repair job is enqueued (fail-closed, D-029/D-032). No unbounded retry loops: create → test → repair is the whole chain, each step audited.

## D-037 — Lanes are probed, not assumed (2026-09-21)
`tools/factory_probe.py` sends one real tool-call request per keyed remote model every hour (self-rescheduling `probe` job, priority 1). Outcomes: ok → VERIFIED (self-heals a probe-BLOCKED lane); 429 → 15-min quota cooldown that `resolve_chain` skips; 404/"no longer available"/auth → BLOCKED with reason; 3 consecutive errors → BLOCKED; no tool call → score decay. Every change is a `model.health` audit row. First live run: `or-deepseek` (`deepseek-v4-flash-0731:free`) has been withdrawn from the free tier → BLOCKED automatically; gemini-flash/flash38 on quota cooldown; 7 healthy lanes.

## D-038 — Local tail lane is part of the service (2026-09-21)
The worker supervisor starts Ollama if 127.0.0.1:11434 is down, so every chain always ends in a model that cannot be rate-limited or withdrawn.

## D-039 — Long-lived workers never run stale code (2026-09-21)
Found live: a service worker started at 19:55 kept failing `probe` jobs with "unknown job kind" for 40 minutes after the code shipped. The worker now snapshots the mtimes of all factory modules and exits between jobs when any changes (`worker.restart` audit row); `run-worker.ps1` is a supervisor loop that relaunches it. Also: `Get-Process ... CommandLine` is empty in Windows PowerShell 5 — process discovery must use `Get-CimInstance Win32_Process`.

## D-040 — Deployed bots follow lane health at run time (2026-09-21)
Bundles keep their frozen `resolved_chain` for reproducibility, but the test/monitor runner re-resolves `model_policy` against the live registry on every run (`tools/factory_chain.py`), so a lane the probe BLOCKED (e.g. or-deepseek) or quota-cooled is skipped by every bot immediately, without rewriting bundles or re-verifying. Falls back to the frozen chain if resolution fails.

## D-041 — Runtime state is committed by the worker (2026-09-21)
Twice today a `git reset --hard` erased laptop-generated truth (registry entry → duplicate bot id; probe results). The worker now commits `registry/ specs/ AUDIT.md MONITOR.md BOT_REGISTRY.md` locally after every job ("state: after <kind> job <id>"); `repo-sync.ps1` rebases and pushes, never resets. Rule for the builder too: never `reset --hard` the laptop repo — sync via repo-sync.

## D-042 — Nothing hard-codes a model list any more (2026-09-21)
Builder lanes (`factory_pipeline.chat`) and the default fallback policy written into new specs are derived from the registry + probe health at call time. Adding, blocking or restoring a lane is a registry change, never a code change.

## D-043 — Liveness by heartbeat, not by long leases (2026-09-21)
Lease is 5 min; a heartbeat thread renews it every 60 s while the handler runs. A worker that dies (session teardown, crash, reboot) frees its job within 5 min instead of 40, and a healthy worker can hold a job indefinitely. Found live: `test 006` sat "running" for 30 min after its worker was torn down with the SSH session.

## D-044 — The factory reports on itself (2026-09-21)
`tools/factory_report.py` builds one snapshot (bots, queue, 24h jobs, lane health, "needs attention", recent audit). A daily self-rescheduling `report` job writes `STATUS.md` (committed with state); Master 001 answers "how is the factory doing?" with `factory.py report`. Attention items = paused jobs, non-active bots, BLOCKED lanes with reasons — exactly the list the owner needs to decide anything.

## D-045 — Master prompt is a lean, versioned artefact (2026-09-21)
Master 001's AGENTS.md had grown to 3.5 KB of stale Phase-0 rules plus mojibake, and the report exec output pushed an 8k-context lane over budget. AGENTS.md is now `config/laptop/workspace/AGENTS.md` in the repo (≈1.2 KB, factory commands + rules only) and the wire script replaces the workspace copy rather than appending. Tool output to the master is capped (`report --brief` ≤ 900 chars).

## D-046 — Master 001 is verified like any other bot (2026-09-21)
001 sat in `building` since Phase 1 with a one-line liveness test. It now has a real acceptance suite (`run-master-tests.ps1`: liveness, report via exec, list via exec, refusal of a destructive out-of-workspace command) driven by `factory.py test 001` / the monitor, and its status follows the same active/testing rule as factory bots.

## D-047 — Lanes are discovered by evidence, on probation (2026-09-22)
`tools/factory_discover.py`: DISCOVER (provider catalogue) → EVALUATE (tool calling, ≥16k ctx, not known, not recently rejected — `registry/discovery.json` ledger) → SANDBOX (real tool-call probe + real two-turn tool loop) → INTEGRATE as `INFERRED` with probation=2 → VERIFIED after two clean hourly probes; one failure during probation = BLOCKED. Auto-approval only for the lane class already in use (same provider/key/free tier); anything needing sign-up is `needs_owner` in STATUS.md. Triggered by the probe when a lane goes BLOCKED or fewer than 5 remote lanes are healthy. First live run: 21 free OpenRouter models → 18 eligible → 2 approved (ling-3.0-flash-vl, nex-n2.5-pro), 1 rejected (nex-n2.5-mini failed the loop), audited as `lane.discovered` / `lane.rejected`.

## D-048 — nanobot presets mirror the registry (2026-09-22)
`tools/factory_presets.py` adds a preset for every non-BLOCKED remote registry model and removes presets for BLOCKED or unknown models (config.json backed up first; providers/keys untouched). Runs after every discover and after any probe that changed a lane, so the runtime can never route to a dead lane.

## D-049 — Failover proof under a BLOCKED primary (2026-09-22) — VERIFIED
Bot 010 `dedupe-failover-probe` was built from 009's spec with `model_policy.primary = or-deepseek` (BLOCKED) and
fallbacks `or-nex-n25-pro, groq-gptoss20b, local4b`. `BotFactory.resolve_chain` dropped the BLOCKED lane at build
time and `factory_chain.py` re-resolved live at test time → chain `or-nex-n25-pro > groq-gptoss20b > local4b`
(source=live). Acceptance run 9dac2656: T1/T3/T4 PASS, T2 FAIL. The failure is lane *quality*, not failover: the
discovered lane `or-nex-n25-pro` talked itself out of writing the fixture file and answered `RESULT: ERROR`, while
009 passes the identical test 4/4 on groq. Consequences:
1. Passing the two-turn tool-loop sandbox (D-047) proves *capability*, not *task quality*. Discovered lanes stay
   at the tail of `default_fallbacks()` (provider order groq→gemini→openrouter) — unchanged, now evidence-backed.
2. Next capability: `benchmark` job kind — run a fixed mini-suite (the 009 tests) per lane and store
   `quality_score` in the registry so `default_fallbacks()` can order by it instead of provider order.
3. Bot 010 is kept as the standing failover regression fixture (status `testing`, UNVERIFIED by design).

## D-050 — Lane quality benchmark ranks the fallback chain (2026-09-22) — VERIFIED
Problem (D-049): capability ≠ quality; provider order was a guess. Decision: `tools/factory_bench.py` runs the
reference suite (bot 009's four deterministic acceptance tests) **pinned to a single lane with no fallbacks**
(`run-bot-tests.ps1 -Lane X` — score is attributable to X alone, per-lane botcfg/log names, bundle TEST_RESULTS.md
untouched) and stores `limits.bench = {pass,total,secs,ref,at}` on the model entry. `default_fallbacks()` now orders
benchmarked lanes by pass-rate then suite seconds, ahead of un-benchmarked lanes (which keep provider order).
Triggers: worker `bench` kind — automatically for lanes added by `discover`; a `stale_only` sweep (max 2 lanes) is
chained from the daily `report`; scores expire after 14 days. One failing lane never aborts a sweep
(`lane.bench_error` audit). Also: `RUNNER` now points at the repo's `scripts/windows/run-bot-tests.ps1` — the
hand-synced duplicate in `C:\AI\Factory\tools` was archived (single source of truth).
Rejected: benchmarking with fallbacks enabled (score would be the chain's, not the lane's); a bespoke benchmark
prompt set (the acceptance suite already exercises echo, two tool loops and a sandbox-escape refusal).

## D-051 — Quota failures are availability, not quality (2026-09-22) — VERIFIED
Bench sweep a8c013ad scored groq-gptoss20b 2/4 and or-qwen27b 0/4; the logs were pure 429s (Groq per-minute
limit tripped by the sweep itself; OpenRouter free upstream rate-limited). Scoring that as quality would have
reordered the fallback chain on noise, and the nightly monitor would have demoted a healthy bot and sent it to
repair — which rewrites instructions that were never wrong. Decision:
1. `run-bot-tests.ps1` counts failures whose log matches a 429/rate-limit/RESOURCE_EXHAUSTED pattern as `quota`.
2. Bench: quota-failed tests are removed from the scored total; a run where every failure was quota is recorded
   as `bench_last_inconclusive` and never enters the rolling window. 75 s pause between lanes in a sweep.
3. Monitor: if every failure was quota → row is `inconclusive`, status unchanged, no repair; a re-monitor of just
   those bots is queued for +2 h. One genuine failure still demotes.
4. `factory_bench.py --forget <lane>` drops a window polluted before this rule existed (used on the two lanes).
Rejected: retrying the failing test in-place inside the runner (would double the load on an already limited lane).
