# Keeps C:\AI\Factory\repo in sync with GitHub WITHOUT destroying laptop-generated state (registry, specs, run/, AUDIT, MONITOR).
$r='C:\AI\Factory\repo'
if(-not (Test-Path $r)){ git clone -q https://github.com/contactgleamsphere-afk/grok-system.git $r }
cd $r
git config user.name  'AI Factory Laptop' | Out-Null
git config user.email 'contactgleamsphere-afk+laptop@users.noreply.github.com' | Out-Null
git add -A registry specs bots MONITOR.md AUDIT.md BOT_REGISTRY.md 2>$null
git diff --cached --quiet; if($LASTEXITCODE -ne 0){ git commit -qm "laptop state $(Get-Date -Format s)" }
git fetch -q origin
git rebase -q origin/main 2>$null
if($LASTEXITCODE -ne 0){
  # conflict: laptop registry/specs win, everything else takes origin
  git checkout --theirs -- registry specs bots MONITOR.md AUDIT.md BOT_REGISTRY.md 2>$null
  git add -A; git -c core.editor=true rebase --continue 2>$null
  if($LASTEXITCODE -ne 0){ git rebase --abort; git merge -q -X theirs origin/main -m "merge origin (laptop state kept)" }
}
git log --oneline -1
