# 1) factory wrapper into the master's workspace
Copy-Item C:\AI\Factory\repo\config\laptop\workspace\tools\factory.py C:\AI\Factory\workspace\tools\factory.py -Force
# 2) exec may pass the lane keys to children (secrets stay in env, never in files)
$p='C:\AI\Factory\config.json'; $c=Get-Content $p -Raw | ConvertFrom-Json
$c.tools.exec.allowedEnvKeys=@('GROQ_API_KEY','GEMINI_API_KEY','OPENROUTER_API_KEY','AIFACTORY_REPO','PYTHONIOENCODING','PATH','SYSTEMROOT','TEMP','TMP','USERPROFILE','APPDATA','LOCALAPPDATA')
$c.tools.exec.timeout=1800
[IO.File]::WriteAllText($p,($c|ConvertTo-Json -Depth 20),(New-Object Text.UTF8Encoding($false)))
# 3) AGENTS.md: how the master builds bots (general rule, no bot names)
$a=Get-Content C:\AI\Factory\workspace\AGENTS.md -Raw
if($a -notmatch 'Bot factory protocol'){
$a += @"

## Bot factory protocol (Phase 4)
When the owner asks you to create/build a bot from an objective, do NOT write the bot yourself. Run, via exec from the workspace root:
    python tools/factory.py create "<the owner's objective, verbatim>"
It returns JSON: bot_id, name, tools, files, tests, pass/total, status, verified. Report those fields exactly. If ok is false, report the error verbatim and stop.
To re-test a bot: python tools/factory.py test <bot_id>.  To list bots: python tools/factory.py list.
Never edit files under C:\AI\Factory\bots or C:\AI\Factory\repo by hand; the pipeline owns them.
"@
[IO.File]::WriteAllText('C:\AI\Factory\workspace\AGENTS.md',$a,(New-Object Text.UTF8Encoding($false)))
}
"master wired: allowedEnvKeys=$($c.tools.exec.allowedEnvKeys.Count) timeout=$($c.tools.exec.timeout)"
