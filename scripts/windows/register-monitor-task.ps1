# Nightly 03:30 re-verification of every active factory bot (Windows Task Scheduler, current user, no admin).
$cmd = 'powershell -NoProfile -ExecutionPolicy Bypass -File C:\AI\Factory\tools\run-monitor.ps1'
schtasks /Create /TN "AIFactory Monitor" /SC DAILY /ST 03:30 /TR $cmd /F | Out-Null
schtasks /Query /TN "AIFactory Monitor" /FO LIST | Select-String 'TaskName|Next Run|Status'
