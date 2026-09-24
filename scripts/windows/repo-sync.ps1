# Sync C:\AI\Factory\repo with GitHub. Worker commits state locally after every job (D-041); this script
# rebases those commits onto origin and pushes. Never hard-resets: laptop state commits are history.
$r='C:\AI\Factory\repo'
if(-not (Test-Path $r)){ git clone -q https://github.com/contactgleamsphere-afk/grok-system.git $r }
cd $r
# D-101: one git writer at a time — same lock as factory_worker._commit_state (D-079). Two workers restarting on the same
# code push both ran this script at 01:20:29/01:21:05 and the second committed inside the first's rebase.
$lock = Join-Path $r 'run\git-state.lock'; New-Item -ItemType Directory -Force (Split-Path $lock) | Out-Null
$deadline = (Get-Date).AddSeconds(120)
while($true){
  try { $fs = [System.IO.File]::Open($lock, 'CreateNew', 'Write', 'None'); $fs.Close(); break } catch {}
  if((Test-Path $lock) -and ((Get-Date) - (Get-Item $lock).LastWriteTime).TotalSeconds -gt 300){ Remove-Item $lock -Force -ErrorAction SilentlyContinue; continue }
  if((Get-Date) -gt $deadline){ Write-Output "SYNC: lock busy, skipped"; exit 0 }
  Start-Sleep 1
}
try {
git config user.name  'AI Factory Laptop' | Out-Null
git config user.email 'contactgleamsphere-afk+laptop@users.noreply.github.com' | Out-Null
git add -A -- registry specs audit proposals AUDIT.md MONITOR.md BOT_REGISTRY.md STATUS.md 2>$null
git diff --cached --quiet; if($LASTEXITCODE -ne 0){ git commit -qm "laptop state $(Get-Date -Format s)" }
$tok=[Environment]::GetEnvironmentVariable('GITHUB_TOKEN','User'); $url="https://x-access-token:$tok@github.com/contactgleamsphere-afk/grok-system.git"
$env:GIT_TERMINAL_PROMPT='0'; $env:GCM_INTERACTIVE='Never'
git -c credential.helper= fetch -q $url main; git update-ref refs/remotes/origin/main FETCH_HEAD
# D-089: never let a dirty worktree (worker's selftest.json, half-written state) turn a clean rebase into a hard reset
git stash push -q --include-untracked -m "repo-sync autostash" 2>$null; $stashed = ($LASTEXITCODE -eq 0) -and ((git stash list | Select-String 'repo-sync autostash' | Measure-Object).Count -gt 0)
git rebase -q origin/main 2>$null
if($LASTEXITCODE -ne 0){
  # conflict on state files: laptop (runtime truth) wins; on anything else origin wins
  git checkout --theirs -- registry specs audit proposals AUDIT.md MONITOR.md BOT_REGISTRY.md STATUS.md 2>$null
  git add -A; git -c core.editor=true rebase --continue 2>$null
  if($LASTEXITCODE -ne 0){
    # D-101: NEVER reset --hard (it discarded the 002 demotion commit 4f563a4 on 2026-09-24 01:21). Fall back to a merge
    # where the laptop's state commits win every conflict; code files never conflict because the laptop never edits them.
    git rebase --abort 2>$null
    git merge -q --no-edit -X ours origin/main 2>$null
    if($LASTEXITCODE -ne 0){ git merge --abort 2>$null; Write-Output "SYNC: merge failed, local state kept unpushed (retry next sync)" }
    else { Write-Output "SYNC: rebase conflict -> merged, laptop state kept" }
  }
}
if($stashed){
  git stash pop -q 2>$null
  if($LASTEXITCODE -ne 0){
    # D-101: a conflicted pop keeps the STASHED (laptop) side for state files, origin for the rest; nothing is discarded
    git checkout --theirs -- registry specs audit proposals AUDIT.md MONITOR.md BOT_REGISTRY.md STATUS.md 2>$null
    git checkout --ours -- . 2>$null; git reset -q; git stash drop -q 2>$null
    Write-Output "SYNC: autostash conflicted, laptop state files kept"
  }
}
if($tok){ git -c credential.helper= push -q $url HEAD:main 2>&1 | Select -Last 1 }
git log --oneline -1
} finally { Remove-Item $lock -Force -ErrorAction SilentlyContinue }
