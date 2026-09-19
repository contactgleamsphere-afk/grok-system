foreach($k in 'GROQ_API_KEY','GEMINI_API_KEY','OPENROUTER_API_KEY'){ Set-Item env:$k ([Environment]::GetEnvironmentVariable($k,'User')) }
$src='C:\AI\Factory\config.json'; $p='C:\AI\Factory\run\failover-xp.json'
function run($label,$mut){
  $c=Get-Content $src -Raw | ConvertFrom-Json
  $c.agents.defaults.modelPreset='groq-gptoss20b'; $c.agents.defaults.fallbackModels=@('gemini-lite','or-deepseek','local4b')
  & $mut $c
  [IO.File]::WriteAllText($p,($c|ConvertTo-Json -Depth 20),(New-Object Text.UTF8Encoding($false)))
  "== $label"; $t=Get-Date
  $out = & C:\AI\Factory\.venv\Scripts\nanobot.exe agent -m 'Reply with exactly: XP_OK' -s "xp-$(Get-Date -Format HHmmss)" --classic --no-markdown --logs --config $p --workspace C:\AI\Factory\workspace 2>&1 | Out-String
  "elapsed $([int]((Get-Date)-$t).TotalSeconds)s"
  ($out -split "`n") | ? { $_ -match 'failed|succeeded|rotating|Response to' } | % { ($_ -replace 'gsk_\w+','gsk_***' -replace 'AIza[\w-]+','AIza***' -replace 'sk-or-v1-\w+','sk-or-***').Substring(0,[Math]::Min(170,$_.Length)) } | Select -First 8
}
run 'C: Groq bad key + Gemini unreachable -> OpenRouter' { param($c) $c.providers.groq.apiKey='gsk_invalid_0000000000000000000000000000000000000000'; $c.providers.gemini | Add-Member -NotePropertyName apiBase -NotePropertyValue 'http://127.0.0.1:9/v1' -Force }
run 'D: Groq+Gemini+OpenRouter all unreachable -> local4b' { param($c) $c.providers.groq.apiKey='gsk_invalid_0000000000000000000000000000000000000000'; foreach($n in 'gemini','openrouter'){ $c.providers.$n | Add-Member -NotePropertyName apiBase -NotePropertyValue 'http://127.0.0.1:9/v1' -Force } }
Remove-Item $p -Force
