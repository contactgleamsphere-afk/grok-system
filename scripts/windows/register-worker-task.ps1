$cmd = 'powershell -NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File C:\AI\Factory\tools\run-worker.ps1'
schtasks /Create /TN "AIFactory Worker" /SC MINUTE /MO 15 /TR $cmd /F | Out-Null
schtasks /Create /TN "AIFactory Worker Logon" /SC ONLOGON /TR $cmd /F | Out-Null
schtasks /Run /TN "AIFactory Worker" | Out-Null
Start-Sleep 5
schtasks /Query /TN "AIFactory Worker" /FO LIST | Select-String 'TaskName|Status|Next Run'
Get-Process python -ErrorAction SilentlyContinue | ? { $_.CommandLine -match 'factory_worker' } | Select -Expand Id
