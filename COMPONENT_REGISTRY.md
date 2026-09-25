# COMPONENT_REGISTRY
| Component | Version | Location | Role | Verified |
|---|---|---|---|---|
| nanobot-ai | 0.3.5 | C:\AI\Factory\.venv | agent runtime (provisional core) | VERIFIED |
| Ollama | 0.34.1 | 127.0.0.1:11434 | local inference | VERIFIED |
| Python | 3.11.9 (laptop) / 3.13 (sandbox) | — | runtime | VERIFIED |
| Node/npm | 24.19 / 11.17 | laptop | future MCP servers | VERIFIED |
| Git | 2.55 | laptop | source control | VERIFIED |
| core/factory | 0.1.0 | this repo | registries, router, botspec | VERIFIED (sandbox tests) |
| Docker / WSL | — | not installed | future sandboxing | BLOCKED |

| factory_bench | tools/factory_bench.py | lane quality benchmark (D-050): pinned single-lane run of the reference suite → limits.bench; `--rank` | VERIFIED 2026-09-22 |
| tools/factory_scout.py | INFRASTRUCTURE | free-resource inventory (registry/infra.json, docs/INFRA.md); weekly `scout` job | VERIFIED live 2026-09-25 (D-118) |
| tools/factory_selfpatch.py | FACTORY | proposal → envelope-checked code edit → worktree tests → branch + PR; never writes main | VERIFIED unit+real git 2026-09-25 (D-122); live pending |
| .github/workflows/ci.yml, watchdog.yml | INFRASTRUCTURE | off-laptop unit suite on push/PR; laptop-offline issue every 30 min | VERIFIED live 2026-09-24 (D-119) |
| factory_pipeline.cmd_canary / job `canary` | FACTORY | nightly architect→bundle→tests self-test with no registry footprint | VERIFIED live 2026-09-24 (D-117) |
