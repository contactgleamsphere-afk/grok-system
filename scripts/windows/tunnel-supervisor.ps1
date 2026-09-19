# AI Factory tunnel supervisor: keeps cloudflared quick tunnel alive and publishes its URL to GitHub (run/tunnel.txt).
$ErrorActionPreference='Continue'
$log='C:\AI\Factory\run\cloudflared.log'; $urlFile='C:\AI\Factory\run\tunnel.txt'
$tokFile='C:\AI\Factory\secrets\github_publish.token'
New-Item -ItemType Directory -Force C:\AI\Factory\run | Out-Null
function Publish($url){
  if(-not (Test-Path $tokFile)){ return }
  $tok=(Get-Content $tokFile -Raw).Trim(); $repo='contactgleamsphere-afk/grok-system'; $path='run/tunnel.txt'
  $hdr=@{Authorization="Bearer $tok"; 'User-Agent'='ai-factory-tunnel'; Accept='application/vnd.github+json'}
  $body=@{message="tunnel: $(Get-Date -Format s)"; content=[Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes("$url`n$(Get-Date -Format o)`n"))}
  try{ $cur=Invoke-RestMethod -Uri "https://api.github.com/repos/$repo/contents/$path" -Headers $hdr -Method Get; $body.sha=$cur.sha }catch{}
  try{ Invoke-RestMethod -Uri "https://api.github.com/repos/$repo/contents/$path" -Headers $hdr -Method Put -Body ($body|ConvertTo-Json) -ContentType 'application/json' | Out-Null; Add-Content $log "$(Get-Date -Format s) published $url" }catch{ Add-Content $log "$(Get-Date -Format s) publish FAILED: $($_.Exception.Message)" }
}
while($true){
  if(Test-Path $log){ if((Get-Item $log).Length -gt 5MB){ Remove-Item $log -Force } }
  $psi=New-Object Diagnostics.ProcessStartInfo; $psi.FileName='C:\AI\Factory\tools\cloudflared.exe'; $psi.Arguments='tunnel --url ssh://localhost:22 --no-autoupdate'
  $psi.RedirectStandardError=$true; $psi.RedirectStandardOutput=$true; $psi.UseShellExecute=$false; $psi.CreateNoWindow=$true
  $p=[Diagnostics.Process]::Start($psi); $published=$false
  while(-not $p.HasExited){
    $line=$p.StandardError.ReadLine(); if($null -eq $line){ Start-Sleep 1; continue }
    Add-Content $log $line
    if(-not $published -and $line -match 'https://[a-z0-9-]+\.trycloudflare\.com'){ $u=$Matches[0]; Set-Content $urlFile $u; Publish $u; $published=$true }
  }
  Add-Content $log "$(Get-Date -Format s) cloudflared exited code $($p.ExitCode); restarting in 15s"; Start-Sleep 15
}
