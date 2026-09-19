$env:GROQ_API_KEY=[Environment]::GetEnvironmentVariable('GROQ_API_KEY','User')
$p='C:\AI\Factory\config.json'; $c=Get-Content $p -Raw -Encoding UTF8|ConvertFrom-Json
# Scenario A: Groq lane with a WRONG key -> must fail over to local4b
$c.providers.groq.apiKey='gsk_invalid_key_for_failover_test_000000000000000000000'
$c.agents.defaults.modelPreset='groq-qwen27b'; $c.agents.defaults.fallbackModels=@('local4b')
[IO.File]::WriteAllText($p,($c|ConvertTo-Json -Depth 20),(New-Object Text.UTF8Encoding($false)))
"== A: bad Groq key -> local4b"; $t=Get-Date
$out = & C:\AI\Factory\.venv\Scripts\nanobot.exe agent -m 'Reply with exactly: FAILOVER_OK' -s "foA-$(Get-Date -Format HHmmss)" --classic --no-markdown --logs --config $p --workspace C:\AI\Factory\workspace 2>&1 | Out-String
"elapsed $([int]((Get-Date)-$t).TotalSeconds)s"
($out -split "`n") | Where-Object { $_ -match 'failed|succeeded|Response to|FAILOVER_OK$' } | Select -First 8
# Scenario B: Groq unreachable (bad apiBase) -> local4b
$c.providers.groq.apiKey='${GROQ_API_KEY}'; $c.providers.groq | Add-Member -NotePropertyName apiBase -NotePropertyValue 'http://127.0.0.1:9/v1' -Force
[IO.File]::WriteAllText($p,($c|ConvertTo-Json -Depth 20),(New-Object Text.UTF8Encoding($false)))
"== B: Groq unreachable -> local4b"; $t=Get-Date
$out = & C:\AI\Factory\.venv\Scripts\nanobot.exe agent -m 'Reply with exactly: FAILOVER_OK' -s "foB-$(Get-Date -Format HHmmss)" --classic --no-markdown --logs --config $p --workspace C:\AI\Factory\workspace 2>&1 | Out-String
"elapsed $([int]((Get-Date)-$t).TotalSeconds)s"
($out -split "`n") | Where-Object { $_ -match 'failed|succeeded|Response to|FAILOVER_OK$' } | Select -First 8
# restore production chain
$c.providers.groq.PSObject.Properties.Remove('apiBase')
$c.agents.defaults.modelPreset='groq-qwen27b'; $c.agents.defaults.fallbackModels=@('groq-gptoss120b','groq-gptoss20b','local4b')
[IO.File]::WriteAllText($p,($c|ConvertTo-Json -Depth 20),(New-Object Text.UTF8Encoding($false)))
"== restored"; & C:\AI\Factory\.venv\Scripts\nanobot.exe status --config $p 2>&1 | Select-String 'Model:|Invalid'
$t=Get-Date; $out = & C:\AI\Factory\.venv\Scripts\nanobot.exe agent -m 'Reply with exactly: GROQ_OK' -s "foC-$(Get-Date -Format HHmmss)" --classic --no-markdown --config $p --workspace C:\AI\Factory\workspace 2>&1 | Out-String
"sanity elapsed $([int]((Get-Date)-$t).TotalSeconds)s: " + (($out.Trim() -split "`n") | Select -Last 1)
