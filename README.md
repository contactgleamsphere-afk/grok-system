# grok-system

Free, open-source, self-hosted **Grok-like** multi-agent AI system.

**Status (2026-09-18):** Phase 1 VERIFIED on laptop (nanobot 0.3.5 + Ollama + qwen2.5:3b). Core package (`core/factory`) with registries, model router and bot-spec validator — 19 tests passing. See **BUILD_STATE.md** for what is actually true right now.

## Layout (current)
```
core/factory/     registry.py · router.py · botspec.py   (CORE layer, tested)
core/tests/       pytest suite
registry/         models.json · tools.json · bots.json   (machine-readable truth)
*_REGISTRY.md     generated from registry/ — do not hand-edit
config/laptop/    SOUL.md · AGENTS.md (Master 001 identity)
scripts/windows/  install-phase1.ps1
docs/phases/      per-phase execution prompts
BUILD_STATE.md · DECISIONS.md · CHANGELOG.md · TEST_RESULTS.md · RECOVERY.md · COMPONENT_REGISTRY.md
```

## Goals

- Deep research, GitHub work, code gen/modify, run/test/debug
- Multi-agent delegation, persistent memory, MCP tools, browser automation
- Discover and integrate useful open-source capabilities
- Improve its own architecture over time
- **Minimise paid AI APIs** — prefer local/self-hosted models and tools

## Non-goals (v1)

- Depending on Cursor / Grok Bot / OpenAI / Anthropic as the permanent brain
- Rebranding Open WebUI at scale (licence branding clause)
- Blind installs of popular repos without licence/security review

## Recommended stack (Recipe A — local-first modular)

| Layer | Primary pick | Licence | Role |
|-------|--------------|---------|------|
| Inference | [ollama/ollama](https://github.com/ollama/ollama) | MIT | Local OpenAI-compatible API |
| Engine (optional) | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | MIT | Lower-level GGUF runtime |
| Agent harness | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | MIT | WebUI, memory, MCP, multi-agent, cron |
| Coding CLI | [Aider-AI/aider](https://github.com/Aider-AI/aider) | Apache-2.0 | Git-native pair programming |
| IDE agents | [cline/cline](https://github.com/cline/cline), [continuedev/continue](https://github.com/continuedev/continue) | Apache-2.0 | In-editor autonomous coding |
| Coding control plane | [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | MIT | Agent Canvas + Docker sandbox |
| Sandboxed coder | [openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter) | Apache-2.0 | Terminal agent with OS sandbox |
| Browser | [browser-use/browser-use](https://github.com/browser-use/browser-use) + Playwright | MIT / Apache | Browser agents (force local LLM) |
| MCP tools | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers), [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | mixed / Apache | Tool servers |
| RAG UI (optional) | [Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm) | MIT | Local docs + agents UI |
| Orchestration lib | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | MIT | Task graphs / planning |
| Multi-agent lib | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | MIT | Role crews (**disable telemetry**) |
| Memory | nanobot Dream → optional [mem0ai/mem0](https://github.com/mem0ai/mem0) / [letta-ai/letta](https://github.com/letta-ai/letta) + [qdrant/qdrant](https://github.com/qdrant/qdrant) | Apache | Persistent memory |
| Research agent | [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) | Apache-2.0 | Deep web research |

**Reject as core:** [open-webui/open-webui](https://github.com/open-webui/open-webui) (custom branding licence), archived Cursor clones, AGPL surprises without explicit accept.

## Docs

- [Capability audit (verified)](docs/CAPABILITY_AUDIT.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Install order (host)](docs/INSTALL_ORDER.md)
- [Security](docs/SECURITY.md)
- [Stack recipes](docs/STACK_RECIPES.md)
- [Research addendum](docs/RESEARCH_ADDENDUM.md)

## Repo layout

```
docs/           architecture, audit, security
stack/          version pins and compose stubs (no live installs yet)
config/         example configs (Ollama, nanobot, MCP)
scripts/        host bootstrap helpers (documented; run on YOUR machine)
```

## Bootstrap environment note

This repository is built with assistance from a Grok Bot session that can operate GitHub and a Linux box. That box has **no Docker and no GPU/Ollama**. The production brain must run on **your laptop or a VPS**.

## Licence

MIT for *this* monorepo’s original files. Third-party projects keep their own licences — see docs.
