# Research addendum (2026-09-18)

Supplementary candidates from a second read-only GitHub pass. Merged with the verified capability audit.

## Upgrades vs first audit

| Area | First pick | Addendum upgrade |
|------|------------|------------------|
| RAG UI | (avoid Open WebUI as core) | **AnythingLLM** (MIT) preferred |
| IDE coding | Aider | Add **Cline** + **Continue** |
| Long-term memory agents | mem0 / nanobot Dream | Add **Letta** |
| Sandboxed coding | OpenHands Docker | Add **openinterpreter** |
| Browser MCP | Playwright via npx | Add **microsoft/playwright-mcp** |
| Inference alt | Ollama / llama.cpp | **LocalAI** as multi-backend alt; **vLLM** if GPU farm |
| Research | web tools | **gpt-researcher**, Haystack pipelines |

## Extra rejects / caution

- voideditor/void — archived
- OpenViking — AGPL
- Daytona — LICENSE unverified at research time
- Autogen — verify LICENSE vs SPDX CC-BY-4.0 metadata
- Perplexica canonical path — UNVERIFIED (possible rename)
- browser-use / mem0 — free OSS but defaults/docs push paid cloud paths; configure local-only

## CrewAI

MIT, Ollama-capable, but **anonymous telemetry on by default** — disable with `OTEL_SDK_DISABLED=true`.
