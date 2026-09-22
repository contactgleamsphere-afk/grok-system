$p='C:\AI\Factory\config.json'; $c=Get-Content $p -Raw | ConvertFrom-Json
function addp($n,$o){ if($c.modelPresets.PSObject.Properties[$n]){$c.modelPresets.$n=$o}else{$c.modelPresets | Add-Member -NotePropertyName $n -NotePropertyValue $o} }
addp 'gemini-lite'  ([pscustomobject]@{model='gemini-3.5-flash-lite';provider='gemini';maxTokens=2048;contextWindowTokens=32768;temperature=0.2})
addp 'gemini-flash' ([pscustomobject]@{model='gemini-3.7-flash';provider='gemini';maxTokens=2048;contextWindowTokens=32768;temperature=0.2})
addp 'gemini-flash38' ([pscustomobject]@{model='gemini-3.8-flash';provider='gemini';maxTokens=2048;contextWindowTokens=32768;temperature=0.2})
addp 'gemini-lite31' ([pscustomobject]@{model='gemini-3.1-flash-lite';provider='gemini';maxTokens=2048;contextWindowTokens=32768;temperature=0.2})
addp 'gemini-gemma26b' ([pscustomobject]@{model='gemma-4-26b-a4b-it';provider='gemini';maxTokens=2048;contextWindowTokens=32768;temperature=0.2})
[IO.File]::WriteAllText($p,($c|ConvertTo-Json -Depth 20),(New-Object Text.UTF8Encoding($false)))
"presets: " + (($c.modelPresets.PSObject.Properties.Name | ? { $_ -match 'gemini|or-' }) -join ',')
