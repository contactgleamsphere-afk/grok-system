# 1) factory wrapper into the master's workspace
New-Item -ItemType Directory -Force C:\AI\Factory\workspace\tools | Out-Null
Copy-Item C:\AI\Factory\repo\config\laptop\workspace\tools\factory.py C:\AI\Factory\workspace\tools\factory.py -Force
# 2) exec may pass the lane keys to children (secrets stay in env, never in files)
$p='C:\AI\Factory\config.json'; $c=Get-Content $p -Raw -Encoding UTF8 | ConvertFrom-Json
# D-035: botIcon must stay a single glyph; a previous encoding bug doubled it each run until it ate the model context budget
if($c.agents.defaults.botIcon.Length -gt 8){ $c.agents.defaults.botIcon='*' }
$c.tools.exec.allowedEnvKeys=@('GROQ_API_KEY','GEMINI_API_KEY','OPENROUTER_API_KEY','AIFACTORY_REPO','PYTHONIOENCODING','PATH','SYSTEMROOT','TEMP','TMP','USERPROFILE','APPDATA','LOCALAPPDATA')
$c.tools.exec.timeout=1800
[IO.File]::WriteAllText($p,($c|ConvertTo-Json -Depth 20),(New-Object Text.UTF8Encoding($false)))
# 3) AGENTS.md: how the master builds bots (general rule, no bot names)
$a=Get-Content C:\AI\Factory\workspace\AGENTS.md -Raw
if($a -notmatch 'factory.py report'){ $a = ($a -split '## Bot factory protocol')[0]
$a += @"

## Bot factory protocol (Phase 4)
When the owner asks you to create/build a bot from an objective, do NOT write the bot yourself. Run, via exec from the workspace root:
    python tools/factory.py create "<the owner's objective, verbatim>"
It returns JSON: bot_id, name, tools, files, tests, pass/total, status, verified. Report those fields exactly. If ok is false, report the error verbatim and stop.
To re-test a bot: python tools/factory.py test <bot_id>.  To list bots: python tools/factory.py list.
For several bots, or when the owner says "queue"/"in the background": python tools/factory.py queue create "<objective>" (one call per objective), then python tools/factory.py jobs to report job ids/states. A background worker processes the queue; python tools/factory.py audit <bot_id> shows the lifecycle. When the owner asks how the factory is doing / what needs attention: python tools/factory.py report.
Never edit files under C:\AI\Factory\bots or C:\AI\Factory\repo by hand; the pipeline owns them.
"@
[IO.File]::WriteAllText('C:\AI\Factory\workspace\AGENTS.md',$a,(New-Object Text.UTF8Encoding($false)))
}
"master wired: allowedEnvKeys=$($c.tools.exec.allowedEnvKeys.Count) timeout=$($c.tools.exec.timeout)"
