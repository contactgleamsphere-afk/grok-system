$p='C:\AI\Factory\config.json'; Copy-Item $p "$p.bak-lanes" -Force
$c=Get-Content $p -Raw | ConvertFrom-Json
$c.providers.gemini.apiKey='${GEMINI_API_KEY}'
$c.providers.openrouter.apiKey='${OPENROUTER_API_KEY}'
function addp($n,$o){ if($c.modelPresets.PSObject.Properties[$n]){$c.modelPresets.$n=$o}else{$c.modelPresets | Add-Member -NotePropertyName $n -NotePropertyValue $o} }
addp 'gemini-flash'  ([pscustomobject]@{model='gemini-3.6-flash';provider='gemini';maxTokens=2048;contextWindowTokens=32768;temperature=0.2})
addp 'gemini-lite'   ([pscustomobject]@{model='gemini-3.5-flash-lite';provider='gemini';maxTokens=2048;contextWindowTokens=32768;temperature=0.2})
addp 'or-deepseek'   ([pscustomobject]@{model='deepseek/deepseek-v4-flash-0731:free';provider='openrouter';maxTokens=2048;contextWindowTokens=32768;temperature=0.2})
addp 'or-qwen27b'    ([pscustomobject]@{model='qwen/qwen3.8-27b:free';provider='openrouter';maxTokens=2048;contextWindowTokens=32768;temperature=0.2})
$c | ConvertTo-Json -Depth 20 | Set-Content $p -Encoding UTF8
# bot 002 chain
$b='C:\AI\Factory\run\botcfg\002.json'; $d=Get-Content $b -Raw | ConvertFrom-Json
$d.providers.gemini.apiKey='${GEMINI_API_KEY}'; $d.providers.openrouter.apiKey='${OPENROUTER_API_KEY}'
foreach($n in 'gemini-flash','gemini-lite','or-deepseek','or-qwen27b'){ $o=$c.modelPresets.$n; if($d.modelPresets.PSObject.Properties[$n]){$d.modelPresets.$n=$o}else{$d.modelPresets|Add-Member -NotePropertyName $n -NotePropertyValue $o} }
$d.agents.defaults.modelPreset='groq-gptoss20b'
$d.agents.defaults.fallbackModels=@('gemini-flash','or-deepseek','gemini-lite','local4b')
$d | ConvertTo-Json -Depth 20 | Set-Content $b -Encoding UTF8
"config ok: presets=" + ($c.modelPresets.PSObject.Properties.Name -join ',')
"002 chain: groq-gptoss20b -> " + ($d.agents.defaults.fallbackModels -join ' -> ')
$env:GROQ_API_KEY=[Environment]::GetEnvironmentVariable('GROQ_API_KEY','User'); $env:GEMINI_API_KEY=[Environment]::GetEnvironmentVariable('GEMINI_API_KEY','User'); $env:OPENROUTER_API_KEY=[Environment]::GetEnvironmentVariable('OPENROUTER_API_KEY','User')
cd C:\AI\Factory; .\.venv\Scripts\nanobot.exe status 2>&1 | Select-String -Pattern 'Model|Provider|provider|gemini|openrouter|groq|Fallback|Config' | Select -First 15
