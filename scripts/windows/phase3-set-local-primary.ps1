$p='C:\AI\Factory\config.json'; $c=Get-Content $p -Raw -Encoding UTF8|ConvertFrom-Json
Copy-Item $p "$p.bak-p7-$(Get-Date -Format yyyyMMddHHmmss)"
$c.agents.defaults.modelPreset='local4b'; $c.agents.defaults.fallbackModels=@('ovh-gptoss20b')
[IO.File]::WriteAllText($p,($c|ConvertTo-Json -Depth 20),(New-Object Text.UTF8Encoding($false)))
& C:\AI\Factory\.venv\Scripts\nanobot.exe status --config $p 2>&1 | Select-String 'Model:|Invalid|missing|Fallback'
"== core tests =="
Set-Location C:\AI\Factory; if(Test-Path core\tests){ & .venv\Scripts\python.exe -m pytest core\tests -q 2>&1 | Select -Last 8 } else { "no core\tests dir"; Get-ChildItem -Directory | % Name }
