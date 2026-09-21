foreach($k in 'GROQ_API_KEY','GEMINI_API_KEY','OPENROUTER_API_KEY'){ Set-Item env:$k ([Environment]::GetEnvironmentVariable($k,'User')) }
$env:AIFACTORY_REPO='C:\AI\Factory\repo'; $env:PYTHONIOENCODING='utf-8'
& C:\AI\Factory\tools\repo-sync.ps1 | Out-Null
try { Invoke-RestMethod -Method Post http://127.0.0.1:11434/api/generate -Body (@{model='qwen3:4b';prompt='hi';stream=$false;keep_alive='60m';options=@{num_predict=2}}|ConvertTo-Json) -ContentType 'application/json' -TimeoutSec 600 | Out-Null } catch {}
cd C:\AI\Factory\repo
python tools\factory_worker.py add monitor --actor nightly-task
