# Runs a factory bot's acceptance tests on the laptop.
# Usage: run-bot-tests.ps1 -BotDir C:\AI\Factory\bots\002-research-scout [-Cap 400]
param([Parameter(Mandatory=$true)][string]$BotDir,[int]$Cap=400,[int]$Only=0)
$ErrorActionPreference='Continue'
$env:GROQ_API_KEY=[Environment]::GetEnvironmentVariable('GROQ_API_KEY','User')
$env:GEMINI_API_KEY=[Environment]::GetEnvironmentVariable('GEMINI_API_KEY','User')
$env:OPENROUTER_API_KEY=[Environment]::GetEnvironmentVariable('OPENROUTER_API_KEY','User')
$bot=Get-Content "$BotDir\bot.json" -Raw -Encoding UTF8|ConvertFrom-Json
$patch=Get-Content "$BotDir\nanobot.patch.json" -Raw -Encoding UTF8|ConvertFrom-Json
# per-bot config = live config + bot's model chain (tool set via env for this process only)
$cfg=Get-Content C:\AI\Factory\config.json -Raw -Encoding UTF8|ConvertFrom-Json
$cfg.agents.defaults.modelPreset=$patch.agents.defaults.modelPreset
$cfg.agents.defaults.fallbackModels=@($patch.agents.defaults.fallbackModels)
# small-TPM lanes: keep tool results tiny so compaction never has to hard-fail
$cfg.agents.defaults.maxToolResultChars=1500
New-Item -ItemType Directory -Force C:\AI\Factory\run\botcfg | Out-Null; $botCfg="C:\AI\Factory\run\botcfg\$($bot.id).json"
[IO.File]::WriteAllText($botCfg,($cfg|ConvertTo-Json -Depth 20),(New-Object Text.UTF8Encoding($false)))
$env:AIFACTORY_DISABLED_TOOLS=$patch.env.AIFACTORY_DISABLED_TOOLS
$env:AIFACTORY_TEMPLATE_DIR="$BotDir\templates"
"bot $($bot.id) $($bot.name)  chain=$($patch.agents.defaults.modelPreset),$($patch.agents.defaults.fallbackModels -join ',')"
$pass=0; $total=0; $idx=0; $ev=@()
foreach($t in $bot.tests){
  $idx++
  if($Only -and $idx -ne $Only){ continue }
  $total++
  $i=$t.LastIndexOf('->'); if($i -ge 0){ $prompt=$t.Substring(0,$i).Trim(); $expect=$t.Substring($i+2).Trim() } else { $prompt=$t.Trim(); $expect='' }
  $sid="bot$($bot.id)-t$idx-$(Get-Date -Format HHmmss)"; $t0=Get-Date
  $job=Start-Job -ScriptBlock { param($nb,$m,$s,$c,$w,$k,$d,$td,$gk,$ok) $env:GROQ_API_KEY=$k; $env:GEMINI_API_KEY=$gk; $env:OPENROUTER_API_KEY=$ok; $env:AIFACTORY_DISABLED_TOOLS=$d; $env:AIFACTORY_TEMPLATE_DIR=$td; & $nb agent -m ($m -replace '"','\"') -s $s --classic --no-markdown --config $c --workspace $w 2>&1 | Out-String } -ArgumentList 'C:\AI\Factory\.venv\Scripts\nanobot.exe',$prompt,$sid,$botCfg,$BotDir,$env:GROQ_API_KEY,$env:AIFACTORY_DISABLED_TOOLS,$env:AIFACTORY_TEMPLATE_DIR,$env:GEMINI_API_KEY,$env:OPENROUTER_API_KEY
  if(Wait-Job $job -Timeout $Cap){ $out=(Receive-Job $job|Out-String); $status='done' } else { Stop-Job $job; $out=(Receive-Job $job|Out-String); $status='TIMEOUT'; Get-Process nanobot -ErrorAction SilentlyContinue|Stop-Process -Force }
  Remove-Job $job -Force
  New-Item -ItemType Directory -Force "C:\AI\Factory\run\logs" | Out-Null; Set-Content "C:\AI\Factory\run\logs\$sid.log" $out
  $el=[int]((Get-Date)-$t0).TotalSeconds
  $last=(($out.Trim() -split "`n") | Where-Object { $_ -notmatch '^\s*✻' -and $_.Trim() } | Select -Last 1)
  $lastClean=("$last".Trim() -replace '^(RESULT|ANSWER|OUTPUT)\s*[:=]\s*','')
  $ok = ($status -eq 'done') -and ( ($expect -eq '' -and $last) -or ($expect -ne '' -and ($lastClean -eq $expect -or $lastClean -match ('(^|\s)' + [regex]::Escape($expect) + '(\s|$)'))) )
  if($ok){ $pass++ }
  $line="T$idx $(if($ok){'PASS'}else{'FAIL'}) ${el}s [$status] expect='$expect' last='$($("$last".Trim()))'"; $line; $ev+=$line
}
"SCORE $pass/$total"
Set-Content "$BotDir\TEST_RESULTS.md" ("# Test run $(Get-Date -Format s)`n`n" + ($ev -join "`n") + "`n`nSCORE $pass/$total`n")
"RESULTJSON " + (@{bot=$bot.id;pass=$pass;total=$total;evidence=($ev -join ' | ')}|ConvertTo-Json -Compress)
