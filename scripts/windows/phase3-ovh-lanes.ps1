$ErrorActionPreference='Stop'
$p='C:\AI\Factory\config.json'; Copy-Item $p "$p.bak-p3-$(Get-Date -Format HHmmss)"
$c=Get-Content $p -Raw|ConvertFrom-Json
# provider: OVH anonymous (no key). nanobot 'custom' provider = OpenAI-compatible with apiBase.
$c.providers.custom.apiBase='https://oai.endpoints.kepler.ai.cloud.ovh.net/v1'
$c.providers.custom.apiKey='anonymous'
$c.modelPresets | Add-Member -NotePropertyName 'ovh-gptoss20b' -NotePropertyValue ([pscustomobject]@{model='gpt-oss-20b';provider='custom';maxTokens=2048;contextWindowTokens=32768;temperature=0.2;reasoningEffort=$null}) -Force
$c.modelPresets | Add-Member -NotePropertyName 'ovh-mistral24b' -NotePropertyValue ([pscustomobject]@{model='Mistral-Small-3.2-24B-Instruct-2506';provider='custom';maxTokens=2048;contextWindowTokens=32768;temperature=0.2;reasoningEffort=$null}) -Force
$c.modelPresets | Add-Member -NotePropertyName 'ovh-llama70b' -NotePropertyValue ([pscustomobject]@{model='Meta-Llama-3_3-70B-Instruct';provider='custom';maxTokens=2048;contextWindowTokens=32768;temperature=0.2;reasoningEffort=$null}) -Force
$c.agents.defaults.modelPreset='ovh-gptoss20b'
$c.agents.defaults.fallbackModels=@('ovh-mistral24b','ovh-llama70b','local4b')
[IO.File]::WriteAllText($p,($c|ConvertTo-Json -Depth 20),(New-Object Text.UTF8Encoding($false)))
& C:\AI\Factory\.venv\Scripts\nanobot.exe status --config $p 2>&1 | Select-String 'Model:|Agent:|Custom:'
"== direct probe from laptop IP =="
$body='{"model":"gpt-oss-20b","messages":[{"role":"user","content":"Reply with exactly: LAPTOP_OK"}],"max_tokens":10}'
(Invoke-RestMethod -Uri 'https://oai.endpoints.kepler.ai.cloud.ovh.net/v1/chat/completions' -Method Post -ContentType 'application/json' -Body $body -TimeoutSec 60).choices[0].message.content
