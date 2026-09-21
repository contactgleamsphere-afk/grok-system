foreach($k in 'GROQ_API_KEY','GEMINI_API_KEY','OPENROUTER_API_KEY'){ Set-Item env:$k ([Environment]::GetEnvironmentVariable($k,'User')) }
$env:AIFACTORY_REPO='C:\AI\Factory\repo'; $env:PYTHONIOENCODING='utf-8'
& C:\AI\Factory\tools\repo-sync.ps1 | Out-Null
try { Invoke-RestMethod -Method Post http://127.0.0.1:11434/api/generate -Body (@{model='qwen3:4b';prompt='hi';stream=$false;keep_alive='60m';options=@{num_predict=2}}|ConvertTo-Json) -ContentType 'application/json' -TimeoutSec 600 | Out-Null } catch {}
cd C:\AI\Factory\repo
$args2 = @(); if($args.Count){ $args2 = $args }
python tools\factory_monitor.py @args2 2>&1 | Tee-Object -FilePath "C:\AI\Factory\run\monitor-$(Get-Date -Format yyyyMMdd-HHmm).log"
# self-improvement v0: try to repair anything the monitor demoted (fail-closed; see D-029/D-030)
$b = Get-Content registry\bots.json -Raw | ConvertFrom-Json
foreach($p in $b.PSObject.Properties){ if($p.Value.status -eq 'testing' -and $p.Name -ne '001'){ "repairing $($p.Name)"; python tools\factory_repair.py $p.Name --max-rounds 2 2>&1 | Tee-Object -FilePath "C:\AI\Factory\run\repair-$($p.Name)-$(Get-Date -Format yyyyMMdd-HHmm).log" } }
