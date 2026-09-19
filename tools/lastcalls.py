import sqlite3,sys
c=sqlite3.connect(r"C:\AI\Factory\llm_usage.sqlite3")
cols=[r[1] for r in c.execute("pragma table_info(llm_calls)")]
print("cols:",cols)
n=int(sys.argv[1]) if len(sys.argv)>1 else 10
for r in c.execute(f"select * from llm_calls where source!='dream' order by id desc limit {n}"):
    print(dict(zip(cols,r)))
