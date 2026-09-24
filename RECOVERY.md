# RECOVERY — rebuild from zero on a Windows machine
1. Install Python 3.11+, Git, Ollama. `ollama pull qwen2.5:3b-instruct-q4_K_M`.
2. `git clone https://github.com/contactgleamsphere-afk/grok-system C:\AI\Factory\repo`
3. Run `scripts\windows\install-phase1.ps1` (creates C:\AI\Factory venv, installs nanobot-ai==0.3.5, writes config).
   - Ensure config.json is UTF-8 **without BOM** and `contextWindowTokens` = 32768.
4. Copy `config\laptop\SOUL.md` and `AGENTS.md` into `C:\AI\Factory\workspace\`.
5. `nanobot status` → `nanobot agent -m "Reply with exactly: PHASE1_OK"` → `nanobot webui`.
6. Registries live in `registry\*.json`; regenerate markdown with `python -c "..."` (see core/factory/registry.py `to_markdown`).
7. Run `python -m pytest core\tests -q` to confirm the core package works on this Python.

## Re-apply nanobot patches after upgrade (2026-09-19)
```powershell
python C:\AI\Factory\tools\patch_groq_reasoning.py
python C:\AI\Factory\tools\patch_fallback_413.py
python C:\AI\Factory\tools\patch_disabled_tools.py
python C:\AI\Factory\tools\patch_quota_retry.py
python C:\AI\Factory\tools\patch_template_override.py
Get-ChildItem C:\AI\Factory\.venv\Lib\site-packages\nanobot -Recurse -Directory -Filter __pycache__ | Remove-Item -Recurse -Force
nanobot status --config C:\AI\Factory\config.json
```
Env vars that must exist for the user: GROQ_API_KEY, AIFACTORY_DISABLED_TOOLS (see TEST_RESULTS 2026-09-19).

## Lanes (2026-09-19)
Keys are User env vars on the laptop: GROQ_API_KEY, GEMINI_API_KEY, OPENROUTER_API_KEY. config.json references them as `${VAR}`; never paste keys into config. Re-add lanes after a config reset: the worker regenerates nanobot presets from `registry/models.json` after every probe/discover (`_sync_presets`, D-062); to force it, `python tools\factory_worker.py add probe`. Legacy one-shots live in `scripts/windows/archive/` (history only).

## Tunnel outage pattern (2026-09-19)
Loading qwen3:4b on the laptop can starve cloudflared → ssh drops mid-run and `run/tunnel.txt` is only refreshed when the supervisor restarts. If the tunnel is silent >10 min: on the laptop run `powershell -File C:\AI\Factory\tools\tunnel-restart.ps1` (or reboot cloudflared service). Never treat a dropped run as a test failure — re-run it.

Pre-warm the local model before any test that may fall back to it (prevents the cloudflared starvation above):
`Invoke-RestMethod -Method Post http://127.0.0.1:11434/api/generate -Body (@{model='qwen3:4b';prompt='hi';stream=$false;keep_alive='30m';options=@{num_predict=4}}|ConvertTo-Json) -ContentType 'application/json'`

## Laptop repo mirror
`C:\AI\Factory\repo` = clone of GitHub main. `C:\AI\Factory\tools\repo-sync.ps1` is a shim that runs `repo\scripts\windows\repo-sync.ps1` (D-101: lock + never reset --hard). The pipeline reads/writes `repo\registry` and `repo\specs`; after a laptop run copy `registry\bots.json` + new `specs\*.json` + `bots\<id>` back into the main repo and commit.

## Factory worker service (2026-09-21)
- Start/restart ONLY via `schtasks /Run /TN "AIFactory Worker"` (detached). Processes launched with `Start-Process` from an SSH/PowerShell session die when that session ends — this looked like "worker vanished" three times today.
- Find processes with `Get-CimInstance Win32_Process | ? { $_.CommandLine -match 'factory_worker' }` (Get-Process has no CommandLine in PS 5).
- Kill + relaunch: stop those PIDs, `Remove-Item C:\AI\Factory\run\worker.lock`, then `schtasks /Run`.
- Orphaned running jobs recover by lease expiry (40 min) or `factory_worker.py release <id8> --uncount`.
- Logs: `C:\AI\Factory\run\logs\worker-<date>-<pid>.log`; audit: `factory_worker.py audit`.

## Tunnel hostname rotated (seen 2026-09-22 03:26)
Symptom from the builder side: `dial tcp: lookup <old>.trycloudflare.com: no such host` then `websocket: bad handshake` for ~2-3 min.
Cause: cloudflared quick tunnels rotate on reconnect. The tunnel supervisor republishes `run/tunnel.txt` to GitHub; `~/bin/laptop` reads it before every connect.
Action: none — retry after 60 s. If it persists >10 min, the laptop is asleep/offline (task AIFactory-Tunnel runs as SYSTEM at boot). `C:\AI\Factory\tools\tunnel-supervisor.ps1` is a shim to `repo\scripts\windows\tunnel-supervisor.ps1` (D-116b: HTTPS reachability test, 300 s cap). Backstop: the hourly `tick` restarts the task if the URL answers 530 and no supervisor is alive (D-116, audit `tunnel.restarted`). Restarting the task by hand: `schtasks /End /TN AIFactory-Tunnel; schtasks /Run /TN AIFactory-Tunnel` (run `/Run` directly, not via Start-Process).

## Nightly monitor did not run
Check `Get-ScheduledTaskInfo 'AIFactory Monitor'` (LastRunTime) and `factory_worker.py jobs | Select-String monitor`.
Since D-055 the daily `report` job enqueues a monitor for the day if none exists, so a skipped task self-heals within 24 h; to force: `factory_worker.py add monitor`.

## Laptop lost / fresh machine
Registry (`registry/`), specs, audit (`audit/*.jsonl`), proposals, MONITOR/BOT_REGISTRY/STATUS are all in git. Jobs DB and bot bundles are not: rebuild bundles from specs with `factory_cli build`, re-run `add monitor` to re-verify. Audit continuity: the JSONL high-water mark means a fresh DB starts a new seq range — keep the old files, do not delete.

## Laptop offline mid-drill (2026-09-23 00:05)
Symptom: `ssh` → `Connection closed by UNKNOWN port 65535`, tunnel URL returns HTTP 530, no worker state commits, `run/tunnel.txt` not refreshed for >45 min. Meaning: the laptop itself is asleep/offline (tunnel supervisor would have republished within ~2 min otherwise). Nothing to fix remotely; when it wakes: worker task restarts at logon/15-min tick, repo-sync pulls, self-test gate runs, queued jobs resume from leases (D-081). Pending at outage: D-099 live repair drill on bot 009 (`tools/_archive/q15.py` then `add repair 009`).

## Laptop offline alert (D-119)
GitHub issue labelled `laptop-offline` = no laptop commit for >2 h (watchdog workflow, every 30 min). Action: physical —
wake the laptop / reconnect Wi-Fi. Nothing to run: supervisor republishes the tunnel, the worker resumes queued jobs, and
the issue closes itself on the next heartbeat. Manual drill: Actions → laptop-watchdog → Run workflow, threshold_min=1.
