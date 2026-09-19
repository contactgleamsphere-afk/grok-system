$ErrorActionPreference='Continue'
$p='C:\AI\Factory\config.json'; $c=Get-Content $p -Raw|ConvertFrom-Json
foreach($k in 'groq','openrouter','gemini'){ $c.providers.$k.apiKey=$null }
foreach($k in 'groq-llama70b','groq-gptoss120b','or-free-auto','gemini-flash'){ $c.modelPresets.PSObject.Properties.Remove($k) }
# staged keyed lanes (applied by apply-keyed-lanes.ps1 when env vars exist)
@'
{ "providers": { "groq": {"apiKey":"${GROQ_API_KEY}"}, "openrouter": {"apiKey":"${OPENROUTER_API_KEY}"}, "gemini": {"apiKey":"${GEMINI_API_KEY}"} },
  "modelPresets": {
    "groq-llama70b":  {"model":"llama-3.3-70b-versatile","provider":"groq","maxTokens":2048,"contextWindowTokens":32768,"temperature":0.2},
    "groq-gptoss120b":{"model":"openai/gpt-oss-120b","provider":"groq","maxTokens":2048,"contextWindowTokens":32768,"temperature":0.2},
    "or-free-auto":   {"model":"openrouter/free","provider":"openrouter","maxTokens":2048,"contextWindowTokens":32768,"temperature":0.2},
    "gemini-flash":   {"model":"gemini-2.5-flash","provider":"gemini","maxTokens":2048,"contextWindowTokens":32768,"temperature":0.2} } }
'@ | Set-Content C:\AI\Factory\config.keyed-lanes.staged.json -Encoding ascii
# FAILOVER TEST
$c.agents.defaults.modelPreset='broken-primary'; $c.agents.defaults.fallbackModels=@('ovh-gptoss20b','local4b')
[IO.File]::WriteAllText($p,($c|ConvertTo-Json -Depth 20),(New-Object Text.UTF8Encoding($false)))
& C:\AI\Factory\.venv\Scripts\nanobot.exe status --config $p 2>&1 | Select-String 'Model:|Invalid|missing'
"== failover test =="; $t=Get-Date
$out = & C:\AI\Factory\.venv\Scripts\nanobot.exe agent -m "Reply with exactly: FAILOVER_OK" --config $p --workspace C:\AI\Factory\workspace 2>&1 | Out-String
"elapsed: $([int]((Get-Date)-$t).TotalSeconds)s"; $out.Trim()
@'
import sqlite3;c=sqlite3.connect(r"C:\AI\Factory\llm_usage.sqlite3")
for r in c.execute("select id,provider,model,finish_reason,duration_ms,error from llm_calls where source!='dream' order by id desc limit 6"): print(r)
'@ | Set-Content C:\AI\Factory\tools\lastcalls.py; python C:\AI\Factory\tools\lastcalls.py
# production chain (no-key lanes only, for now)
$c.agents.defaults.modelPreset='ovh-gptoss20b'; $c.agents.defaults.fallbackModels=@('ovh-mistral24b','ovh-llama70b','local4b')
[IO.File]::WriteAllText($p,($c|ConvertTo-Json -Depth 20),(New-Object Text.UTF8Encoding($false)))
"restored: primary=ovh-gptoss20b chain=ovh-mistral24b,ovh-llama70b,local4b"
