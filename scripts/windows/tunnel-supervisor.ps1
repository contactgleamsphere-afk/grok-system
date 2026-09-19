# AI Factory tunnel supervisor v2 (2026-09-19)
# Keeps a cloudflared quick tunnel alive and publishes its URL to GitHub (run/tunnel.txt).
# v2: health-checked. v1 only restarted on process EXIT; after a network outage cloudflared
# retries "Unauthorized: Tunnel not found" forever without exiting -> zombie. Now we restart on:
#   (a) >=3 "Tunnel not found" errors, (b) no "Registered tunnel connection" within 90s of start,
#   (c) external probe of the URL returns HTTP 530/no route 3 times in a row (every 60s),
#   (d) process exit.
$ErrorActionPreference='Continue'
$root='C:\AI\Factory'; $run="$root\run"
$log="$run\cloudflared.log"; $slog="$run\supervisor.log"; $urlFile="$run\tunnel.txt"
$tokFile="$root\secrets\github_publish.token"; $exe="$root\tools\cloudflared.exe"
New-Item -ItemType Directory -Force $run | Out-Null
function Write-SupLog($m){ Add-Content $slog "$(Get-Date -Format s) $m" }
function Publish($url){
  if(-not (Test-Path $tokFile)){ Write-SupLog "no token file; not publishing"; return }
  $tok=(Get-Content $tokFile -Raw).Trim(); $repo='contactgleamsphere-afk/grok-system'; $path='run/tunnel.txt'
  $hdr=@{Authorization="Bearer $tok"; 'User-Agent'='ai-factory-tunnel'; Accept='application/vnd.github+json'}
  $body=@{message="tunnel: $(Get-Date -Format s)"; content=[Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes("$url`n$(Get-Date -Format o)`n"))}
  for($i=1;$i -le 5;$i++){
    try{ $cur=Invoke-RestMethod -Uri "https://api.github.com/repos/$repo/contents/$path" -Headers $hdr -Method Get -TimeoutSec 20; $body.sha=$cur.sha }catch{}
    try{ Invoke-RestMethod -Uri "https://api.github.com/repos/$repo/contents/$path" -Headers $hdr -Method Put -Body ($body|ConvertTo-Json) -ContentType 'application/json' -TimeoutSec 20 | Out-Null; Write-SupLog "published $url (attempt $i)"; return }
    catch{ Write-SupLog "publish attempt $i FAILED: $($_.Exception.Message)"; Start-Sleep (10*$i) }
  }
}
function Probe($url){
  # dead quick tunnel => Cloudflare error 1033 (HTTP 530). Live ssh tunnel => 200/400/502-ish but not 530.
  try{ $r=Invoke-WebRequest -Uri $url -UseBasicParsing -TimeoutSec 15 -MaximumRedirection 0; return $r.StatusCode }
  catch{ $resp=$_.Exception.Response; if($resp){ return [int]$resp.StatusCode } else { return -1 } }
}
# kill orphans from a previous supervisor instance only (children of a supervisor powershell, or parent dead).
# Never touches a user's manually started cloudflared window.
$supPids=(Get-CimInstance Win32_Process -Filter "name='powershell.exe'" | Where-Object { $_.CommandLine -like '*tunnel-supervisor.ps1*' -and $_.ProcessId -ne $PID }).ProcessId
Get-CimInstance Win32_Process -Filter "name='cloudflared.exe'" | ForEach-Object {
  $parentAlive = [bool](Get-Process -Id $_.ParentProcessId -ErrorAction SilentlyContinue)
  if(($supPids -contains $_.ParentProcessId) -or -not $parentAlive){ Write-SupLog "killing orphan cloudflared $($_.ProcessId)"; Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }
}
Write-SupLog "supervisor v2 start pid=$PID"
while($true){
  foreach($f in @($log,$slog)){ if((Test-Path $f) -and (Get-Item $f).Length -gt 5MB){ Move-Item $f "$f.1" -Force } }
  if(Test-Path $log){ Remove-Item $log -Force }
  $p=Start-Process -FilePath $exe -ArgumentList 'tunnel --url ssh://localhost:22 --no-autoupdate' -RedirectStandardError $log -WindowStyle Hidden -PassThru
  Write-SupLog "started cloudflared pid=$($p.Id)"
  $start=Get-Date; $url=$null; $registered=$false; $notFound=0; $probeFail=0; $lastProbe=Get-Date; $pos=0; $reason=$null
  while(-not $p.HasExited){
    Start-Sleep 2
    # read new log lines
    if(Test-Path $log){
      try{ $fs=[IO.File]::Open($log,'Open','Read','ReadWrite'); $fs.Seek($pos,'Begin')|Out-Null; $sr=New-Object IO.StreamReader($fs); $new=$sr.ReadToEnd(); $pos=$fs.Position; $sr.Close(); $fs.Close() }catch{ $new='' }
      foreach($line in ($new -split "`n")){
        if(-not $url -and $line -match 'https://[a-z0-9-]+\.trycloudflare\.com'){ $url=$Matches[0]; Set-Content $urlFile $url; Write-SupLog "url $url"; Publish $url }
        if($line -match 'Registered tunnel connection'){ $registered=$true; $notFound=0 }
        if($line -match 'Tunnel not found'){ $notFound++ }
      }
    }
    $age=((Get-Date)-$start).TotalSeconds
    if($notFound -ge 3){ $reason="tunnel expired server-side ($notFound x 'Tunnel not found')"; break }
    if(-not $registered -and $age -gt 90){ $reason="no registered connection after 90s"; break }
    if(-not $url -and $age -gt 60){ $reason="no URL after 60s"; break }
    if($url -and $registered -and ((Get-Date)-$lastProbe).TotalSeconds -ge 60){
      $lastProbe=Get-Date; $code=Probe $url
      if($code -eq 530 -or $code -eq -1){ $probeFail++; Write-SupLog "probe $url -> $code (fail $probeFail/3)" } else { $probeFail=0 }
      if($probeFail -ge 3){ $reason="external probe failed 3x (last=$code)"; break }
    }
  }
  if($p.HasExited){ $reason="cloudflared exited code $($p.ExitCode)" }
  else { Stop-Process -Id $p.Id -Force -ErrorAction SilentlyContinue; Start-Sleep 2 }
  Write-SupLog "restart: $reason"
  # wait for internet before relaunch (avoid burning quick-tunnel creates while offline)
  $w=0; while(-not (Test-Connection 1.1.1.1 -Count 1 -Quiet) -and $w -lt 600){ Start-Sleep 10; $w+=10 }
  if($w -gt 0){ Write-SupLog "network back after ${w}s" }
  Start-Sleep 10
}
