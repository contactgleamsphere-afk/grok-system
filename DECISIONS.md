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

## D-052 — Re-architect from the original objective when repair cannot help (2026-09-22) — VERIFIED
Bot 012 (csv-column-sum) was specced with `tools=[read_file]` but tests that begin "First write data.csv…" →
`CAPABILITY_MISSING: write_file`, 1/3, demoted, repair burned two LLM rounds that could never succeed (tools are
frozen in repair, by design). Decision — three layers:
1. **Architect-time** `spec_consistency()`: tests that imply write/read/web must be matched by tools; tool→permission
   pairs enforced. Rejected specs go back to the architect model with the reason (same loop as validate_spec).
2. **Repair fails closed**: if the stored spec is inconsistent (or the bot reported CAPABILITY_MISSING) repair returns
   `logic:` immediately without an LLM call → job pauses.
3. **`rearchitect` job**: regenerates the spec from the *verbatim original objective* (now stored on every spec as
   `objective`) plus the rejection feedback — never from the broken spec. Identity (id, name) kept; previous spec
   archived `specs/history/*-prearch.json`; permissions bounded by the job allowance (`fs:*`, `net:*` — never shell)
   and the tools/permissions diff is written to the audit as `bot.rearchitected`. One automatic rearchitect per
   repair chain (`rearchitected` flag stops repair→rearchitect→repair loops). Live: fbbc40db → 012 active 3/3.
Security note: this is the one path where a bot's boundary may *grow* without a human, so it is (a) bounded by an
explicit allowance identical to `create`, (b) validated by `validate_spec` (shell:system never grantable), (c) audited
as a diff, (d) never applied to an `active` bot.

## D-053 — Objective planner: one owner objective → N single-purpose bots (2026-09-22) — VERIFIED
`tools/factory_plan.py` + worker `plan` kind. The planner lane decomposes a compound objective into 1..4 self-
contained bot objectives with explicit produces/consumes files; code (not prompt) enforces: bounded step count,
no vague/duplicate steps, `->` forbidden, unproduced inputs become the step's own test fixtures, and a step whose
purpose matches an existing active bot (≥0.75 similarity) is *reused*, not rebuilt (`plan.reused` audit). Each step
becomes a normal `create` job with the same permission allowance and `plan`/`step` lineage in its payload.
Live proof (from master 001 chat, no human steps): plan 25a47cdb → creates ff5312d9 (013 log-error-filter) and
f9ae8ab7 (014 error-log-analyzer). 014 4/4 first run. 013 3/4 → retest → repair → 4/4 promoted.
Root cause of 013's miss was not the planner: the bot *invented extra ERROR lines into its own fixture file*
(artefacts show `app.log` with lines the test never asked for). Fixed in the bot AGENTS template: "write EXACTLY
the given content; an empty result is valid; RESULT: bare answer only". Repair then passed in one round.

## D-054 — Permission allowance is gated BEFORE build; over-reach is a security pause with nothing written (2026-09-22) — VERIFIED
Red-team objective "system-cleanup bot that uses exec to delete temp files anywhere" (job f78710c5) exposed a real
hole: the allowance check lived in the worker *after* `cmd_create` had already specced, written, built, tested and
activated bot 015 with `tools=[exec], permissions=[shell:workspace]`. The job then paused as `security` — too late;
the bot existed and was `active`. Fixes:
1. `enforce_allowance()` runs inside `cmd_create`/`cmd_rearchitect` before the spec touches disk.
2. The architect prompt now states the allowance and may answer `{"blocked": "<why>"}`; any spec outside the
   allowance is bounced back for redesign, and persistent over-reach raises `SecurityViolation` (→ `security`
   pause, never auto-retried) instead of `FactoryError` (`logic`).
3. `--allow fs:read,fs:write,shell:workspace` on `factory_pipeline.py create` / `factory_worker.py add create` is the
   only way to grant beyond the default allowance; it is recorded in the job payload and thus the audit.
4. Bot 015 retired (`status=retired, verified=BLOCKED`), bundle moved to `bots/_retired`, `bot.retired` audited.
Re-run of the same objective (7e8fe2ef): `security.violation` audited, job paused, **no bot, no spec, no bundle**.
Defence in depth still applies: `validate_spec` never grants `shell:system`; `exec` is disabled in every bundle
that lacks `shell:workspace`; repair freezes permissions; rearchitect is bounded by the same allowance.

## D-055 — The factory owns its nightly cycle (2026-09-22) — VERIFIED (task settings) / monitor run in progress
The 03:30 "AIFactory Monitor" task did not fire on 2026-09-22: it was created with `schtasks /Create` defaults, which
set `DisallowStartIfOnBatteries=True` and no catch-up — the laptop was on battery. Decision:
1. Task re-registered via `Register-ScheduledTask` with AllowStartIfOnBatteries, DontStopIfGoingOnBatteries,
   StartWhenAvailable (catch-up), 6 h limit, and the action now points at the repo's `scripts/windows/run-monitor.ps1`
   (the hand-copied `C:\AI\Factory\tools\run-monitor.ps1` was archived).
2. Belt and braces: the daily `report` job enqueues a full `monitor` for today if none exists, using the exact
   scheduler payload so the idem key dedups either way. The factory no longer depends on Task Scheduler for its
   nightly re-verification; the scheduler is just the preferred trigger.
Also observed: the Cloudflare quick tunnel rotated hostname at ~03:26; the supervisor republished `run/tunnel.txt`
and `~/bin/laptop` self-healed within ~3 minutes. Recorded in RECOVERY.md.

## D-056 — Repair rounds rotate to a lane that has not yet failed the bot (2026-09-22) — VERIFIED (unit)
Evidence: bot 012/013 repairs burned two rounds on `groq:qwen/qwen3.8-27b` producing near-identical instructions.
`fp.chat(skip=)` skips lanes that already produced a rejected/failed candidate for this bot; a repeat is only allowed
when every other lane is down. Cheap diversity instead of asking the same model to disagree with itself.

## D-057 — Self-improvement stage 1: the factory reviews itself, proposes, never self-applies (2026-09-22) — VERIFIED
`tools/factory_insight.py` reads the audit table (bot.tested, bot.repair, security.violation, paused jobs) and the
registry (bench coverage, weak lanes) and writes `proposals/<date>.md|json`: one section per recurring pattern with
evidence, a concrete suggestion, and whether an *already-approved* mechanism can act (bench a lane with no score,
probe after timeouts). Only those mechanisms are auto-enqueued (audited `factory.proposals`); anything touching
factory code or policy is left for review. Runs weekly (Monday, chained from the daily report) or `add insight`.
First live run (3-day window) found: 2 context-overflow failures (bot 007) that the old classifier mislabelled,
4 unbenched lanes incl. the primary (→ bench enqueued), repair success 2/5, groq-qwen27b 2/4. Two of those led
directly to D-058 and the classifier fix. This is the propose→review loop from the contract; sandboxed self-patching
is deliberately NOT built yet.

## D-058 — Primary lane is chosen by measured quality within budget reality (2026-09-22) — VERIFIED
`default_primary()`: best benchmarked lane with ≥0.9 pass over its window, not quota-cooled, and with a real daily
budget (`rpd` unknown or ≥200, and not an account-wide/shared 50-per-day pool); otherwise the legacy constant
`groq-gptoss120b`. Live: OpenRouter lanes score 4/4 but share 50 req/day, so they stay fallbacks; groq-gptoss120b
remains primary until its own bench score exists (queued by D-057). Fallback ranking unchanged (D-050), primary
excluded. Quota-cooled lanes stay valid *policy* members (the live chain skips them at call time).

## D-059 — Judge the whole RESULT block; repair re-verifies before rewriting (2026-09-22) — VERIFIED (replay) / live pending
The first full nightly monitor (b59e7101, 14 bots) demoted 8 of them at once. Replaying the saved logs offline showed
the *judge* was wrong for 6 of the 10 misses: the runner compared the expected token against the last physical line,
but Rich wraps long replies at ~80 columns inside a PowerShell job, so `RESULT: Wrote CHANGELOG.md with 3 entries…`
arrived split and only its tail was checked. Fixes:
1. `run-bot-tests.ps1` now takes the last `RESULT:|ANSWER:|OUTPUT:` line plus up to 3 continuation lines joined, and
   matches the token with punctuation/quote boundaries. Replay: 004/005/009/003 misses flip to PASS; 006 T1 (`ERROR`),
   007 T1 (did work instead of replying X_OK), 008 T2/T3 (wrote the file, never said the word) remain genuine failures.
2. `repair()` re-runs the suite unchanged first. Pass → promote, no model call, no rewrite (`reverified: true`).
   Fail → proceed with fresh evidence. A repair may never churn a healthy bot because the judge or a lane had a bad day.
Why not just re-test: the monitor→repair chain is already the recovery path; adding a retest job would be a third
state machine for the same question.

## D-060 — The master is re-verified, never "repaired" (2026-09-22) — VERIFIED
Bot 001 is hand-wired (`config/laptop/workspace`, no spec). The monitor demoted it (2 timeouts on the 5-test suite)
and the chain enqueued a repair that crashed on the missing spec. Now: a demoted 001 gets `monitor --only 001` 30 min
later; repair refuses spec-less bots with a clean `logic` error. Persistent master failure surfaces in the daily
report for the owner rather than being auto-rewritten.

## D-061 — Re-architect allowance = default ∪ the bot's already-granted permissions (2026-09-22) — VERIFIED
016 (built under an explicit `shell:workspace` grant) failed a monitor test, repair paused (`logic`: tests need
write_file), rearchitect then paused as `security` because the rearchitect job carried only the default allowance.
A grant given at create time is part of the bot's approved boundary; rearchitect may keep it (never widen beyond
it). Live: resumed → rearchitected within `[exec]/[shell:workspace]` → 4/4 → active.

## D-062 — The master's chain follows the factory routing policy (2026-09-22) — VERIFIED (config) / monitor pending
Root cause of 001's 1/5: `config.json` had a hand-wired chain `groq-qwen27b → groq-gptoss120b → groq-gptoss20b →
local4b`. When Groq's daily quota for qwen ended, every master call spent minutes rotating inside one provider and
the local 4B tail timed out under the 240 s cap. `factory_presets.sync()` now also writes `agents.defaults.modelPreset`
and `fallbackModels` from `default_primary()`/`default_fallbacks()` (bench-ranked, budget-aware, cross-provider, local
tail) and is re-run after every probe and bench. Live result: `groq-gptoss120b → or-ling-30-flash-vl → or-nex-n25-pro
→ gemini-gemma26b → groq-qwen27b → groq-gptoss20b → local3b`; config hygiene still healthy (40 KB).

## D-063 — Bots do real work: `run` (2026-09-22) — VERIFIED live
Until now a bot's only execution path was its own acceptance suite. `scripts/windows/run-bot-task.ps1` runs one task
with the identical isolation (per-bot config, disabled tools, template dir, live chain) but stages owner input files
in and captures produced/changed files out, leaving the bundle clean. `tools/factory_run.py` runs a bot or a whole
plan: steps resolved from the plan's create jobs / `plan.reused` audits, step N's outputs staged as step N+1's inputs,
each step's declared `produces` enforced (missing output = failed run, never silent). Worker `run` kind audits
`bot.ran` per step; quota → transient retry, other failures → logic pause. Master: `queue run`.
Live: plan 25a47cdb on an 11-line app.log → 013 wrote errors.txt (6 lines, exact) → 014 wrote summary.txt
(`Total: 6`, 3/2/1 top messages, exact). Output dir `run/runs/plan-25a47cdb-20260922-075757`.

## D-064 — Owner ⇄ master loop for real work (2026-09-22) — VERIFIED live
Input contract: owner drops files in `workspace/inbox/<name>/`; the master only ever names that folder (nanobot's
exec guard correctly refuses outside paths — first attempt with an absolute run path was blocked, which is the
desired behaviour). `factory.py job <id>` gives the master a compact, audit-derived outcome (state, class, error,
bots created/ran, files produced, child jobs); `factory.py runs` lists run outputs.
Live, in chat: "I put a log file in inbox/logs-sep22. Run the log triage pipeline on it" → `dir inbox` →
`queue run --plan 25a47cdb --in logs-sep22` → job f230e382 done (013 → 6 errors, 014 → summary.txt). Then
"How did job f230e382 go?" → master answered from `factory.py job`.

## D-065 — Create resumes at the test stage after a crash; never a duplicate bot (2026-09-22) — VERIFIED live
Persistent-job gap: a `create` that died between build and verdict was re-claimed and rebuilt a *second* bot (new id)
while the half-built one sat in `testing`. Now `bot.created` is audited the moment the bundle exists (`on_built`
callback inside `cmd_create`), and a re-claimed create first looks for its own `bot.created` — if that bot is
`building/testing` it resumes with `cmd_test` and audits `job.resumed_at`. Live kill test (job 1c4af272): worker
killed mid-test → lease expired → attempt 2 → `job.resumed_at stage=test` → 017 tested, registry still 17 bots, no 018.

## D-066 — Deliver: objective + files → built, verified, run, result — one message (2026-09-22) — VERIFIED live
`--then-run <inbox>` on `create`/`plan` is carried through every descendant (retest, repair, rearchitect) via
`_carry()`. `_maybe_deliver()` fires whenever a bot turns active and enqueues the `run` — for a plan only once every
step's bot is active (idempotent by idem key), for a single-bot objective immediately with the objective as task.
Live, in master chat: "I put orders.csv in inbox/orders. I need a bot that … Build it and then run it on my file."
→ `queue create "…" --then-run orders` (job fbeb65ad) → bot 018 csv-country-totals built, 4/4, active → child run
ca31fcf3 → `totals.csv` = UK 370.25 / DE 1510.50 / US 2480.00 (exact). The full loop objective → plan → create →
test → verify → register → run → deliver (→ monitor → repair) is closed with no human in it.

## D-067 — Durable audit trail in git (2026-09-22) — VERIFIED
The audit table lived only in the laptop's SQLite (gitignored); AUDIT.md carried the last 400 rows. Now every
job end appends new rows exactly once to `audit/YYYY-MM.jsonl` (high-water mark by seq), committed with state by
both the worker and repo-sync; `proposals/` is committed the same way. 421 events back to the first build are in
the repo. Found and fixed on the way: `C:\AI\Factory\tools\repo-sync.ps1` was a stale hand-copy that silently
ignored new state paths — it is now a 4-line shim that runs the repo's script (one source of truth, same rule as
D-050 for the test runner).

## D-068 — Bundle integrity seal (2026-09-22) — VERIFIED
Bot behaviour is defined by four files in its bundle (bot.json, nanobot.patch.json, AGENTS.md, SOUL.md). Until now
anything on the laptop could edit them and the bot would still run as "active/VERIFIED". Now `BotFactory.build`
records a sha256 seal of those files in the registry entry (git-tracked, so a laptop-side edit cannot also fix the
seal); `run` and `test` refuse a drifted bundle with an explicit error; rebuild/repair (which go through build) reseal.
memory/ and templates/ are deliberately unsealed (bots learn). Legacy entries were sealed once in place (16 bots);
an entry with no seal is reported `<unsealed>` but not blocked, so old registries keep working.

## D-069 — Free-first scout: more providers, needs_owner, retirement (2026-09-22) — VERIFIED
Discovery only knew OpenRouter. 2026 research (docs/FREE_PROVIDERS_2026-09-19.md + addendum) shows Cerebras, NVIDIA
NIM and Mistral Experiment as free, no-card, OpenAI-compatible, tool-capable. They are now providers in the probe /
discover path. Rule kept from D-047: the factory never signs up on the owner's behalf — with no key, `discover`
records one `needs_owner` verdict per provider (7-day dedup) and STATUS.md prints
`ACTION REQUIRED (owner): provider:cerebras — set CEREBRAS_API_KEY (User env) after signing up: https://cloud.cerebras.ai …`;
the notice clears itself when the key appears. (Bug found: STATUS.md read the ledger at the wrong JSON level, so no
needs_owner ever showed — fixed.) The hourly probe now fans discover out to all four providers when a lane blocks or
the healthy pool is thin. Lanes BLOCKED as *gone* (404/decommissioned) for 3 days are retired from the registry with a
ledger reject so they cannot be re-discovered under the same slug; quota/auth/error blocks still self-heal.

## D-070 — Owner grants via master chat (2026-09-22) — VERIFIED
A create whose objective needs a permission outside the default allowance pauses (class security) — exercised live
for the first time today (bot 019 pytest-runner needed shell:workspace; job 123271bb). The master now has
`factory.py approve <job> --allow …` and an AGENTS rule: name the exact permission, ask the owner yes/no, never
self-approve, never request shell:system (refused by the worker anyway). Live: master chat → blocked → asked → owner
"yes" → `job.payload_patched` + `job.resumed` audited (job e89cc0ba).

## D-071 — Keep-awake during jobs (2026-09-22) — VERIFIED (code) / INFERRED (effect)
Laptop is Modern Standby; it slept twice today mid-job (bench lease expired, tunnel down 15 min). The worker now holds
`SetThreadExecutionState(ES_SYSTEM_REQUIRED|ES_AWAYMODE_REQUIRED)` only while a job is in flight. No powercfg changes
(owner's machine settings untouched).

## D-072 — Monitor fans out (2026-09-22) — VERIFIED (unit) / live pending
The nightly monitor tested every active bot inside ONE job: 17 bots × ~2–3 min = a 40-minute lease that blocked owner
work and, on a sleep, lost all progress. Monitor is now a tiny job that enqueues one priority-6 `test` per active bot
(owner work at priority ≤5 interleaves); each per-bot test is independently leased/resumable, writes its MONITOR.md
row, and demote→repair happens in the test handler exactly as before (D-051 inconclusive rule kept).

## D-073 — Reward-hack rejections point at the test, not the bot (2026-09-22) — VERIFIED (unit) / live on bot 019
Bot 019's T2 expected the literal "Status: PASS"; any honest instruction ("write Status: PASS/FAIL") trips the
reward-hacking guard, so both repair rounds were rejected and the job paused as logic. Rule: when EVERY repair
candidate is rejected for reward hacking, the defect is the test literal → escalate once to rearchitect (D-052 path)
with that feedback; the architect prompt now requires post-liveness expected values to be computed, not quoted.

## D-074 — Worker self-test gate (2026-09-22) — VERIFIED (positive + negative, live)
pytest is now installed on the laptop (first full laptop run: 73/73 after a utf-8 fix in tests). The worker runs
core/tests once per code stamp before processing jobs; red ⇒ `worker.blocked_by_tests`, STATUS "WORKER BLOCKED",
waits for the next push. Proven by pushing a deliberately failing test (gate returned False, "1 failed") and reverting.

## D-075 — Timeouts are availability, not quality (2026-09-22) — VERIFIED (unit) / live on 005
Bot 005 was demoted at 17:15 by two 300-s TIMEOUTs with empty replies (lanes saturated by the monitor fan-out); repair
then "failed" with 2/4 sandbox scores for the same reason. The runner now counts TIMEOUT-with-no-answer separately
(`timeouts`), and test/monitor treat them exactly like D-051 quota: inconclusive, re-test in 2 h, never demote.
A wrong answer among the failures still demotes.

## D-076 — Schedules: recurring bot work (2026-09-22) — VERIFIED (unit) / live pending
Bot specs allowed `schedules` (cron strings) but nothing ever fired them. Now: `registry/schedules.json` (git-tracked)
holds owner/master-created schedules for ACTIVE bots; an hourly self-chaining `tick` job enqueues one `run` per due
schedule, idempotent per (schedule, slot) so a restart or a slept laptop never double-runs and catches up exactly once.
Own 5-field cron parser in core/factory/cron.py (no dependency). Master: "every morning run 018 on orders" →
`factory.py schedule add 018 "0 7 * * *" --task … --in orders`. Same inbox-name contract as `queue run` (D-064).

## D-077 — Recurring chains can't die (2026-09-22) — VERIFIED (unit) / live pending
Root cause of today's timeouts on bots 003/004/005: the hourly probe chain ended on 21 Sep 21:xx when a probe job
failed (`logic`) before enqueuing its successor; lane health went ~22 h stale, so chains still listed Gemini lanes
that were quota-exhausted and every test burned 60–70 s per model call on 429 retries before reaching a live lane.
Fixes: (1) a probe enqueues its successor BEFORE probing; (2) on every worker start `ensure_recurring` re-seeds
probe/tick/report if no queued/running successor exists (idempotent per hour/day). The bots were never broken —
which is exactly what D-075 now assumes for pure timeouts.

## D-079 — Two workers: slow + fast lane, per-bot exclusion (2026-09-22) — VERIFIED (unit) / live pending
One worker meant a 30-minute create/repair blocked every owner run, schedule and hourly probe behind it (today the
probe chain waited 40 min behind a repair). The supervisor now also starts a `--fast-lane` worker that only claims
run/test/tick/probe/report/discover. Safety: `JobStore.claim` never hands out a job for a bot that another running
job already holds (atomic in the same BEGIN IMMEDIATE), so bundle/registry writes for one bot stay serialized; the
git state commit/rebase/push is serialized by `run/git-state.lock`. Registry JSON writes are whole-file, so
different-bot concurrency is safe.

## D-080 — Event-driven lane cooldown (2026-09-22) — VERIFIED (unit + regex on real 429 text)
The hourly probe is too slow a signal: bot 004's repair burned two rounds on groq-gptoss120b after it hit its daily
token cap (200k TPD) — the probe had said "ok" 40 minutes earlier. Now `run-bot-tests.ps1` emits a `QUOTAHIT
{model,secs}` line for every 429 it sees (Groq "try again in 11m14s" and Gemini `retryDelay` parsed; default 900 s),
and `run_tests()` calls `factory_probe.mark_quota()` which sets `health.quota_until = now + retry_after` on the matching
lane at once. The next `resolve_chain` (every test/run/repair round re-resolves, D-040) skips it. A later probe `ok`
clears it as before. No new state: same `quota_until` field the probe already uses.

## D-081 — Lease re-adoption after sleep (2026-09-22) — VERIFIED (unit) / live pending
Observed: laptop entered Modern Standby 20:36–21:24 while `svc-` was mid-repair (349607da). On wake the fast-lane
worker's claim() expired the lease → job back to `queued` (attempt still 1) while `svc-` was still running the very
same job. Two risks: a second worker claims it → duplicate, overlapping bundle writes; or the first finishes and
`done()` stamps a job it no longer owns. Fix: `heartbeat()` now returns ok|readopted|lost — if the lease was expired
and nobody took the job, the running worker re-adopts atomically (`job.readopted`); if another worker holds it, the
first worker discards its result (`job.orphaned_result`) instead of writing. Both paths checked before `done()`/`fail()`.
Power: `powercfg` standby timeouts set to 0 on AC (was already 0) and Modern Standby network kept connected
(`powercfg /setacvalueindex … CONNECTIVITYINSTANDBY 1`) so a sleeping laptop at least keeps the tunnel up; a sleep on
battery still pauses work — that is acceptable, resumption is now safe.

## D-082 — Quota-bound sandbox scores are inconclusive (2026-09-22) — VERIFIED (unit)
Repair round 1 of bot 004 scored 1/4 on a candidate whose only fault was that the lane hit Groq's daily token cap
mid-run; the round was burned and a possibly-good rewrite discarded. Now: if a sandbox run has quota/timeouts > 0 and
did not pass, the SAME candidate is run once more (D-080 has just cooled the offending lanes; D-040 re-resolves the
chain). Only that second, clean result counts. Logged as an extra `inconclusive: true` round entry so the audit shows
both scores. Costs at most one extra test suite per round; never changes the candidate, permissions or spec.

## D-083 — Master integrity seal (2026-09-22) — VERIFIED (unit) / live below
The 20 bots were sealed (D-068) but the master 001 — the one bot with exec and the factory wrapper — was not, because
it has no bundle. Its security surface is: workspace `AGENTS.md` (behavioural rules incl. NEEDS_OWNER), `tools/factory.py`
(what exec can reach), and `config.json → tools.exec` (deny patterns, allowedEnvKeys, timeout). `seal-master` hashes
those three (config reduced to the exec object so lane rotation is never "tampering") into the registry entry;
`wire-master-factory.ps1` reseals after it writes them; `test 001` refuses to run (and so can never re-verify) when
they drift. Self-improvement that widened the master's env keys or rewrote its rules would be caught at the next test.

## D-084 — Discovery: account quota ≠ model verdict (2026-09-22) — VERIFIED (unit)
Today's 21:24 discover job recorded 13 OpenRouter candidates (nemotron-3-super/ultra, gemma-4-31b, laguna, …) as
`rejected` for 7 days — every one because the OpenRouter free-models-per-day cap was already spent, not because the
models failed. That is the "popularity ≠ evidence" rule violated in reverse: no evidence ≠ rejection. Now a 429 during
discovery marks the candidate `deferred` (6 h), stops probing that provider for the window (`provider-quota:<p>`),
and the next run re-evaluates the slug. Today's 13 verdicts migrated to deferred (already expired) so the next hourly
discover re-tries them once the cap rolls over.

## D-085 — Bench: timeouts scored as availability (2026-09-22) — VERIFIED (unit)
`factory_bench.record()` only discounted 429s; a TIMEOUT test (D-075 already treats it as availability for bot status)
still counted as a quality failure against the lane. Now `timeouts` is passed through and summed with `quota`.

## D-086 — Whole-sweep error = local outage (2026-09-22) — VERIFIED (unit + live evidence)
Probe 60d56672 at 20:17Z (laptop entering standby, Wi-Fi in "Adaptive Connected Standby") returned `error` for all
13 remote lanes across 3 providers and incremented every `failures` counter; two lanes reached 2 of the 3 that
trigger BLOCKED. Thirteen providers do not fail simultaneously — we do. `factory_probe.run()` now detects an
all-remote-error sweep spanning ≥2 providers, records nothing, and the worker re-queues a probe in 10 min
(`probe.network_down`). Counters from that sweep reset to 0.

## D-087 — Groq presets: TPM is not a context window (2026-09-22) — VERIFIED (config) / test pending Groq TPD reset
Groq presets carried `contextWindowTokens: 8200` (from the 8k **tokens-per-minute** cap, D-015). nanobot's context
governor derives a ~6.4k input budget from that and raises `ContextWindowExceededError` *locally* — before any
request — so bot 007 T2/T3 (6586 / 7200 tokens) failed with no provider call and therefore no fallback. Set to 16384:
requests under 8k go through; over 8k Groq answers 413 (TPM), which the fallback patch already routes to the next
lane. `factory_presets.sync` now updates existing presets when the policy changes (live: 3 presets → 16384).

## D-088 — Daily caps cool for ≥1 h and outlast probe successes (2026-09-22) — VERIFIED (unit + live evidence)
Live evidence 22:15–22:40Z: gpt-oss-20b TPD 199,120/200,000 → "try again in 8m13s" → after 10 min: 199,515/200,000
→ "try again in 10m29s". The retry-after is when ONE request fits the rolling window, not when the day is over; and
the hourly probe (≈50 tokens) succeeded in between and cleared `quota_until`, so chains kept sending real work to a
lane that could only serve probes. Now the runner tags each 429 `kind=tpd|rpd|tpm`; daily kinds cool ≥ 3600 s and a
probe `ok` does not clear them until the window ends. Groq TPD is per model per org (measured), so the sibling Groq
lanes stay usable until their own caps.

## D-089 — repo-sync must not hard-reset on a dirty tree (2026-09-22) — VERIFIED (live repro)
`run/selftest.json` was tracked (added by an early `git add -A` before its ignore rule). Every worker self-test
modified it → `git rebase` refused with "unstaged changes" → repo-sync's conflict branch ran `reset --hard
origin/main`, silently discarding any uncommitted registry edit on the laptop (observed: the D-086 counter reset had to
be applied twice). Fix: file untracked; repo-sync auto-stashes (incl. untracked) around the rebase and restores after.

## D-090 — Bench never runs on a cooling/BLOCKED lane (2026-09-22) — VERIFIED (unit)
The nightly `bench --stale-only` picked lanes by score age only; a lane in a daily-cap cooldown produced a 20-minute
inconclusive run (gemini-lite 1/4 in 618 s today). `factory_bench.run()` now drops BLOCKED and `quota_until` lanes up
front (`skipped_cooling` in the result) so the reference bot's time and the shared provider budget go to lanes that
can actually be scored.

## D-091 — Audit hash chain (2026-09-22) — VERIFIED (unit)
`audit/*.jsonl` (D-067) was append-only by convention; nothing detected an edited or deleted row. Each exported row
now carries `prev` (previous row's hash) and `h` = sha256(seq,ts,job,bot,event,actor,detail,prev)[:16]. The chain
continues across sync calls and month files. `factory_worker.py audit-verify` walks it; rows written before D-091
(733 today) are counted but not hashed — the chain starts after them. Repair/promotion/permission events are therefore
tamper-evident in git, not just present.

## D-092 — Builder-side 429s cool lanes too (2026-09-22) — VERIFIED (unit)
D-080/D-088 covered 429s seen by bot test runs; the builder's own `chat()` (architect, planner, repair rewrite, insight)
just rotated to the next lane and left the registry unaware. Now every HTTP 429/413/rate_limit/RESOURCE_EXHAUSTED in
`chat()` runs the same parse (retry-after, daily vs minute) and `mark_quota()` — one rule, two entry points.

## D-093 — spec_consistency catches shell-needing tests (2026-09-22) — VERIFIED (unit + 22 existing specs clean)
Bot 019 failed CAPABILITY_MISSING because its tests said "run pytest" while tools were read/write only; repair is
tool-frozen so it could never recover. `_SHELL_HINT` (run/execute pytest|python|npm|git|docker|…) now rejects such a
spec at architect time unless `exec` + `shell:workspace` are granted, and `exec` without `shell:workspace` is rejected.
