# Runs a factory bot's acceptance tests on the laptop.
# Usage: run-bot-tests.ps1 -BotDir C:\AI\Factory\bots\002-research-scout [-Cap 400]
param([Parameter(Mandatory=$true)][string]$BotDir,[int]$Cap=400,[int]$Only=0,[string]$Lane='')
$ErrorActionPreference='Continue'
$env:GROQ_API_KEY=[Environment]::GetEnvironmentVariable('GROQ_API_KEY','User')
$env:GEMINI_API_KEY=[Environment]::GetEnvironmentVariable('GEMINI_API_KEY','User')
$env:OPENROUTER_API_KEY=[Environment]::GetEnvironmentVariable('OPENROUTER_API_KEY','User')
$bot=Get-Content "$BotDir\bot.json" -Raw -Encoding UTF8|ConvertFrom-Json
$patch=Get-Content "$BotDir\nanobot.patch.json" -Raw -Encoding UTF8|ConvertFrom-Json
# per-bot config = live config + bot's model chain (tool set via env for this process only)
$cfg=Get-Content C:\AI\Factory\config.json -Raw -Encoding UTF8|ConvertFrom-Json
# D-040: chain is re-resolved against the live registry (lane health) every run; frozen chain is the fallback
$env:AIFACTORY_REPO='C:\AI\Factory\repo'
$live = python C:\AI\Factory\repo\tools\factory_chain.py $BotDir | ConvertFrom-Json
# D-050: -Lane pins ONE preset with no fallbacks so a benchmark score is attributable to that lane alone
if($Lane){ $cfg.agents.defaults.modelPreset=$Lane; $cfg.agents.defaults.fallbackModels=@(); $live=@{source="pinned:$Lane"} }
elseif($live -and $live.primary){ $cfg.agents.defaults.modelPreset=$live.primary; $cfg.agents.defaults.fallbackModels=@($live.fallbacks) }
else { $cfg.agents.defaults.modelPreset=$patch.agents.defaults.modelPreset; $cfg.agents.defaults.fallbackModels=@($patch.agents.defaults.fallbackModels) }
# small-TPM lanes: keep tool results tiny so compaction never has to hard-fail
$cfg.agents.defaults.maxToolResultChars=1500
New-Item -ItemType Directory -Force C:\AI\Factory\run\botcfg | Out-Null; $botCfg="C:\AI\Factory\run\botcfg\$($bot.id)$(if($Lane){"-$Lane"}).json"
[IO.File]::WriteAllText($botCfg,($cfg|ConvertTo-Json -Depth 20),(New-Object Text.UTF8Encoding($false)))
$env:AIFACTORY_DISABLED_TOOLS=$patch.env.AIFACTORY_DISABLED_TOOLS
$env:AIFACTORY_TEMPLATE_DIR="$BotDir\templates"
"bot $($bot.id) $($bot.name)  chain=$($cfg.agents.defaults.modelPreset),$($cfg.agents.defaults.fallbackModels -join ',') [$($live.source)]"
$pass=0; $total=0; $idx=0; $quota=0; $timeouts=0; $ev=@(); $suiteStart=Get-Date
foreach($t in $bot.tests){
  $idx++
  if($Only -and $idx -ne $Only){ continue }
  $total++
  $i=$t.LastIndexOf('->'); if($i -ge 0){ $prompt=$t.Substring(0,$i).Trim(); $expect=$t.Substring($i+2).Trim() } else { $prompt=$t.Trim(); $expect='' }
  $sid="bot$($bot.id)$(if($Lane){"-$Lane"})-t$idx-$(Get-Date -Format HHmmss)"; $t0=Get-Date
  $job=Start-Job -ScriptBlock { param($nb,$m,$s,$c,$w,$k,$d,$td,$gk,$ok) $env:GROQ_API_KEY=$k; $env:GEMINI_API_KEY=$gk; $env:OPENROUTER_API_KEY=$ok; $env:AIFACTORY_DISABLED_TOOLS=$d; $env:AIFACTORY_TEMPLATE_DIR=$td; & $nb agent -m ($m -replace '"','\"') -s $s --classic --no-markdown --config $c --workspace $w 2>&1 | Out-String } -ArgumentList 'C:\AI\Factory\.venv\Scripts\nanobot.exe',$prompt,$sid,$botCfg,$BotDir,$env:GROQ_API_KEY,$env:AIFACTORY_DISABLED_TOOLS,$env:AIFACTORY_TEMPLATE_DIR,$env:GEMINI_API_KEY,$env:OPENROUTER_API_KEY
  if(Wait-Job $job -Timeout $Cap){ $out=(Receive-Job $job|Out-String); $status='done' } else { Stop-Job $job; $out=(Receive-Job $job|Out-String); $status='TIMEOUT'; Get-Process nanobot -ErrorAction SilentlyContinue|Stop-Process -Force }
  Remove-Job $job -Force
  New-Item -ItemType Directory -Force "C:\AI\Factory\run\logs" | Out-Null; Set-Content "C:\AI\Factory\run\logs\$sid.log" $out
  # keep artefacts produced by this test for inspection (workspace files, excluding bundle/runtime)
  $art="C:\AI\Factory\run\artefacts\$sid"; New-Item -ItemType Directory -Force $art | Out-Null
  Get-ChildItem $BotDir -File | ? { $_.Name -notmatch '^(AGENTS|SOUL|TESTS|RECOVERY|TEST_RESULTS|HEARTBEAT|USER)\.md$|^bot\.json$|^nanobot\.patch\.json$|^\.gitignore$' } | % { Copy-Item $_.FullName $art -Force; Remove-Item $_.FullName -Force }
  $el=[int]((Get-Date)-$t0).TotalSeconds
  # D-059: judge the whole final RESULT block, not the last physical line. Rich wraps long replies at ~80 cols inside a
  # background job, so "RESULT: Wrote CHANGELOG.md with 3 entries" arrived as two lines and only "entries…" was checked.
  $lines=@(($out.Trim() -split "`n") | Where-Object { $_ -notmatch '^\s*✻' -and $_.Trim() } | % { $_.TrimEnd("`r") })
  $ri=-1; for($li=0; $li -lt $lines.Count; $li++){ if($lines[$li] -match '^\s*(RESULT|ANSWER|OUTPUT)\s*[:=]'){ $ri=$li } }
  if($ri -ge 0){ $last=(($lines[$ri..($lines.Count-1)] | Select -First 4) -join ' ') } else { $last=($lines | Select -Last 1) }
  $lastClean=("$last".Trim() -replace '^(RESULT|ANSWER|OUTPUT)\s*[:=]\s*','')
  $tok='(^|[\s`"''(\[])' + [regex]::Escape($expect) + '([\s`"'')\].,;:!?]|$)'
  $ok = ($status -eq 'done') -and ( ($expect -eq '' -and $last) -or ($expect -ne '' -and ($lastClean -eq $expect -or $lastClean -match $tok)) )
  if($ok){ $pass++ }
  # D-051: a 429/quota answer is an availability failure, not a quality failure — counted separately so benchmarks stay attributable
  if(-not $ok -and ($out -match "code': 429|rate.limit|rate_limit_exceeded|Rate limit reached|temporarily rate-limited|RESOURCE_EXHAUSTED")){ $quota++ }
  # D-080: report every 429 with the model and the provider's retry-after so the worker cools that lane immediately
  foreach($qm in [regex]::Matches($out, "Rate limit reached for model ``([^``]+)``[\s\S]{0,400}?try\s+again in (?:(\d+)h)?(?:(\d+)m)?(?:([\d.]+)s)?")){
    $qs=[int]([int]"0$($qm.Groups[2].Value)"*3600 + [int]"0$($qm.Groups[3].Value)"*60 + [double]"0$($qm.Groups[4].Value)")
    $kind = if($qm.Value -match 'per day \(TPD\)|\(TPD\)'){ 'tpd' } elseif($qm.Value -match 'per day \(RPD\)'){ 'rpd' } else { 'tpm' }
    "QUOTAHIT " + (@{model=$qm.Groups[1].Value;secs=$(if($qs -gt 0){$qs+30}else{900});kind=$kind}|ConvertTo-Json -Compress) }
  if(($out -match "RESOURCE_EXHAUSTED") -and ($out -match "model[s/:\s]+([\w.\-]+)")){ "QUOTAHIT " + (@{model=$Matches[1];secs=$(if($out -match "retryDelay['`":\s]+(\d+)s"){[int]$Matches[1]+30}else{900})}|ConvertTo-Json -Compress) }
  elseif(-not $ok -and $status -eq 'TIMEOUT'){ $timeouts++ }   # D-075: a wall-clock timeout with no answer is availability, not quality
  $line="T$idx $(if($ok){'PASS'}else{'FAIL'}) ${el}s [$status] expect='$expect' last='$($("$last".Trim()))'"; $line; $ev+=$line
}
"SCORE $pass/$total"
if(-not $Lane){ Set-Content "$BotDir\TEST_RESULTS.md" ("# Test run $(Get-Date -Format s)`n`n" + ($ev -join "`n") + "`n`nSCORE $pass/$total`n") }
"RESULTJSON " + (@{bot=$bot.id;lane=$Lane;pass=$pass;total=$total;quota=$quota;timeouts=$timeouts;secs=[int]((Get-Date)-$suiteStart).TotalSeconds;evidence=($ev -join ' | ')}|ConvertTo-Json -Compress)
