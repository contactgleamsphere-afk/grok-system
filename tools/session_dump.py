import json,glob,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
fs=sorted(glob.glob(r"C:\AI\Factory\sessions\*\*.jsonl"),key=os.path.getmtime)[-1]
for line in open(fs,encoding="utf-8",errors="replace"):
    d=json.loads(line)
    if d.get("_type")=="metadata": print(json.dumps(d["metadata"].get("_last_usage"))[:300]); continue
    tc=d.get("tool_calls") or []
    print(d.get("role"), (d.get("content") or "")[:150].replace("\n"," "), "| CALL "+",".join(t["function"]["name"]+" "+t["function"]["arguments"][:80] for t in tc) if tc else "", "| lat",d.get("latency_ms"))
