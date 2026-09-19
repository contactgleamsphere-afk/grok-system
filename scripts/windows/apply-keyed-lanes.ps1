# Run on the laptop AFTER setting user env vars (setx GROQ_API_KEY ... etc). Merges staged keyed lanes into live config and validates.
$p='C:\AI\Factory\config.json'; Copy-Item $p "$p.bak-keyed-$(Get-Date -Format HHmmss)"
$c=Get-Content $p -Raw|ConvertFrom-Json; $c.modelPresets.PSObject.Properties.Remove('groq-llama70b'); $s=Get-Content C:\AI\Factory\config.keyed-lanes.staged.json -Raw|ConvertFrom-Json
$have=@(); foreach($k in 'GROQ_API_KEY','OPENROUTER_API_KEY','GEMINI_API_KEY'){ if([Environment]::GetEnvironmentVariable($k,'User') -or [Environment]::GetEnvironmentVariable($k,'Machine')){ $have+=$k } }
"keys present: $($have -join ', ')"; if(-not $have){ "no keys set - nothing applied"; exit 1 }
$map=@{GROQ_API_KEY='groq';OPENROUTER_API_KEY='openrouter';GEMINI_API_KEY='gemini'}
foreach($k in $have){ $prov=$map[$k]; $c.providers.$prov.apiKey=$s.providers.$prov.apiKey
  foreach($pp in $s.modelPresets.PSObject.Properties){ if($pp.Value.provider -eq $prov){ $c.modelPresets | Add-Member -NotePropertyName $pp.Name -NotePropertyValue $pp.Value -Force } } }
$chain=@(); foreach($x in @('groq-gptoss120b','groq-qwen27b','groq-gptoss20b','or-free-auto','gemini-flash','ovh-gptoss20b','ovh-mistral24b','local4b')){ if($c.modelPresets.PSObject.Properties[$x]){ $chain+=$x } }
$c.agents.defaults.modelPreset=$chain[0]; $c.agents.defaults.fallbackModels=$chain[1..($chain.Count-1)]
[IO.File]::WriteAllText($p,($c|ConvertTo-Json -Depth 20),(New-Object Text.UTF8Encoding($false)))
"primary=$($chain[0]) chain=$($chain[1..($chain.Count-1)] -join ',')"
& C:\AI\Factory\.venv\Scripts\nanobot.exe status --config $p 2>&1 | Select-String 'Model:|Agent:|Invalid|missing'
