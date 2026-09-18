# Capability Audit — Free Open-Source Grok-like System
**Date:** 2026-09-18 (Europe/London)  
**Auditor context:** Grok Bot box + GitHub MCP (account `contactgleamsphere-afk`)  
**Rule:** Only claims below marked VERIFIED were exercised in this session. Nothing installed for the target system.

---

## Scope note (important)

This audit covers **two layers**:

1. **Bootstrap environment (this Grok Bot):** what *I* can do today to design/build for you.
2. **Target system (yours):** what must exist on *your* hardware / self-hosted stack so the product is free of paid AI platforms.

Grok Bot itself is a **usage-limited commercial platform**. It is useful as a factory floor, not as the long-term runtime for your free system.

Probe artifacts created during verification (safe to delete):
- Repo: https://github.com/contactgleamsphere-afk/capability-audit-probe
- Draft PR: https://github.com/contactgleamsphere-afk/capability-audit-probe/pull/1

---

## A. Current capabilities (bootstrap — VERIFIED where noted)

| Capability | Classification | Evidence |
|---|---|---|
| Read GitHub (public files) | **AVAILABLE** | `get_file_contents` on `octocat/Hello-World` → “Hello World!” |
| Read authenticated user | **AVAILABLE** | `get_me` → `contactgleamsphere-afk` (account created 2026-09-18, 0 public repos) |
| Create repository | **AVAILABLE** | Created private `capability-audit-probe` |
| Create branch | **AVAILABLE** | Created `audit-write-probe` (and `audit/write-probe`) |
| Modify files + commit via API | **AVAILABLE** | `create_or_update_file` wrote `AUDIT_PROBE.md` |
| Create pull request | **AVAILABLE** | Draft PR #1 opened |
| GitHub search (user-scoped) | **AVAILABLE WITH CAVEAT** | `search_repositories user:contactgleamsphere-afk` failed validation (new/private visibility); public/global search works |
| Shell `gh` CLI authenticated | **AVAILABLE WITH CONFIGURATION** | `gh` installed (2.46.0) but `gh auth status` = not logged in; MCP holds the PAT, shell does not |
| Cursor Cloud Agent on GitHub repos | **AVAILABLE WITH CONFIGURATION** | `CloudAgent repositories` → no SCM integration on Cursor account (separate from GitHub MCP) |
| Execute shell on box | **AVAILABLE** | Multiple commands succeeded |
| Run Python | **AVAILABLE** | Python 3.13.5 |
| Run Node.js | **AVAILABLE** | Node v20.19.2, npm 9.2.0 |
| Install Python packages | **AVAILABLE WITH CONFIGURATION** | System pip blocked (PEP 668); **venv works** (`python3 -m venv` + pip install verified) |
| Install Node packages | **AVAILABLE** | `npm install -g cowsay` succeeded |
| Run Docker | **NOT AVAILABLE** (on box) | `docker: command not found`; `apt-get install -s docker.io` → package not in apt sources |
| Podman | **NOT AVAILABLE** | not found |
| Access box filesystem R/W | **AVAILABLE** | `/workspace` and `/home/box` write tests passed; ~113 GB free of 126 GB |
| Browse the web (search/fetch) | **AVAILABLE** | `WebSearch` returned live results; `curl` to example.com OK |
| Download / clone repositories | **AVAILABLE** | `git clone --depth 1` of public repo succeeded |
| Execute downloaded code | **AVAILABLE** (with risk) | Box can run cloned code; no strong sandbox beyond OS user |
| Run tests | **AVAILABLE WITH CONFIGURATION** | `pytest` not preinstalled; `npx jest` works (30.5.2); can install pytest in venv |
| Deploy software | **PARTIAL / REQUIRES ANOTHER TOOL** | Can run long processes on box; no Docker; no verified public deploy pipeline; Cloud Agent Origin/Vercel path is platform-tied |
| Use MCP servers | **AVAILABLE** | `user-Github` connected (45 tools); can `InstallPlugin` / `AddMcpServer` with approval |
| Call external APIs | **AVAILABLE** | Network egress works; credentials must be supplied |
| Persistent memory (platform) | **AVAILABLE** | Agent memory/profile via platform tools (not portable OSS) |
| Scheduled / background tasks | **AVAILABLE** | Routines (cron/event) + background subagents + shell jobs |
| Create other agents | **AVAILABLE** | `CreateAgent` / channels (Grok Bot teammates — platform-tied) |
| Multi-agent delegation (platform) | **AVAILABLE** | `Task` executor / computerUse / peer agents |
| Browser automation (box desktop) | **AVAILABLE** | computerUse subagent + Playwright via `npx` (1.63.0 verified) |
| Local LLM inference on box | **NOT AVAILABLE** | No `ollama`, no `nvidia-smi`/GPU, ~15 GiB RAM shared, CPU-only Xeon |
| Operate on user laptop | **AVAILABLE WITH CONFIGURATION** | Machine `LAPTOP-LRE6PSA8` registered & connected; local Shell was **denied** this session (needs Local Computer approval) |
| Languages/tooling on box | **AVAILABLE** | git, gcc, rustc 1.85, go 1.24, uv, jq, rg, ffmpeg, sudo (passwordless) |
| 1Password / saved logins | **NOT AVAILABLE** | Credential provider not connected |
| Autonomous planning (platform) | **AVAILABLE** | Planner behaviour in this agent; not a portable OSS planner you own |

### GitHub write quirks (VERIFIED)
- Branch names containing `/` (`audit/write-probe`) can fail Contents API file writes with “Branch not found”; simple names (`audit-write-probe`) worked.
- No `delete_repository` tool in the MCP surface — cleanup may need web UI or `gh` after auth.

---

## B. Missing capabilities (for the *target* free system)

These are **not** present as a self-owned, free, portable stack today:

1. **Local LLM runtime** (own weights, no paid API) — missing on box; laptop UNVERIFIED
2. **Owned agent orchestrator** (not Grok Bot) with tools, memory, multi-agent, scheduling
3. **Portable persistent memory** (vector + structured) you control
4. **Hardened code sandbox** (Docker/Firecracker/gVisor) — Docker absent on box
5. **Self-hosted coding agent** equivalent to Cloud Agent
6. **Self-hosted browser agent** stack you control end-to-end
7. **Self-improving skill/repo discovery loop** as first-class product feature
8. **Independent deploy/hosting story** for always-on agent (VPS/home server)
9. **GPU / sufficient RAM** for useful local models (box: insufficient; laptop: UNVERIFIED)
10. **gh CLI + Cursor SCM** wiring for dual GitHub paths

---

## C. Best candidate open-source projects (inspected; no install)

Criteria applied: free/OSS preference, local/self-host, licence, maintenance signal, paid-API independence, modularity. Stars are approximate from live GitHub search on 2026-09-18.

### 1. Local LLM inference
| Project | Licence | Notes | Verdict |
|---|---|---|---|
| **ollama/ollama** (~181k★) | **MIT** (file verified) | Simple local OpenAI-compatible API; active | **Primary pick** for ergonomics |
| **ggml-org/llama.cpp** (~129k★) | **MIT** (file verified) | Lower-level, maximum control, GGUF | **Secondary** / engine under many UIs |
| vLLM / llama.cpp+server | varies | Better throughput; heavier ops | Later if serving many requests |

**Caveat:** “Free software” ≠ “free electricity/GPU”. Useful 7B–14B models need RAM/VRAM you do not have on this box.

### 2. Agent orchestrator / personal Grok-like core
| Project | Licence | Notes | Verdict |
|---|---|---|---|
| **HKUDS/nanobot** (~48k★) | **MIT** (file verified) | Self-hosted; WebUI; memory (“Dream”); MCP; multi-agent; cron; OpenAI-compatible / Ollama / vLLM; chat apps | **Strong primary harness candidate** |
| **OpenHands/OpenHands** (~88k★) | **MIT** (file verified) | Agent Canvas + SDK; self-host docs; Docker sandbox option; BYO model | **Strong coding-agent control plane** |
| **crewAIInc/crewAI** (~59k★) | (typical Apache — confirm before ship) | Multi-agent roles | Library, not full product UI |
| **langchain-ai/langgraph** (~42k★) | OSS | Task graphs / durable workflows | Good **planning substrate**, not a product alone |

### 3. Persistent memory
| Project | Licence | Notes | Verdict |
|---|---|---|---|
| **mem0ai/mem0** (~66k★) | **Apache-2.0** (README) | OSS library + self-host server; **defaults to OpenAI** for LLM/embeddings unless reconfigured; cloud upsell | **Usable if forced local LLM+embedder** |
| nanobot built-in memory | MIT (via nanobot) | File/workspace memory + Dream | Prefer for v1 simplicity |
| **qdrant/qdrant** | **Apache-2.0** (file verified) | Vector DB self-host | Pair with local embeddings |
| Chroma / LanceDB | OSS | Lighter vectors | Fine for single-node |

### 4. Browser automation
| Project | Licence | Notes | Verdict |
|---|---|---|---|
| **browser-use/browser-use** (~115k★) | **MIT** (file verified) | Playwright-based browser agents | **Primary browser agent lib** |
| Playwright itself | Apache-2.0 | Already runnable via npx on box | Base layer |
| modelcontextprotocol/servers | various | Official MCP server collection | Tool ecosystem |

### 5. Coding / repo agent (Cloud Agent alternative)
| Project | Licence | Notes | Verdict |
|---|---|---|---|
| **Aider-AI/aider** (~49k★) | **Apache-2.0** (file verified) | Terminal pair-programmer; local LLMs supported per docs; git-native | **Primary local coding CLI** |
| OpenHands Agent Server / SDK | MIT | Heavier, more agentic | When you need sandbox + UI |
| Continue (continue-dev) | OSS | IDE-centric | Optional |

### 6. Chat UI over local models
| Project | Licence | Notes | Verdict |
|---|---|---|---|
| **open-webui/open-webui** (~152k★) | **Custom restrictive** (branding lock >50 users / 30 days) | Excellent UX but **not clean for rebrandable product** | **Reject as core** (optional personal-only) |
| nanobot WebUI | MIT | Part of harness | Prefer |

### 7. MCP ecosystem
| Project | Notes | Verdict |
|---|---|---|
| **modelcontextprotocol/servers** (~90k★) | Reference MCP servers | Adopt selectively |
| open-webui/mcpo | MCP↔OpenAPI proxy | Useful bridge |

### Explicit rejects / caution
- **open-webui** as product core — branding licence fails “own and rebrand” goal.
- **Mem0 Cloud / managed scores** — README admits platform scores ≠ OSS; avoid paid path.
- **“Free Claude Code” aggregator repos** — ToS/abuse risk; not a sustainable architecture.
- **Popularity-only picks** without licence/local-model check — discarded by policy.

---

## D. Dependencies between components

```
Hardware (RAM/VRAM) 
  → llama.cpp / Ollama (inference API :11434)
    → local embedding model (e.g. nomic/gte via Ollama)
      → Qdrant/Chroma (optional vector store)
        → Agent harness (nanobot OR OpenHands)
          → Tools: MCP servers, shell, git, browser-use/Playwright
          → Coding specialist: Aider (and/or OpenHands coding agent)
          → Scheduler: nanobot cron / OpenHands automation
```

**Hard dependency:** without a local (or self-hosted) OpenAI-compatible LLM endpoint, every “agent” project collapses to paid APIs.

**Soft dependency:** Docker strongly recommended for OpenHands sandbox and Mem0 self-host server — **missing on this box**.

---

## E. Proposed architecture (target system)

**Name working title:** `grok-system` (repo to create when you approve build phase)

```
┌─────────────────────────────────────────────────────────┐
│  Interfaces: WebUI (nanobot) / CLI (Aider) / API        │
├─────────────────────────────────────────────────────────┤
│  Orchestrator: HKUDS/nanobot (MIT)                      │
│   - planning, multi-agent, memory, cron, MCP gateway    │
├───────────────┬─────────────────────┬───────────────────┤
│ Coding lane   │ Research lane       │ Browser lane      │
│ Aider + git   │ web fetch/search    │ browser-use       │
│ OpenHands*    │ MCP github          │ Playwright        │
├───────────────┴─────────────────────┴───────────────────┤
│  Model gateway: Ollama (OpenAI-compatible)              │
│  Optional: Qdrant + local embeddings                    │
├─────────────────────────────────────────────────────────┤
│  Host: YOUR machine or cheap VPS (GPU optional)         │
│  NOT: Grok Bot box as permanent brain                   │
└─────────────────────────────────────────────────────────┘
* OpenHands when Docker sandbox is available
```

**Role of this Grok Bot going forward:** architect, researcher, GitHub operator, code generator that pushes into *your* repos — while the runtime lives on hardware you control.

---

## F. Exact installation order (proposed — **do not install yet**)

1. **Choose host** — laptop with Local Computer approval, or GPU/CPU VPS (≥16 GB RAM recommended for 7B–14B).
2. **Install Docker Engine** (if host supports) — unlocks sandboxes & compose stacks.
3. **Install Ollama** → pull one small chat model + one embedding model → verify `localhost:11434`.
4. **Install nanobot** → point provider at Ollama → verify WebUI chat with **zero** cloud keys.
5. **Add MCP servers** (filesystem, git, fetch) from `modelcontextprotocol/servers` as needed.
6. **Install Aider** in project repos → `--model` via Ollama OpenAI-compat endpoint.
7. **Optional:** Qdrant + wire memory; or rely on nanobot Dream first.
8. **Optional:** OpenHands Agent Canvas **after** Docker works.
9. **Optional:** browser-use in a dedicated venv with Playwright browsers.
10. **Create your system monorepo** on GitHub (`contactgleamsphere-afk/...`) with docker-compose, config templates, and docs — built by me in the next phase.
11. **Wire CI** with free GitHub Actions only if runners stay free-tier acceptable (see H).

---

## G. Which components can run completely free (software + no mandatory API)

- Ollama + open-weight models (weights free; hardware not)
- llama.cpp
- nanobot
- Aider (with local model)
- OpenHands self-host (MIT)
- browser-use + Playwright
- Qdrant / Chroma
- MCP reference servers
- GitHub free private repos (within GitHub’s free plan)

---

## H. Unavoidable compute / API / platform limits

| Limit | Nature |
|---|---|
| GPU/RAM for decent models | **Physics** — CPU 7B is slow; quality needs VRAM/RAM |
| This Grok Bot session | **Usage / plan limits** of the commercial host |
| GitHub API rate limits | Free-tier API quotas |
| GitHub Actions minutes | Free quota if you use Actions |
| Open WebUI branding licence | Legal limit if rebranding at scale |
| Mem0 OSS vs Platform | Managed features/scores not in OSS |
| No Docker on box | Blocks many “one-command” sandboxes **here** |
| Cursor Cloud Agent | Needs Cursor SCM + is not free/self-owned |

---

## I. Security risks

1. **PAT in chat history** — already present; rotate after bootstrap; prefer fine-grained least privilege.
2. **Agent with shell = RCE on host** — nanobot/OpenHands without sandbox can modify/delete anything the OS user can.
3. **Ollama unbound to LAN** — no auth by default; never expose `:11434` publicly.
4. **Downloading & executing arbitrary GitHub code** — supply-chain risk; pin commits/tags, review licences.
5. **browser-use** — can drive authenticated sessions; isolate profile/data.
6. **MCP servers** — third-party tools inherit agent trust; audit before enable.
7. **Passwordless sudo on box** — powerful; treat box as untrusted multi-tenant-ish environment.
8. **Probe repo left private on GitHub** — delete when audit accepted.

---

## J. Permissions / credentials actually required

| Item | Required for | Status now |
|---|---|---|
| GitHub PAT (repo + workflow as needed) | MCP GitHub write/read | **Present** (in connector); rotate recommended |
| `gh auth login` on box | Shell-side git/GitHub ops | **Missing** |
| Cursor SCM connect | CloudAgent on GitHub | **Missing** (optional; not needed for free path) |
| Local Computer “Always allow” | Probe/install on laptop | **Denied** this session |
| Ollama models on host | Local brain | **Not installed** |
| Optional: Brave/Serp API | Higher-quality web search | Avoid if possible; prefer self-hosted fetch |
| **No** OpenAI/Anthropic key | Goal state | Do **not** require for v1 |

---

## Immediate next build step (when you say go)

1. Confirm **host**: laptop vs VPS (and whether Docker install is allowed).
2. Create public/private monorepo `grok-system` with architecture docs + compose stubs.
3. Still **no** mass installs until host choice is explicit.

