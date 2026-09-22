# Nightly 03:30 re-verification of every active factory bot (Windows Task Scheduler, current user, no admin).
# D-055: runs on battery (schtasks default silently skips when unplugged), catches up if the time was missed,
# and executes the REPO copy of run-monitor.ps1 (single source of truth).
$act = New-ScheduledTaskAction -Execute 'powershell' -Argument '-NoProfile -ExecutionPolicy Bypass -File C:\AI\Factory\repo\scripts\windows\run-monitor.ps1'
$trg = New-ScheduledTaskTrigger -Daily -At 03:30
$set = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -ExecutionTimeLimit (New-TimeSpan -Hours 6) -MultipleInstances IgnoreNew
Register-ScheduledTask -TaskName 'AIFactory Monitor' -Action $act -Trigger $trg -Settings $set -Force | Out-Null
$t = Get-ScheduledTask -TaskName 'AIFactory Monitor'; $i = $t | Get-ScheduledTaskInfo
"AIFactory Monitor: battery_ok=$(-not $t.Settings.DisallowStartIfOnBatteries) catchup=$($t.Settings.StartWhenAvailable) next=$($i.NextRunTime) action=$($t.Actions[0].Arguments)"
