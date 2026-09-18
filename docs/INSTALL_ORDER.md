# Install order (on YOUR host — not yet executed)

Do not run these on the Grok Bot box expecting a permanent brain (no Docker, no GPU).

1. **Pick host** — laptop (≥16 GB RAM ideal) or VPS.
2. **Enable Local Computer / SSH** so automation can reach the host if desired.
3. **Install Docker Engine** (recommended) — unlocks OpenHands sandbox & compose.
4. **Install Ollama** → pull a small chat model + embedding model → `curl localhost:11434`.
5. **Install nanobot** → provider = Ollama → verify WebUI with **no** cloud API keys.
6. **Add MCP servers** (filesystem, git, fetch) from `modelcontextprotocol/servers`.
7. **Install Aider** → point at Ollama OpenAI-compatible endpoint.
8. **Optional:** Cline and/or Continue in your editor (same Ollama endpoint).
9. **Optional:** Qdrant + local embeddings; or keep nanobot Dream only.
10. **Optional:** AnythingLLM for doc RAG (MIT).
11. **Optional:** OpenHands Agent Canvas **after** Docker works.
12. **Optional:** browser-use in a venv; force local LLM; isolated browser profile.
13. **Optional:** gpt-researcher for deep research lane.
14. **Wire compose** from `stack/docker-compose.stub.yml` once Docker exists.

CrewAI (if used): set `OTEL_SDK_DISABLED=true` to disable anonymous telemetry.
