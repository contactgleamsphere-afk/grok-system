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
# 3) AGENTS.md: canonical lean copy from the repo (D-045) — never appended to, always replaced
Copy-Item C:\AI\Factory\repo\config\laptop\workspace\AGENTS.md C:\AI\Factory\workspace\AGENTS.md -Force
# Strip mojibake from SOUL/USER (same encoding bug as botIcon)
foreach($f in 'SOUL.md','USER.md'){ $q="C:\AI\Factory\workspace\$f"; if(Test-Path $q){ $t=Get-Content $q -Raw -Encoding UTF8; $t2=($t -replace '[\u00C2\u00C3\u00E2][\u0080-\u00BF\u20AC\u2122\u201A\u2039\u0153\u017E\u02C6\u2013\u2014\u2018\u2019\u201C\u201D\u2022\u2026]+','-'); if($t2 -ne $t){ [IO.File]::WriteAllText($q,$t2,(New-Object Text.UTF8Encoding($false))) } } }
"master wired: allowedEnvKeys=$($c.tools.exec.allowedEnvKeys.Count) timeout=$($c.tools.exec.timeout) AGENTS=$((Get-Item C:\AI\Factory\workspace\AGENTS.md).Length)B"
