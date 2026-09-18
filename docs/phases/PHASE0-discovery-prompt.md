GROK EXECUTION PROMPT — PHASE 0: DISCOVERY, BASELINE & BUILD-STATE SCAFFOLD

A. MISSION
Establish a measured baseline of LAPTOP-LRE6PSA8, test whether the current local model can actually perform tool calls, pull ONE candidate model for comparison, and create the private GitHub repository `ai-factory` containing the persistent build-state documentation. Do not change the running nanobot configuration.

B. CURRENT STATE (known)
- nanobot-ai 0.3.5 in C:\AI\Factory\.venv ; config C:\AI\Factory\config.json ; workspace C:\AI\Factory\workspace ; WebUI 127.0.0.1:8765
- Ollama 0.34.1 on 127.0.0.1:11434 ; model qwen2.5:3b-instruct-q4_K_M
- Windows 11 Home, 4c/8t, ~14 GB RAM, iGPU, no Docker/WSL, Python 3.11.9, Node 24, Git 2.55
- GitHub account contactgleamsphere-afk via GitHub MCP

C. PRECONDITIONS (verify, report actual values, do not proceed if any fails)
1. `C:\AI\Factory\.venv\Scripts\nanobot.exe --version` prints 0.3.5
2. `ollama list` shows qwen2.5:3b-instruct-q4_K_M
3. `Invoke-RestMethod http://127.0.0.1:11434/api/tags` succeeds
4. GitHub MCP `get_me` returns contactgleamsphere-afk
5. Free disk on C: > 20 GB

D. EXACT ACTIONS

D1. RAM/CPU baseline (no changes)
- Run: `Get-CimInstance Win32_OperatingSystem | Select TotalVisibleMemorySize,FreePhysicalMemory`
- Run: `Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 15 Name,Id,@{n='MB';e={[math]::Round($_.WorkingSet64/1MB)}}`
- Run: `ollama ps`
- Record all output verbatim.

D2. Inference baseline, current model
- Run: `ollama run qwen2.5:3b-instruct-q4_K_M "Write exactly 150 words about the history of Birmingham, England." --verbose`
- Record: prompt eval rate, eval rate (tokens/s), total duration. Record FreePhysicalMemory before and after.

D3. Tool-calling capability test, current model (this is the critical measurement)
Use nanobot one-shot mode against the CURRENT config (do not edit config). Run each of these 5 prompts once, record whether the model actually invoked the tool and whether the result was correct:
  T1: `nanobot agent -m "Create a file named phase0_test.txt in the workspace containing the single line HELLO_FACTORY, then read it back and tell me its contents."`
  T2: `nanobot agent -m "List the files in the workspace root directory and count them."`
  T3: `nanobot agent -m "Use web search to find the current stable version number of the Python package nanobot-ai on PyPI and report only the version."`
  T4: `nanobot agent -m "Run the shell command: python --version  and tell me the exact output."`
  T5: `nanobot agent -m "Read phase0_test.txt, append a second line GOODBYE, save it, then tell me how many lines it now has."`
Score each: TOOL_CALLED yes/no ; RESULT_CORRECT yes/no ; time taken. Paste the agent's actual replies. Then delete phase0_test.txt.

D4. Pull ONE comparison model
- Run: `ollama pull qwen3:4b`
- If that tag does not exist, run `ollama pull qwen3:4b-instruct` ; if neither exists, STOP and report the exact error plus output of a web search for the current Ollama Qwen3 4B tag. Do not pull anything else.
- Repeat D2 against the new model (same prompt, --verbose) and record the same numbers.
- Do NOT put this model in nanobot config. Do NOT pull any other model.

D5. Create GitHub repository and build-state scaffold
Via GitHub MCP create PRIVATE repo `contactgleamsphere-afk/ai-factory` (description: "Personal AI Factory — core, registries, build state"). Add these files with real content filled from what you measured in D1–D4 (no placeholders where you have data; write "UNVERIFIED" where you do not):
  README.md            — one paragraph: what this repo is, the CORE / WORKERS / MODELS / TOOLS / INFRASTRUCTURE split
  BUILD_STATE.md       — phase table (0–12), status of each, verified facts list, date
  ARCHITECTURE.md      — the 5-layer split, current runtime = nanobot 0.3.5 (provisional), planned exits
  CHANGELOG.md         — entries for Phase 1 (done) and Phase 0 (this run)
  DECISIONS.md         — D-001 nanobot as provisional core (reasons: Windows, no Docker, native fallback/subagents/cron/MCP/multi-instance, MIT) ; D-002 repo is source of truth ; D-003 model chosen by benchmark not assumption
  SECURITY.md          — current posture: localhost-only Ollama/WebUI, restrictToWorkspace planned, NO OS sandbox on Windows (nanobot limitation), no secrets in repo, PAT rotation pending
  COMPONENT_REGISTRY.md — nanobot, Ollama, Python venv, Node, Git with versions/paths
  MODEL_REGISTRY.md    — table: model | size | tok/s | RAM delta | tool-call score (from D3, "not tested" for qwen3) | status
  TOOL_REGISTRY.md     — nanobot built-in tools currently registered (list them from `nanobot status` or WebUI)
  BOT_REGISTRY.md      — "001 MASTER — not yet configured" only
  TEST_RESULTS.md      — D2/D3/D4 raw results
  RECOVERY.md          — exact steps to rebuild Phase 1 from scratch on a new Windows machine
  .gitignore           — *.log, .venv/, sessions/, *.env
Also copy the CURRENT C:\AI\Factory\config.json into the repo as `config/config.phase1.json` (it contains no secrets — verify that before committing).
Commit message: "phase0: baseline, tool-call test, build-state scaffold".

E. DECISION RULES
- If a command's output differs from the expectation stated here, record the difference and continue unless it is a precondition.
- If the 3B model fails ≥3 of the 5 tool tests, mark MODEL_REGISTRY status "UNSUITABLE AS MASTER" — do not attempt to fix it in this phase.
- If free RAM drops below 1 GB during D4, stop the model run, record it, continue to D5.
- If GitHub repo creation fails, complete D1–D4, write the files to C:\AI\Factory\repo-staging\ locally, and report BLOCKED for D5 only.

F. VALIDATION
- `ollama list` shows exactly two models (3B and the one qwen3 tag)
- C:\AI\Factory\config.json is byte-identical to before (report its SHA256 before and after: `Get-FileHash`)
- `nanobot agent -m "Reply with exactly: STILL_OK"` still works after everything
- GitHub repo exists, private, 14 files, one commit
- phase0_test.txt no longer exists in the workspace

G. SECURITY CONSTRAINTS
- Do not edit config.json, SOUL.md, AGENTS.md, firewall, or anything outside C:\AI\Factory.
- Do not add API keys anywhere. Do not commit any token, PAT, or .env.
- Keep Ollama and WebUI on 127.0.0.1. Confirm with `netstat -ano | findstr "11434 8765"`.
- Do not install Python or npm packages. Do not install MCP servers.

H. STOP CONDITIONS
Stop immediately and report if: a precondition fails; config.json hash changes; any command asks for credentials; disk free < 10 GB; you are about to run anything not listed above.

I. ROLLBACK
- `ollama rm <qwen3 tag>` removes the comparison model.
- Delete repo via GitHub web UI (no MCP delete tool) — or leave it; it holds only docs.
- Delete C:\AI\Factory\workspace\phase0_test.txt if still present.

J. COMPLETION REPORT — return exactly this structure
PHASE: 0
STATUS: SUCCESS / PARTIAL / FAILED / BLOCKED
ENVIRONMENT VERIFIED: (C1–C5 actual values)
ACTIONS EXECUTED:
FILES CREATED:
FILES MODIFIED: (must be none outside the repo/staging)
PACKAGES INSTALLED: (must be none)
SERVICES STARTED:
PORTS: (netstat output)
COMMANDS RUN:
TESTS: (D3 table: test | tool called | correct | seconds | reply excerpt)
TEST RESULTS: (D2/D4 table: model | prompt tok/s | eval tok/s | total s | RAM before | RAM after)
TOP RAM CONSUMERS: (D1 top-15)
GITHUB CHANGES: (repo URL, commit SHA, file list)
ERRORS:
WARNINGS:
SECURITY CONCERNS:
ROLLBACK:
NEXT RECOMMENDED ACTION:
UNVERIFIED CLAIMS:
CONFIG SHA256 BEFORE / AFTER:

Then STOP. Do not begin Phase 2.
