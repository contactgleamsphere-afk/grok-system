# Runs ONE real task on a factory bot (D-063): same isolation as the acceptance runner (per-bot config, disabled
# tools, template dir, live chain), but with owner-supplied input files and the produced files captured.
# Usage: run-bot-task.ps1 -BotDir C:\AI\Factory\bots\013-log-error-filter -Task "..." -InDir C:\...\in -OutDir C:\...\out [-Cap 300]
param([Parameter(Mandatory=$true)][string]$BotDir,[Parameter(Mandatory=$true)][string]$Task,[string]$InDir='',[Parameter(Mandatory=$true)][string]$OutDir,[int]$Cap=300)
$ErrorActionPreference='Continue'
$env:GROQ_API_KEY=[Environment]::GetEnvironmentVariable('GROQ_API_KEY','User')
$env:GEMINI_API_KEY=[Environment]::GetEnvironmentVariable('GEMINI_API_KEY','User')
$env:OPENROUTER_API_KEY=[Environment]::GetEnvironmentVariable('OPENROUTER_API_KEY','User')
$bot=Get-Content "$BotDir\bot.json" -Raw -Encoding UTF8|ConvertFrom-Json
$patch=Get-Content "$BotDir\nanobot.patch.json" -Raw -Encoding UTF8|ConvertFrom-Json
$cfg=Get-Content C:\AI\Factory\config.json -Raw -Encoding UTF8|ConvertFrom-Json
$env:AIFACTORY_REPO='C:\AI\Factory\repo'
$live = python C:\AI\Factory\repo\tools\factory_chain.py $BotDir | ConvertFrom-Json
if($live -and $live.primary){ $cfg.agents.defaults.modelPreset=$live.primary; $cfg.agents.defaults.fallbackModels=@($live.fallbacks) }
else { $cfg.agents.defaults.modelPreset=$patch.agents.defaults.modelPreset; $cfg.agents.defaults.fallbackModels=@($patch.agents.defaults.fallbackModels) }
$cfg.agents.defaults.maxToolResultChars=1500
New-Item -ItemType Directory -Force C:\AI\Factory\run\botcfg | Out-Null; $botCfg="C:\AI\Factory\run\botcfg\$($bot.id)-task.json"
[IO.File]::WriteAllText($botCfg,($cfg|ConvertTo-Json -Depth 20),(New-Object Text.UTF8Encoding($false)))
$env:AIFACTORY_DISABLED_TOOLS=$patch.env.AIFACTORY_DISABLED_TOOLS
$env:AIFACTORY_TEMPLATE_DIR="$BotDir\templates"
$bundle='^(AGENTS|SOUL|TESTS|RECOVERY|TEST_RESULTS|HEARTBEAT|USER)\.md$|^bot\.json$|^nanobot\.patch\.json$|^\.gitignore$'
# clean workspace of leftovers, then stage inputs
Get-ChildItem $BotDir -File | ? { $_.Name -notmatch $bundle } | Remove-Item -Force
$staged=@()
if($InDir -and (Test-Path $InDir)){ Get-ChildItem $InDir -File | % { Copy-Item $_.FullName $BotDir -Force; $staged+=$_.Name } }
$sid="bot$($bot.id)-task-$(Get-Date -Format HHmmss)"; $t0=Get-Date
$job=Start-Job -ScriptBlock { param($nb,$m,$s,$c,$w,$k,$d,$td,$gk,$ok) $env:GROQ_API_KEY=$k; $env:GEMINI_API_KEY=$gk; $env:OPENROUTER_API_KEY=$ok; $env:AIFACTORY_DISABLED_TOOLS=$d; $env:AIFACTORY_TEMPLATE_DIR=$td; & $nb agent -m ($m -replace '"','\"') -s $s --classic --no-markdown --config $c --workspace $w 2>&1 | Out-String } -ArgumentList 'C:\AI\Factory\.venv\Scripts\nanobot.exe',$Task,$sid,$botCfg,$BotDir,$env:GROQ_API_KEY,$env:AIFACTORY_DISABLED_TOOLS,$env:AIFACTORY_TEMPLATE_DIR,$env:GEMINI_API_KEY,$env:OPENROUTER_API_KEY
if(Wait-Job $job -Timeout $Cap){ $out=(Receive-Job $job|Out-String); $status='done' } else { Stop-Job $job; $out=(Receive-Job $job|Out-String); $status='TIMEOUT'; Get-Process nanobot -ErrorAction SilentlyContinue|Stop-Process -Force }
Remove-Job $job -Force
New-Item -ItemType Directory -Force "C:\AI\Factory\run\logs" | Out-Null; Set-Content "C:\AI\Factory\run\logs\$sid.log" $out
# capture everything the bot produced (new or changed files), move it out, leave the bundle clean
New-Item -ItemType Directory -Force $OutDir | Out-Null
$produced=@()
Get-ChildItem $BotDir -File | ? { $_.Name -notmatch $bundle } | % {
  $isInput = $staged -contains $_.Name
  $changed = $true
  if($isInput){ $orig = Join-Path $InDir $_.Name; if((Get-FileHash $orig).Hash -eq (Get-FileHash $_.FullName).Hash){ $changed=$false } }
  if($changed){ Copy-Item $_.FullName $OutDir -Force; $produced+=$_.Name }
  Remove-Item $_.FullName -Force
}
$lines=@(($out.Trim() -split "`n") | Where-Object { $_ -notmatch '^\s*✻' -and $_.Trim() } | % { $_.TrimEnd("`r") })
$ri=-1; for($li=0; $li -lt $lines.Count; $li++){ if($lines[$li] -match '^\s*(RESULT|ANSWER|OUTPUT)\s*[:=]'){ $ri=$li } }
if($ri -ge 0){ $last=(($lines[$ri..($lines.Count-1)] | Select -First 4) -join ' ') } else { $last=($lines | Select -Last 1) }
$quota = [bool]($out -match "code': 429|rate.limit|rate_limit_exceeded|Rate limit reached|temporarily rate-limited|RESOURCE_EXHAUSTED")
"RESULTJSON " + (@{bot=$bot.id;status=$status;secs=[int]((Get-Date)-$t0).TotalSeconds;staged=$staged;produced=$produced;reply="$last".Trim();quota=$quota;log="C:\AI\Factory\run\logs\$sid.log";chain=$cfg.agents.defaults.modelPreset}|ConvertTo-Json -Compress)
