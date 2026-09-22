# Persistent factory worker supervisor. Started by Task Scheduler at logon and every 15 min (no-op if already alive).
foreach($k in 'GROQ_API_KEY','GEMINI_API_KEY','OPENROUTER_API_KEY','GITHUB_TOKEN'){ Set-Item env:$k ([Environment]::GetEnvironmentVariable($k,'User')) }
$env:AIFACTORY_REPO='C:\AI\Factory\repo'; $env:PYTHONIOENCODING='utf-8'
$lock='C:\AI\Factory\run\worker.lock'
if(Test-Path $lock){
  $old=[int](Get-Content $lock -ErrorAction SilentlyContinue)
  if($old -and (Get-Process -Id $old -ErrorAction SilentlyContinue)){ exit 0 }   # supervisor already alive
}
Set-Content $lock $PID
New-Item -ItemType Directory -Force C:\AI\Factory\run\logs | Out-Null
Start-Transcript -Path "C:\AI\Factory\run\logs\supervisor-$PID.txt" -Force | Out-Null
try {
  # D-038: the local tail lane must exist whenever the factory runs
  try { Invoke-WebRequest -UseBasicParsing http://127.0.0.1:11434/api/tags -TimeoutSec 3 | Out-Null } catch {
    $ol = "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe"; if(Test-Path $ol){ Start-Process $ol -ArgumentList 'serve' -WindowStyle Hidden; Start-Sleep 6 }
  }
  cd C:\AI\Factory\repo
  while($true){
    # one log file per supervisor process -> no sharing violations between overlapping instances
    $log = "C:\AI\Factory\run\logs\worker-$(Get-Date -Format yyyyMMdd)-$PID.log"
    New-Item -ItemType Directory -Force C:\AI\Factory\run\logs | Out-Null
    # D-079: a second worker serves only short job kinds so owner runs / schedules / probes are never stuck behind a
    # 30-minute create/repair. Per-bot exclusion is enforced in JobStore.claim, so both can never touch the same bot.
    $fast = Get-CimInstance Win32_Process -Filter "name='python.exe'" | Where-Object { $_.CommandLine -like '*factory_worker.py run*--fast-lane*' }
    if(-not $fast){ Start-Process python -ArgumentList 'tools\factory_worker.py','run','--worker',"fast-$env:COMPUTERNAME",'--fast-lane','--respawn' -WorkingDirectory C:\AI\Factory\repo -WindowStyle Hidden -RedirectStandardOutput "C:\AI\Factory\run\logs\fast-$(Get-Date -Format yyyyMMdd)-$PID.log" -RedirectStandardError "C:\AI\Factory\run\logs\fast-$(Get-Date -Format yyyyMMdd)-$PID.err" }
    & python tools\factory_worker.py run --worker "svc-$env:COMPUTERNAME" *>> $log
    Start-Sleep 3   # worker exits on code change (D-039) -> relaunch with fresh modules
  }
} finally { Stop-Transcript | Out-Null; if((Get-Content $lock -ErrorAction SilentlyContinue) -eq "$PID"){ Remove-Item $lock -Force -ErrorAction SilentlyContinue } }
