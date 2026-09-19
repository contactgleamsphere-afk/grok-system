import os,json,urllib.request,time
exec(open(r"C:\AI\Factory\tools\lanes.py").read().split("g=os.environ")[0])
g=os.environ["GEMINI_API_KEY"]; o=os.environ["OPENROUTER_API_KEY"]
r=urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models?key={g}")
ms=[m["name"].split("/")[1] for m in json.load(urllib.request.urlopen(r,timeout=60))["models"] if "generateContent" in m.get("supportedGenerationMethods",[])]
print("gemini models:",[m for m in ms if "flash" in m or "lite" in m][:20])
for m in ["gemini-3.6-flash","gemini-3.5-flash-lite"]:
    for i in range(5):
        dt,d,err=post("https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",{"Authorization":f"Bearer {g}"},{"model":m,"messages":msgs,"tools":tools})
        tc=d and d["choices"][0]["message"].get("tool_calls")
        print(f"gemini {m:24s} run{i+1} {dt:4.1f}s tool_call={bool(tc)} {'' if not err else err[:220]}")
        if err: break
for m in ["qwen/qwen3.8-27b:free","google/gemma-4-26b-a4b-it:free","nex-agi/nex-n2.5-mini:free","deepseek/deepseek-v4-flash-0731:free"]:
    ok=0;ts=[]
    for i in range(5 if m.startswith("deepseek") else 2):
        dt,d,err=post("https://openrouter.ai/api/v1/chat/completions",{"Authorization":f"Bearer {o}"},{"model":m,"messages":msgs,"tools":tools})
        tc=d and d["choices"][0]["message"].get("tool_calls"); ok+=bool(tc); ts.append(round(dt,1))
        if err: print("  err",m,err[:160]); break
    print(f"openrouter {m:40s} ok={ok} times={ts}")
r=urllib.request.Request("https://openrouter.ai/api/v1/key",headers={"Authorization":f"Bearer {o}"}); print("or key:",json.load(urllib.request.urlopen(r))["data"])
