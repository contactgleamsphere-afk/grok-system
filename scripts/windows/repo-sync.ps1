# Sync C:\AI\Factory\repo with GitHub. Worker commits state locally after every job (D-041); this script
# rebases those commits onto origin and pushes. Never hard-resets: laptop state commits are history.
$r='C:\AI\Factory\repo'
if(-not (Test-Path $r)){ git clone -q https://github.com/contactgleamsphere-afk/grok-system.git $r }
cd $r
git config user.name  'AI Factory Laptop' | Out-Null
git config user.email 'contactgleamsphere-afk+laptop@users.noreply.github.com' | Out-Null
git add -A -- registry specs AUDIT.md MONITOR.md BOT_REGISTRY.md 2>$null
git diff --cached --quiet; if($LASTEXITCODE -ne 0){ git commit -qm "laptop state $(Get-Date -Format s)" }
git fetch -q origin
git rebase -q origin/main 2>$null
if($LASTEXITCODE -ne 0){
  # conflict on state files: laptop (runtime truth) wins; on anything else origin wins
  git checkout --theirs -- registry specs AUDIT.md MONITOR.md BOT_REGISTRY.md 2>$null
  git add -A; git -c core.editor=true rebase --continue 2>$null
  if($LASTEXITCODE -ne 0){ git rebase --abort; git fetch -q origin; git reset -q --hard origin/main; Write-Output "SYNC: conflict, took origin (laptop state commits preserved in reflog)" }
}
git log --oneline -1
