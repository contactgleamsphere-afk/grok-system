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
