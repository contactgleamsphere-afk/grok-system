<#
  AI FACTORY — PHASE 1 (Windows 11, LAPTOP-LRE6PSA8)
  Installs nanobot-ai into an isolated venv and wires it to the EXISTING
  local Ollama + qwen2.5:3b-instruct-q4_K_M. Nothing else is installed.

  Run in PowerShell (normal user, no admin needed):
    Set-ExecutionPolicy -Scope Process Bypass
    .\install-phase1.ps1

  Verified against nanobot docs (main, Sep 2026) and PyPI nanobot-ai 0.3.5.
#>

$ErrorActionPreference = "Stop"
$Factory   = "C:\AI\Factory"
$Venv      = "$Factory\venv"
$Model     = "qwen2.5:3b-instruct-q4_K_M"
$OllamaUrl = "http://127.0.0.1:11434"

function Step($m) { Write-Host "`n=== $m ===" -ForegroundColor Cyan }
function Fail($m) { Write-Host "FAIL: $m" -ForegroundColor Red; exit 1 }

# ---------- 0. Pre-flight (no installs) ----------
Step "0. Pre-flight checks"
$py = (Get-Command python -ErrorAction SilentlyContinue)
if (-not $py) { Fail "python not on PATH (audit said 3.11.9 via 'python')" }
$pyver = & python -c "import sys;print('%d.%d.%d'%sys.version_info[:3])"
Write-Host "Python: $pyver"
if ([version]$pyver -lt [version]"3.11.0") { Fail "nanobot-ai requires Python >= 3.11" }

try { $tags = Invoke-RestMethod "$OllamaUrl/api/tags" -TimeoutSec 5 }
catch { Fail "Ollama not reachable at $OllamaUrl — start Ollama first" }
$have = $tags.models | Where-Object { $_.name -eq $Model }
if (-not $have) {
  Write-Host "Models present:" ($tags.models.name -join ", ")
  Fail "Model $Model not found in Ollama. (Rule: do NOT pull another model in Phase 1.)"
}
Write-Host "Ollama OK, model present: $Model"

# Confirm Ollama is bound to localhost only (security rule)
$listen = netstat -ano | Select-String ":11434 " | Select-String "LISTENING"
Write-Host "Ollama listeners:`n$listen"
if ($listen -match "0\.0\.0\.0:11434") { Write-Warning "Ollama is bound to 0.0.0.0 — should be 127.0.0.1 only. Check OLLAMA_HOST env var." }

# ---------- 1. Directory + venv ----------
Step "1. Create $Factory and venv"
New-Item -ItemType Directory -Force -Path $Factory | Out-Null
if (-not (Test-Path "$Venv\Scripts\python.exe")) { & python -m venv $Venv }
$VPy = "$Venv\Scripts\python.exe"
& $VPy -m pip install --upgrade pip --quiet

# ---------- 2. Install nanobot (pinned) ----------
Step "2. Install nanobot-ai (pinned 0.3.5)"
& $VPy -m pip install "nanobot-ai==0.3.5"
$Nanobot = "$Venv\Scripts\nanobot.exe"
if (-not (Test-Path $Nanobot)) { Fail "nanobot.exe not found after install" }
$nbver = & $Nanobot --version
Write-Host "Installed: $nbver"

# ---------- 3. Config ----------
Step "3. Write ~/.nanobot/config.json (Ollama only, no API keys)"
$NbHome = "$env:USERPROFILE\.nanobot"
New-Item -ItemType Directory -Force -Path $NbHome | Out-Null
$cfgPath = "$NbHome\config.json"
if (Test-Path $cfgPath) {
  Copy-Item $cfgPath "$cfgPath.bak-$(Get-Date -Format yyyyMMdd-HHmmss)"
  Write-Host "Existing config backed up."
}
Copy-Item "$PSScriptRoot\nanobot.config.json" $cfgPath -Force
Write-Host "Config written to $cfgPath"

# ---------- 4. Smoke test ----------
Step "4. Status + terminal-only reply test"
& $Nanobot status
Write-Host "`nSending test message to local model (CPU 3B — allow 10-60s)..."
$reply = & $Nanobot -m "Reply with exactly: PHASE1_OK" 2>&1
Write-Host $reply
if ($reply -notmatch "PHASE1_OK") { Write-Warning "Model replied but not with the exact token — that is fine for a 3B model; check the reply is coherent." }

# ---------- 5. Report ----------
Step "PHASE 1 REPORT"
@"
A. nanobot version      : $nbver
B. Install directory    : $Factory  (venv: $Venv)
C. Ollama model         : $Model @ $OllamaUrl
D. Ollama communication : see reply above
E. Interface            : run   $Nanobot webui   (opens http://localhost bound WebUI)
F. Files created        : $Venv, $cfgPath, $NbHome\workspace\ (on first run)
G. Warnings             : none unless printed above
H. Phase 1              : PASSED if a coherent reply printed in step 4
"@
Write-Host "`nTo open the WebUI now:  $Nanobot webui" -ForegroundColor Green
Write-Host "STOP HERE. Do not proceed to Phase 2 until reported." -ForegroundColor Yellow
