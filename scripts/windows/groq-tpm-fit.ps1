$p='C:\AI\Factory\config.json'; $c=Get-Content $p -Raw -Encoding UTF8|ConvertFrom-Json
foreach($k in 'groq-gptoss120b','groq-qwen27b','groq-gptoss20b'){ $c.modelPresets.$k.contextWindowTokens=8200; $c.modelPresets.$k.maxTokens=768 }
$c.agents.defaults.maxToolResultChars=2500
[IO.File]::WriteAllText($p,($c|ConvertTo-Json -Depth 20),(New-Object Text.UTF8Encoding($false)))
& C:\AI\Factory\.venv\Scripts\nanobot.exe status --config $p 2>&1 | Select-String 'Model:|Invalid'
