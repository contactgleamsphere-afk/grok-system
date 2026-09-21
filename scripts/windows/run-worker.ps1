# Persistent factory worker: drains the job queue; restarted by Task Scheduler at logon and every 15 min if not running.
foreach($k in 'GROQ_API_KEY','GEMINI_API_KEY','OPENROUTER_API_KEY'){ Set-Item env:$k ([Environment]::GetEnvironmentVariable($k,'User')) }
$env:AIFACTORY_REPO='C:\AI\Factory\repo'; $env:PYTHONIOENCODING='utf-8'
$lock='C:\AI\Factory\run\worker.lock'
if(Test-Path $lock){ $pid0=Get-Content $lock; if(Get-Process -Id $pid0 -ErrorAction SilentlyContinue){ exit 0 } }
Set-Content $lock $PID
cd C:\AI\Factory\repo
python tools\factory_worker.py run --worker "svc-$env:COMPUTERNAME" 2>&1 | Out-File -Append "C:\AI\Factory\run\worker-$(Get-Date -Format yyyyMMdd).log"
Remove-Item $lock -Force -ErrorAction SilentlyContinue
