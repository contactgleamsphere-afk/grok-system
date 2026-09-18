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
