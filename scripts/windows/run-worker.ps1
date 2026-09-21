# Persistent factory worker: drains the job queue; restarted by Task Scheduler at logon and every 15 min if not running.
foreach($k in 'GROQ_API_KEY','GEMINI_API_KEY','OPENROUTER_API_KEY'){ Set-Item env:$k ([Environment]::GetEnvironmentVariable($k,'User')) }
$env:AIFACTORY_REPO='C:\AI\Factory\repo'; $env:PYTHONIOENCODING='utf-8'
$lock='C:\AI\Factory\run\worker.lock'
if(Test-Path $lock){ $pid0=Get-Content $lock; if(Get-Process -Id $pid0 -ErrorAction SilentlyContinue){ exit 0 } }
Set-Content $lock $PID
# D-038: the local tail lane must exist whenever the factory runs
try { Invoke-WebRequest -UseBasicParsing http://127.0.0.1:11434/api/tags -TimeoutSec 3 | Out-Null } catch {
  $ol = "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe"; if(Test-Path $ol){ Start-Process $ol -ArgumentList 'serve' -WindowStyle Hidden; Start-Sleep 6 }
}
cd C:\AI\Factory\repo
python tools\factory_worker.py run --worker "svc-$env:COMPUTERNAME" 2>&1 | Out-File -Append "C:\AI\Factory\run\worker-$(Get-Date -Format yyyyMMdd).log"
Remove-Item $lock -Force -ErrorAction SilentlyContinue
