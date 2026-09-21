# Registers the persistent worker supervisor as a scheduled task (idempotent). Interactive user session, no password stored.
$script = 'C:\AI\Factory\tools\run-worker.ps1'
$action  = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument "-NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File $script"
$trig1   = New-ScheduledTaskTrigger -AtLogOn -User $env:USERNAME
$trig2   = New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(1) -RepetitionInterval (New-TimeSpan -Minutes 15)
$set     = New-ScheduledTaskSettingsSet -MultipleInstances IgnoreNew -ExecutionTimeLimit ([TimeSpan]::Zero) -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -RestartCount 3 -RestartInterval (New-TimeSpan -Minutes 1)
foreach($n in 'AIFactory Worker','AIFactory Worker Logon'){ Unregister-ScheduledTask -TaskName $n -Confirm:$false -ErrorAction SilentlyContinue }
Register-ScheduledTask -TaskName 'AIFactory Worker' -Action $action -Trigger @($trig1,$trig2) -Settings $set -RunLevel Limited -Force | Out-Null
Start-ScheduledTask -TaskName 'AIFactory Worker'
Start-Sleep 20
Get-ScheduledTaskInfo -TaskName 'AIFactory Worker' | Select LastRunTime, LastTaskResult, NextRunTime
(Get-ScheduledTask -TaskName 'AIFactory Worker').State
Get-CimInstance Win32_Process | ? { $_.CommandLine -match 'run-worker|factory_worker\.py run' } | % { "$($_.ProcessId) $($_.Name)" }
