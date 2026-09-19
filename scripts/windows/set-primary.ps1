param([string]$primary,[string]$chain)
$chainArr=@($chain -split "[,;]" | ForEach-Object { $_.Trim() } | Where-Object { $_ })
$p='C:\AI\Factory\config.json'; $c=Get-Content $p -Raw -Encoding UTF8|ConvertFrom-Json
$c.agents.defaults.modelPreset=$primary; $c.agents.defaults.fallbackModels=$chainArr
[IO.File]::WriteAllText($p,($c|ConvertTo-Json -Depth 20),(New-Object Text.UTF8Encoding($false)))
& C:\AI\Factory\.venv\Scripts\nanobot.exe status --config $p 2>&1 | Select-String 'Model:|Invalid|missing'
