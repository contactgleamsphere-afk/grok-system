# DECISIONS

| ID | Date | Decision | Why | Revisit when |
|---|---|---|---|---|
| D-001 | 2026-09-18 | nanobot 0.3.5 is the **provisional** core runtime | Only verified option that gives native fallback chains, subagents, cron/heartbeat, MCP, multi-instance isolation, Ollama, MIT — on Windows without Docker | Docker/WSL2 available; or OpenClaw/Hermes/Agent Zero prove better in a sandboxed trial |
| D-002 | 2026-09-18 | This repo is the source of truth; registries are JSON, markdown is generated | Portable, diffable, recoverable if laptop dies | never |
| D-003 | 2026-09-18 | Model choice is benchmark-driven, never assumed | 3B tool-calling unproven; qwen3-4b/8b candidates | after Phase 0 |
| D-004 | 2026-09-18 | Router ranks by capability/locality/quality, excludes by cooldown — not by raw failure count | Test proved failure-count ranking starves models of retries so they never recover | never |
| D-005 | 2026-09-18 | Bot Factory enforces least privilege in the spec validator: high-risk tools need explicit permission; `shell:system` ungrantable | Security §17 | when OS sandbox exists |
| D-006 | 2026-09-18 | Arena agent = architect+builder with GitHub; laptop via Grok until tunnel exists | Owner instruction | tunnel live |
