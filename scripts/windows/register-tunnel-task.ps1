$a = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument '-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -Command "& C:\AI\Factory\tools\tunnel-supervisor.ps1 *>> C:\AI\Factory\run\supervisor.err"'
$t = @((New-ScheduledTaskTrigger -AtStartup),(New-ScheduledTaskTrigger -AtLogOn))
$s = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -RestartCount 999 -RestartInterval (New-TimeSpan -Minutes 1) -ExecutionTimeLimit ([TimeSpan]::Zero) -MultipleInstances IgnoreNew -StartWhenAvailable
$p = New-ScheduledTaskPrincipal -UserId 'SYSTEM' -LogonType ServiceAccount -RunLevel Highest
Stop-ScheduledTask AIFactory-Tunnel -ErrorAction SilentlyContinue
Get-CimInstance Win32_Process -Filter "name='cloudflared.exe'" | Where-Object { $_.CommandLine -like '*--no-autoupdate*' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }
Register-ScheduledTask -TaskName AIFactory-Tunnel -Action $a -Trigger $t -Settings $s -Principal $p -Force | Out-Null
Start-ScheduledTask AIFactory-Tunnel
Start-Sleep 30
"TASK: " + (Get-ScheduledTask AIFactory-Tunnel).State
Get-Process cloudflared | Select Id,StartTime | Format-Table -AutoSize
"--- supervisor.err"; Get-Content C:\AI\Factory\run\supervisor.err -Tail 20 -ErrorAction SilentlyContinue
"--- supervisor.log"; Get-Content C:\AI\Factory\run\supervisor.log -Tail 20 -ErrorAction SilentlyContinue
"--- tunnel.txt"; Get-Content C:\AI\Factory\run\tunnel.txt
