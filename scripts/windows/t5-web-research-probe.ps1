$env:GROQ_API_KEY=[Environment]::GetEnvironmentVariable('GROQ_API_KEY','User')
$t=Get-Date
& C:\AI\Factory\.venv\Scripts\nanobot.exe agent -m 'Use web search to find the current stable version number of the Python package nanobot-ai on PyPI and report only the version.' -s "t5-$(Get-Date -Format HHmmss)" --classic --no-markdown --logs --config C:\AI\Factory\config.json --workspace C:\AI\Factory\workspace 2>&1 | Out-File -Encoding utf8 C:\AI\Factory\run\t5.out
"elapsed $([int]((Get-Date)-$t).TotalSeconds)s"
