# AUDIT — append-only factory event log (latest 400)

| seq | time | job | bot | event | actor | detail |
|---|---|---|---|---|---|---|
| 684 | 2026-09-22 21:24:53 | 615d5d9f |  | lane.rejected | fast-LAPTOP-LRE6PSA8 | {"model": "liquid/lfm-2.5-2.6b:free", "reason": "probe quota: {\"error\":{\"message\":\"rate limit exceeded: free-models-per-day. add 10 cre |
| 685 | 2026-09-22 21:24:53 | 615d5d9f |  | lane.rejected | fast-LAPTOP-LRE6PSA8 | {"model": "nvidia/nemotron-3.5-lightning:free", "reason": "probe quota: {\"error\":{\"message\":\"rate limit exceeded: free-models-per-day.  |
| 686 | 2026-09-22 21:24:53 | 615d5d9f |  | lane.rejected | fast-LAPTOP-LRE6PSA8 | {"model": "thinkingmachines/inkling-small:free", "reason": "probe auth: {\"error\":{\"message\":\"thinkingmachines/inkling-small:free is onl |
| 687 | 2026-09-22 21:24:53 | 615d5d9f |  | lane.rejected | fast-LAPTOP-LRE6PSA8 | {"model": "poolside/laguna-s-2.1:free", "reason": "probe quota: {\"error\":{\"message\":\"rate limit exceeded: free-models-per-day. add 10 c |
| 688 | 2026-09-22 21:24:53 | 615d5d9f |  | lane.rejected | fast-LAPTOP-LRE6PSA8 | {"model": "thinkingmachines/inkling:free", "reason": "probe auth: {\"error\":{\"message\":\"thinkingmachines/inkling:free is only available  |
| 689 | 2026-09-22 21:24:53 | 615d5d9f |  | lane.rejected | fast-LAPTOP-LRE6PSA8 | {"model": "poolside/laguna-xs-2.1:free", "reason": "probe quota: {\"error\":{\"message\":\"rate limit exceeded: free-models-per-day. add 10  |
| 690 | 2026-09-22 21:24:53 | 615d5d9f |  | lane.rejected | fast-LAPTOP-LRE6PSA8 | {"model": "cohere/north-mini-code:free", "reason": "probe quota: {\"error\":{\"message\":\"rate limit exceeded: free-models-per-day. add 10  |
| 691 | 2026-09-22 21:24:53 | 615d5d9f |  | lane.rejected | fast-LAPTOP-LRE6PSA8 | {"model": "nvidia/nemotron-3-ultra-550b-a55b:free", "reason": "probe quota: {\"error\":{\"message\":\"rate limit exceeded: free-models-per-d |
| 692 | 2026-09-22 21:24:53 | 615d5d9f |  | lane.rejected | fast-LAPTOP-LRE6PSA8 | {"model": "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free", "reason": "probe quota: {\"error\":{\"message\":\"rate limit exceeded: free- |
| 693 | 2026-09-22 21:24:53 | 615d5d9f |  | lane.rejected | fast-LAPTOP-LRE6PSA8 | {"model": "google/gemma-4-26b-a4b-it:free", "reason": "probe quota: {\"error\":{\"message\":\"rate limit exceeded: free-models-per-day. add  |
| 694 | 2026-09-22 21:24:53 | 615d5d9f |  | lane.rejected | fast-LAPTOP-LRE6PSA8 | {"model": "google/gemma-4-31b-it:free", "reason": "probe quota: {\"error\":{\"message\":\"rate limit exceeded: free-models-per-day. add 10 c |
| 695 | 2026-09-22 21:24:53 | 615d5d9f |  | lane.rejected | fast-LAPTOP-LRE6PSA8 | {"model": "nvidia/nemotron-3-super-120b-a12b:free", "reason": "probe quota: {\"error\":{\"message\":\"rate limit exceeded: free-models-per-d |
| 696 | 2026-09-22 21:24:53 | 615d5d9f |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 697 | 2026-09-22 21:32:00 |  |  | worker.restart | fast-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 698 | 2026-09-22 21:34:28 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["79 passed in 10.12s"]} |
| 699 | 2026-09-22 21:34:28 |  |  | worker.selftest | svc-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["79 passed in 10.14s"]} |
| 700 | 2026-09-22 21:34:28 | 349607da | 004 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 701 | 2026-09-22 21:40:06 |  |  | worker.restart | svc-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 702 | 2026-09-22 21:40:06 |  |  | worker.restart | fast-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 703 | 2026-09-22 21:40:17 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["81 passed in 9.14s"]} |
| 704 | 2026-09-22 21:40:20 |  |  | worker.selftest | svc-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["81 passed in 8.60s"]} |
| 705 | 2026-09-22 21:43:27 | 60e46601 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 706 | 2026-09-22 21:43:27 | 51e8edf3 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-22T22"}} |
| 707 | 2026-09-22 21:43:27 | 60e46601 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 708 | 2026-09-22 21:53:22 | 349607da | 004 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": "4/4", "rejected": null}], "boundary_ |
| 709 | 2026-09-22 21:53:22 | 349607da | 004 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 710 | 2026-09-22 21:53:22 | 349607da | 004 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "004", "name": "changelog-writer", "status": "active", "verified": "VERIFIED"}} |
| 711 | 2026-09-22 21:53:25 |  |  | worker.restart | svc-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 712 | 2026-09-22 21:53:27 |  |  | worker.restart | svc-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 713 | 2026-09-22 21:53:29 |  |  | worker.restart | fast-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 714 | 2026-09-22 21:53:40 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["82 passed in 9.83s"]} |
| 715 | 2026-09-22 21:53:40 |  |  | worker.selftest | svc-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["82 passed in 10.35s"]} |
| 716 | 2026-09-22 21:55:42 | 135e45ff |  | job.enqueued | master-001 | {"kind": "create", "payload": {"objective": "reads a text file and counts how many lines contain a valid email address, replying with only t |
| 717 | 2026-09-22 21:55:45 | 135e45ff |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 718 | 2026-09-22 21:55:47 | 135e45ff | 021 | bot.created | svc-LAPTOP-LRE6PSA8 | {"name": "email-line-counter", "tools": ["read_file", "write_file"], "permissions": ["fs:read", "fs:write"], "chain": ["groq-gptoss120b", "o |
| 719 | 2026-09-22 21:59:57 | 135e45ff | 021 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 52s [done] expect='X_OK' last='X_OK' \| T2 PASS 72s [done] expect='2' last='RESULT: 2' \| T3 PASS 68s [done] expect='1'  |
| 720 | 2026-09-22 21:59:57 | 135e45ff | 021 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "021", "name": "email-line-counter", "pass": 4, "total": 4, "status": "active", "verified": "VERIFIED"}} |
| 721 | 2026-09-22 22:00:00 |  |  | worker.restart | fast-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 722 | 2026-09-22 22:00:01 |  |  | worker.restart | svc-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 723 | 2026-09-22 22:00:11 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["83 passed in 9.26s"]} |
| 724 | 2026-09-22 22:00:15 |  |  | worker.selftest | svc-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["83 passed in 8.98s"]} |
| 725 | 2026-09-22 22:11:16 |  |  | worker.restart | fast-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 726 | 2026-09-22 22:11:20 |  |  | worker.restart | svc-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 727 | 2026-09-22 22:11:27 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["84 passed in 8.91s"]} |
| 728 | 2026-09-22 22:11:33 |  |  | worker.selftest | svc-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["84 passed in 8.20s"]} |
| 729 | 2026-09-22 22:12:59 | f462fb6b |  | job.dedup | builder | {"kind": "probe"} |
| 730 | 2026-09-22 22:13:25 | f462fb6b |  | job.resumed | builder | {} |
| 731 | 2026-09-22 22:13:27 | f462fb6b |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 732 | 2026-09-22 22:13:27 | c367ebb5 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-22T23"}} |
| 733 | 2026-09-22 22:13:39 | f462fb6b |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash36", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qwe |
| 734 | 2026-09-22 22:19:48 |  |  | worker.restart | svc-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 735 | 2026-09-22 22:19:50 |  |  | worker.restart | fast-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 736 | 2026-09-22 22:20:01 |  |  | worker.selftest | svc-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["84 passed in 8.54s"]} |
| 737 | 2026-09-22 22:20:01 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["84 passed in 9.77s"]} |
| 738 | 2026-09-22 22:34:26 |  |  | worker.restart | svc-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 739 | 2026-09-22 22:34:27 |  |  | worker.restart | fast-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 740 | 2026-09-22 22:34:37 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["85 passed in 9.20s"]} |
| 741 | 2026-09-22 22:34:39 |  |  | worker.selftest | svc-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["85 passed in 8.31s"]} |
| 742 | 2026-09-22 22:35:09 |  |  | worker.restart | svc-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 743 | 2026-09-22 22:35:12 |  |  | worker.restart | fast-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 744 | 2026-09-22 22:35:24 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["85 passed in 10.08s"]} |
| 745 | 2026-09-22 22:35:24 |  |  | worker.selftest | svc-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["85 passed in 10.28s"]} |
| 746 | 2026-09-22 22:42:14 |  |  | worker.restart | fast-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 747 | 2026-09-22 22:42:14 |  |  | worker.restart | svc-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 748 | 2026-09-22 22:42:25 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["86 passed in 9.02s"]} |
| 749 | 2026-09-22 22:42:27 |  |  | worker.selftest | svc-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["86 passed in 8.76s"]} |
| 750 | 2026-09-22 22:43:27 | 51e8edf3 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 751 | 2026-09-22 22:43:27 | 5230a652 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-22T23"}} |
| 752 | 2026-09-22 22:43:27 | 51e8edf3 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 753 | 2026-09-22 22:44:55 |  |  | worker.restart | fast-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 754 | 2026-09-22 22:44:56 |  |  | worker.restart | svc-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 755 | 2026-09-22 22:45:06 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["87 passed in 9.73s"]} |
| 756 | 2026-09-22 22:45:10 |  |  | worker.selftest | svc-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["87 passed in 9.47s"]} |
| 757 | 2026-09-22 22:55:12 |  |  | worker.restart | fast-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 758 | 2026-09-22 22:55:16 |  |  | worker.restart | svc-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 759 | 2026-09-22 22:55:23 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["88 passed in 9.80s"]} |
| 760 | 2026-09-22 22:55:29 |  |  | worker.selftest | svc-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["88 passed in 8.78s"]} |
| 761 | 2026-09-22 22:59:58 | 197bb3e5 |  | job.enqueued | master-001 | {"kind": "plan", "payload": {"objective": "Create a pipeline: first bot reads a CSV of orders and writes only rows where status is refunded  |
| 762 | 2026-09-22 22:59:59 | 197bb3e5 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 763 | 2026-09-22 23:00:00 | 1e546b89 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "create", "payload": {"objective": "Read orders.csv, filter rows where the 'status' column is 'refunded', and write the resulting r |
| 764 | 2026-09-22 23:00:00 | 1a129f56 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "create", "payload": {"objective": "Read refunded.csv, sum the values in the 'amount' column, and write a single line to summary.tx |
| 765 | 2026-09-22 23:00:00 | 197bb3e5 |  | plan.made | svc-LAPTOP-LRE6PSA8 | {"lane": "groq:qwen/qwen3.8-27b", "steps": 2, "queued": [[1, "1e546b89"], [2, "1a129f56"]], "rationale": "The objective explicitly defines a |
| 766 | 2026-09-22 23:00:00 | 197bb3e5 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"name": "plan:2 steps", "status": "queued 1e546b89,1a129f56"}} |
| 767 | 2026-09-22 23:00:04 | 1e546b89 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 768 | 2026-09-22 23:00:06 | 1e546b89 | 022 | bot.created | svc-LAPTOP-LRE6PSA8 | {"name": "csv-refund-filter", "tools": ["read_file", "write_file"], "permissions": ["fs:read", "fs:write"], "chain": ["or-ling-30-flash-vl", |
| 769 | 2026-09-22 23:04:43 | 1e546b89 | 022 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 28s [done] expect='X_OK' last='X_OK' \| T2 PASS 105s [done] expect='2' last='RESULT: 2' \| T3 PASS 95s [done] expect='2' |
| 770 | 2026-09-22 23:04:43 | 1e546b89 | 022 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "022", "name": "csv-refund-filter", "pass": 4, "total": 4, "status": "active", "verified": "VERIFIED"}} |
| 771 | 2026-09-22 23:04:47 | 1a129f56 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 772 | 2026-09-22 23:04:49 | 1a129f56 | 023 | bot.created | svc-LAPTOP-LRE6PSA8 | {"name": "refund-summarizer", "tools": ["read_file", "write_file"], "permissions": ["fs:read", "fs:write"], "chain": ["or-ling-30-flash-vl", |
| 773 | 2026-09-22 23:08:55 | 1a129f56 | 023 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] expect='X_OK' last='X_OK' \| T2 PASS 87s [done] expect='36.0' last='RESULT: 36.0' \| T3 PASS 82s [done] expec |
| 774 | 2026-09-22 23:08:55 | 1a129f56 | 023 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "023", "name": "refund-summarizer", "pass": 4, "total": 4, "status": "active", "verified": "VERIFIED"}} |
| 775 | 2026-09-22 23:09:19 | bb6439ae |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 776 | 2026-09-22 23:09:19 | 5aa3c5cd |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "report", "payload": {"day": "2026-09-23"}} |
| 777 | 2026-09-22 23:09:19 | 4004bf3d |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "bench", "payload": {"stale_only": true, "max": 2, "day": "2026-09-22"}} |
| 778 | 2026-09-22 23:09:19 | bb6439ae |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 779 | 2026-09-22 23:09:19 | 4004bf3d |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 780 | 2026-09-22 23:12:53 | 4004bf3d |  | lane.benchmarked | svc-LAPTOP-LRE6PSA8 | {"lane": "gemini-flash36", "result": "2/4", "quota": 0, "secs": 63} |
| 781 | 2026-09-22 23:12:53 | 4004bf3d |  | lane.benchmarked | svc-LAPTOP-LRE6PSA8 | {"lane": "gemini-lite31", "result": "4/4", "quota": 0, "secs": 73} |
| 782 | 2026-09-22 23:12:53 | 4004bf3d |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"benchmarked": [["gemini-flash36", "2/4"], ["gemini-lite31", "4/4"]]}} |
| 783 | 2026-09-22 23:13:27 | c367ebb5 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 784 | 2026-09-22 23:13:27 | 6349a92d |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-23T00"}} |
| 785 | 2026-09-22 23:13:47 | c367ebb5 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen2 |
| 786 | 2026-09-22 23:15:50 | fa0a4093 |  | job.enqueued | builder | {"kind": "run", "payload": {"plan": "197bb3e5", "in": "C:\\AI\\Factory\\workspace\\inbox\\orders1", "cap": 300, "t": 1790115350}} |
| 787 | 2026-09-22 23:15:51 | fa0a4093 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 788 | 2026-09-22 23:17:38 | fa0a4093 | 022 | bot.ran | fast-LAPTOP-LRE6PSA8 | {"plan": "197bb3e5", "step": 1, "ok": true, "produced": ["refunded.csv"], "missing": [], "secs": 52, "reply": "RESULT: refunded.csv", "chain |
| 789 | 2026-09-22 23:17:38 | fa0a4093 | 023 | bot.ran | fast-LAPTOP-LRE6PSA8 | {"plan": "197bb3e5", "step": 2, "ok": true, "produced": ["summary.txt"], "missing": [], "secs": 53, "reply": "RESULT: 39.5", "chain": "gemin |
| 790 | 2026-09-22 23:17:38 | fa0a4093 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"name": "run:plan 197bb3e5", "status": "ok orders.csv,refunded.csv,summary.txt"}} |
| 791 | 2026-09-22 23:24:17 |  |  | worker.restart | svc-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 792 | 2026-09-22 23:24:19 |  |  | worker.restart | fast-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 793 | 2026-09-22 23:24:31 |  |  | worker.selftest | svc-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["89 passed in 9.59s"]} |
| 794 | 2026-09-22 23:24:31 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["89 passed in 10.34s"]} |
| 795 | 2026-09-22 23:25:08 | bb3c746e |  | job.enqueued | builder | {"kind": "create", "payload": {"objective": "--objective"}} |
| 796 | 2026-09-22 23:25:11 | bb3c746e |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 797 | 2026-09-22 23:25:12 | bb3c746e |  | security.violation | svc-LAPTOP-LRE6PSA8 | {"error": "architect: objective needs permissions outside the allowance ['fs:read', 'fs:write', 'net:search', 'net:fetch']: The objective is |
| 798 | 2026-09-22 23:25:12 | bb3c746e |  | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "security", "next_state": "paused", "attempt": 1, "error": "security: architect: objective needs permissions outside the a |
| 799 | 2026-09-22 23:27:51 |  |  | worker.restart | svc-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 800 | 2026-09-22 23:27:51 |  |  | worker.restart | fast-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 801 | 2026-09-22 23:28:02 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["90 passed in 9.35s"]} |
| 802 | 2026-09-22 23:28:04 |  |  | worker.selftest | svc-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["90 passed in 8.71s"]} |
| 803 | 2026-09-22 23:28:37 | bb3c746e |  | job.cancelled | owner | {} |
| 804 | 2026-09-22 23:28:38 | 8216dd6e |  | job.enqueued | builder | {"kind": "create", "payload": {"objective": "Run pytest in the workspace and report how many tests passed"}} |
| 805 | 2026-09-22 23:28:39 | 8216dd6e |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 806 | 2026-09-22 23:28:41 | 8216dd6e |  | security.violation | svc-LAPTOP-LRE6PSA8 | {"error": "architect: objective needs permissions outside the allowance ['fs:read', 'fs:write', 'net:search', 'net:fetch']: shell:workspace  |
| 807 | 2026-09-22 23:28:41 | 8216dd6e |  | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "security", "next_state": "paused", "attempt": 1, "error": "security: architect: objective needs permissions outside the a |
| 808 | 2026-09-22 23:31:27 | 8216dd6e |  | job.cancelled | owner | {} |
| 809 | 2026-09-22 23:31:27 | c73bd54a |  | job.enqueued | owner | {"kind": "create", "payload": {"objective": "Given a Python test file test_x.py in the workspace, run it with 'python -m pytest -q test_x.py |
| 810 | 2026-09-22 23:31:31 | c73bd54a |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 811 | 2026-09-22 23:31:34 | c73bd54a | 024 | bot.created | svc-LAPTOP-LRE6PSA8 | {"name": "pytest-runner-bot", "tools": ["write_file", "read_file", "exec"], "permissions": ["fs:read", "fs:write", "shell:workspace"], "chai |
| 812 | 2026-09-22 23:32:19 | c73bd54a | 024 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] expect='X_OK' last='X_OK' \| T2 PASS 17s [done] expect='2' last='RESULT: 2' \| T3 PASS 17s [done] expect='CON |
| 813 | 2026-09-22 23:32:19 | c73bd54a | 024 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "024", "name": "pytest-runner-bot", "pass": 3, "total": 3, "status": "active", "verified": "VERIFIED"}} |
| 814 | 2026-09-22 23:40:19 |  |  | worker.restart | svc-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 815 | 2026-09-22 23:40:23 |  |  | worker.restart | fast-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 816 | 2026-09-22 23:40:33 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["91 passed in 8.90s"]} |
| 817 | 2026-09-22 23:40:33 |  |  | worker.selftest | svc-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["91 passed in 10.43s"]} |
| 818 | 2026-09-22 23:42:33 |  |  | worker.restart | fast-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 819 | 2026-09-22 23:42:33 |  |  | worker.restart | svc-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 820 | 2026-09-22 23:42:44 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["91 passed in 9.03s"]} |
| 821 | 2026-09-22 23:42:46 |  |  | worker.selftest | svc-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["91 passed in 8.77s"]} |
| 822 | 2026-09-22 23:43:29 | 5230a652 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 823 | 2026-09-22 23:43:29 | 4f65b755 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-23T00"}} |
| 824 | 2026-09-22 23:43:29 | 5230a652 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 825 | 2026-09-22 23:46:06 |  |  | worker.restart | svc-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 826 | 2026-09-22 23:46:10 |  |  | worker.restart | fast-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 827 | 2026-09-22 23:46:22 |  |  | worker.selftest | svc-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["92 passed in 11.14s"]} |
| 828 | 2026-09-22 23:46:22 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["92 passed in 10.72s"]} |
| 829 | 2026-09-22 23:46:52 | 593061c9 |  | job.enqueued | builder | {"kind": "plan", "payload": {"objective": "Pipeline: take orders.csv, keep only the rows whose status is refunded and write them to refunded |
| 830 | 2026-09-22 23:46:52 | 593061c9 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 831 | 2026-09-22 23:46:56 | 593061c9 | 022 | plan.reused | svc-LAPTOP-LRE6PSA8 | {"step": 1, "similarity": 0.7} |
| 832 | 2026-09-22 23:46:56 | 593061c9 | 023 | plan.reused | svc-LAPTOP-LRE6PSA8 | {"step": 2, "similarity": 0.78} |
| 833 | 2026-09-22 23:46:56 | 9d375361 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "create", "payload": {"objective": "Read summary.txt and write its content in uppercase to summary_upper.txt.", "plan": "593061c979 |
| 834 | 2026-09-22 23:46:56 | 593061c9 |  | plan.made | svc-LAPTOP-LRE6PSA8 | {"lane": "gemini:gemini-3.1-flash-lite", "steps": 3, "queued": [[3, "9d375361"]], "rationale": "The objective requires a three-step pipeline |
| 835 | 2026-09-22 23:46:56 | 593061c9 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"name": "plan:3 steps", "status": "queued 9d375361"}} |
| 836 | 2026-09-22 23:47:00 | 9d375361 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 837 | 2026-09-22 23:47:06 | 9d375361 | 025 | bot.created | svc-LAPTOP-LRE6PSA8 | {"name": "text-transformer", "tools": ["read_file", "write_file"], "permissions": ["fs:read", "fs:write"], "chain": ["gemini-lite31", "gemin |
| 838 | 2026-09-22 23:48:09 | 9d375361 | 025 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='LIVENESS_OK' last='LIVENESS_OK' \| T2 PASS 38s [done] expect='HELLO WORLD' last='RESULT: HELLO WORLD' |
| 839 | 2026-09-22 23:48:09 | 9d375361 | 025 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "025", "name": "text-transformer", "pass": 3, "total": 3, "status": "active", "verified": "VERIFIED"}} |
| 840 | 2026-09-22 23:52:51 | 40a753dd |  | job.enqueued | builder | {"kind": "run", "payload": {"plan": "593061c9", "in": "C:\\AI\\Factory\\workspace\\inbox\\orders1", "cap": 300, "t": 1790117571}} |
| 841 | 2026-09-22 23:52:53 | 40a753dd |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 842 | 2026-09-22 23:52:53 | 40a753dd |  | job.failed | fast-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "KeyError: 'bot_id'\n\\Factory\\repo\\tools\\factory_worker.py\",  |
| 843 | 2026-09-22 23:58:48 |  |  | worker.restart | svc-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 844 | 2026-09-22 23:58:49 |  |  | worker.restart | fast-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 845 | 2026-09-22 23:59:01 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["93 passed in 9.94s"]} |
| 846 | 2026-09-22 23:59:01 |  |  | worker.selftest | svc-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["93 passed in 8.76s"]} |
| 847 | 2026-09-22 23:59:31 | 40a753dd |  | job.resumed | builder | {} |
| 848 | 2026-09-22 23:59:31 | 40a753dd |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 849 | 2026-09-23 00:00:45 | 40a753dd | 022 | bot.ran | fast-LAPTOP-LRE6PSA8 | {"plan": "593061c9", "step": 1, "ok": true, "produced": ["refunded.csv"], "missing": [], "secs": 11, "reply": "RESULT: success", "chain": "g |
| 850 | 2026-09-23 00:00:45 | 40a753dd | 023 | bot.ran | fast-LAPTOP-LRE6PSA8 | {"plan": "593061c9", "step": 2, "ok": true, "produced": ["summary.txt"], "missing": [], "secs": 12, "reply": "RESULT: 39.5", "chain": "groq- |
| 851 | 2026-09-23 00:00:45 | 40a753dd | 025 | bot.ran | fast-LAPTOP-LRE6PSA8 | {"plan": "593061c9", "step": 3, "ok": true, "produced": ["summary_upper.txt"], "missing": [], "secs": 48, "reply": "RESULT: 39.5", "chain":  |
| 852 | 2026-09-23 00:00:45 | 40a753dd |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"name": "run:plan 593061c9", "status": "ok orders.csv,refunded.csv,summary.txt,summary_upper.txt"}} |
| 853 | 2026-09-23 00:46:16 | 6349a92d |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 854 | 2026-09-23 00:46:16 | 4f65b755 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 855 | 2026-09-23 00:46:17 | 0d9b9aaa |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-23T01"}} |
| 856 | 2026-09-23 00:46:17 | 4f65b755 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 857 | 2026-09-23 00:46:17 | 6320985a |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-23T01"}} |
| 858 | 2026-09-24 01:11:59 | 6349a92d |  | probe.network_down | svc-LAPTOP-LRE6PSA8 | {"detail": "all 13 remote lanes across 3 providers errored in one sweep -> local network outage, health untouched"} |
| 859 | 2026-09-24 01:11:59 | 499dd527 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-23T00-retry", "retry_of": "6349a92dea06417c9b6e323550875b4a"}} |
| 860 | 2026-09-24 01:11:59 | 6349a92d |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 861 | 2026-09-24 01:12:00 | 0d9b9aaa |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 862 | 2026-09-24 01:12:00 | 657a2134 | 018 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "run", "payload": {"bot_id": "018", "task": "Sum order totals per country into totals.csv", "in": "C:\\AI\\Factory\\workspace\\inbo |
| 863 | 2026-09-24 01:12:00 |  | 018 | schedule.fired | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "fire": "2026-09-23T07:00", "job": "657a2134"} |
| 864 | 2026-09-24 01:12:00 | 96a47019 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-24T02"}} |
| 865 | 2026-09-24 01:12:00 | 0d9b9aaa |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 866 | 2026-09-24 01:12:04 | 6320985a |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 867 | 2026-09-24 01:12:04 | ada8b925 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-24T02"}} |
| 868 | 2026-09-24 01:12:07 | 6320985a |  | probe.network_down | svc-LAPTOP-LRE6PSA8 | {"detail": "all 13 remote lanes across 3 providers errored in one sweep -> local network outage, health untouched"} |
| 869 | 2026-09-24 01:12:07 | bdee72b1 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-23T01-retry", "retry_of": "6320985aecca4449a53b8cc8acd81034"}} |
| 870 | 2026-09-24 01:12:07 | 6320985a |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 871 | 2026-09-24 01:12:07 | 657a2134 | 018 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 872 | 2026-09-24 01:12:10 | 5aa3c5cd |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 873 | 2026-09-24 01:12:10 | 0253aa82 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "report", "payload": {"day": "2026-09-25"}} |
| 874 | 2026-09-24 01:12:10 | c35f9462 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "bench", "payload": {"stale_only": true, "max": 2, "day": "2026-09-24"}} |
| 875 | 2026-09-24 01:12:10 | ec7ed624 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "monitor", "payload": {"only": null, "day": "2026-09-24"}} |
| 876 | 2026-09-24 01:12:10 | 5aa3c5cd |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 877 | 2026-09-24 01:12:16 | ec7ed624 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 878 | 2026-09-24 01:12:16 | 581618e9 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "ec7ed62485264d62b34fc744deeb0c6f", "day": "2026-09-24"}} |
| 879 | 2026-09-24 01:12:16 | c50593d5 | 002 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "002", "monitor_of": "ec7ed62485264d62b34fc744deeb0c6f", "day": "2026-09-24"}} |
| 880 | 2026-09-24 01:12:16 | 36a3539c | 003 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "003", "monitor_of": "ec7ed62485264d62b34fc744deeb0c6f", "day": "2026-09-24"}} |
| 881 | 2026-09-24 01:12:16 | 1eedd036 | 004 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "004", "monitor_of": "ec7ed62485264d62b34fc744deeb0c6f", "day": "2026-09-24"}} |
| 882 | 2026-09-24 01:12:16 | 192d34a1 | 005 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "005", "monitor_of": "ec7ed62485264d62b34fc744deeb0c6f", "day": "2026-09-24"}} |
| 883 | 2026-09-24 01:12:16 | 80275837 | 006 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "006", "monitor_of": "ec7ed62485264d62b34fc744deeb0c6f", "day": "2026-09-24"}} |
| 884 | 2026-09-24 01:12:17 | 902b8c56 | 007 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "007", "monitor_of": "ec7ed62485264d62b34fc744deeb0c6f", "day": "2026-09-24"}} |
| 885 | 2026-09-24 01:12:17 | 84f90993 | 008 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "008", "monitor_of": "ec7ed62485264d62b34fc744deeb0c6f", "day": "2026-09-24"}} |
| 886 | 2026-09-24 01:12:17 | d67880ac | 009 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "009", "monitor_of": "ec7ed62485264d62b34fc744deeb0c6f", "day": "2026-09-24"}} |
| 887 | 2026-09-24 01:12:17 | b31aa10e | 011 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "011", "monitor_of": "ec7ed62485264d62b34fc744deeb0c6f", "day": "2026-09-24"}} |
| 888 | 2026-09-24 01:12:17 | e6ebfe8c | 012 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "012", "monitor_of": "ec7ed62485264d62b34fc744deeb0c6f", "day": "2026-09-24"}} |
| 889 | 2026-09-24 01:12:17 | 7a134c31 | 013 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "013", "monitor_of": "ec7ed62485264d62b34fc744deeb0c6f", "day": "2026-09-24"}} |
| 890 | 2026-09-24 01:12:17 | 06b13d4d | 014 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "014", "monitor_of": "ec7ed62485264d62b34fc744deeb0c6f", "day": "2026-09-24"}} |
| 891 | 2026-09-24 01:12:17 | 6ea2de2b | 016 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "016", "monitor_of": "ec7ed62485264d62b34fc744deeb0c6f", "day": "2026-09-24"}} |
| 892 | 2026-09-24 01:12:17 | e155909a | 017 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "017", "monitor_of": "ec7ed62485264d62b34fc744deeb0c6f", "day": "2026-09-24"}} |
| 893 | 2026-09-24 01:12:17 | bedaa1af | 018 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "018", "monitor_of": "ec7ed62485264d62b34fc744deeb0c6f", "day": "2026-09-24"}} |
| 894 | 2026-09-24 01:12:17 | 482340ef | 019 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "019", "monitor_of": "ec7ed62485264d62b34fc744deeb0c6f", "day": "2026-09-24"}} |
| 895 | 2026-09-24 01:12:17 | e26da376 | 020 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "020", "monitor_of": "ec7ed62485264d62b34fc744deeb0c6f", "day": "2026-09-24"}} |
| 896 | 2026-09-24 01:12:17 | a6fa92d2 | 021 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "021", "monitor_of": "ec7ed62485264d62b34fc744deeb0c6f", "day": "2026-09-24"}} |
| 897 | 2026-09-24 01:12:18 | c8eb6c89 | 022 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "022", "monitor_of": "ec7ed62485264d62b34fc744deeb0c6f", "day": "2026-09-24"}} |
| 898 | 2026-09-24 01:12:18 | 820f7ef9 | 023 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "023", "monitor_of": "ec7ed62485264d62b34fc744deeb0c6f", "day": "2026-09-24"}} |
| 899 | 2026-09-24 01:12:18 | 87f2fbc2 | 024 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "024", "monitor_of": "ec7ed62485264d62b34fc744deeb0c6f", "day": "2026-09-24"}} |
| 900 | 2026-09-24 01:12:18 | c1c70d3e | 025 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "025", "monitor_of": "ec7ed62485264d62b34fc744deeb0c6f", "day": "2026-09-24"}} |
| 901 | 2026-09-24 01:12:18 | ec7ed624 |  | monitor.fanout | svc-LAPTOP-LRE6PSA8 | {"bots": ["001", "002", "003", "004", "005", "006", "007", "008", "009", "011", "012", "013", "014", "016", "017", "018", "019", "020", "021 |
| 902 | 2026-09-24 01:12:18 | ec7ed624 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 903 | 2026-09-24 01:12:20 | 581618e9 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 904 | 2026-09-24 01:12:23 | 657a2134 | 018 | bot.ran | fast-LAPTOP-LRE6PSA8 | {"ok": true, "produced": [], "secs": 8, "reply": "", "chain": "groq-gptoss120b"} |
| 905 | 2026-09-24 01:12:23 | 657a2134 | 018 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "018", "name": "run", "status": "ok "}} |
| 906 | 2026-09-24 01:12:29 | c50593d5 | 002 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 907 | 2026-09-24 01:12:45 | bc494d29 |  | job.enqueued | nightly-task | {"kind": "monitor", "payload": {"only": null, "day": "2026-09-24"}} |
| 908 | 2026-09-24 01:20:22 | c50593d5 | 002 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 230s [done] expect='SCOUT_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\002.json' \| T2 FAIL 240s [done] expect= |
| 909 | 2026-09-24 01:20:22 | c50593d5 | 002 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 230s [done] expect='SCOUT_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\002.json' \| T2 FAIL 240s [done] expect= |
| 910 | 2026-09-24 01:20:22 | c50593d5 | 002 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 911 | 2026-09-24 01:20:22 | c3c35810 | 002 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "002", "max_rounds": 2}} |
| 912 | 2026-09-24 01:20:22 | c50593d5 | 002 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "002", "status": "testing", "verified": "UNVERIFIED"}} |
| 913 | 2026-09-24 01:20:31 |  |  | worker.restart | fast-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 914 | 2026-09-24 01:20:46 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["96 passed in 12.76s"]} |
| 915 | 2026-09-24 01:20:46 | 36a3539c | 003 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 916 | 2026-09-24 01:23:03 | 36a3539c | 003 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='SMITH_OK' last='SMITH_OK' \| T2 PASS 60s [done] expect='233168' last='RESULT: 233168' \| T3 PASS 30s  |
| 917 | 2026-09-24 01:23:03 | 36a3539c | 003 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='SMITH_OK' last='SMITH_OK' \| T2 PASS 60s [done] expect='233168' last='RESULT: 233168' \| T3 PASS 30s  |
| 918 | 2026-09-24 01:23:03 | 36a3539c | 003 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "003", "status": "active", "verified": "VERIFIED"}} |
| 919 | 2026-09-24 01:23:11 |  |  | worker.restart | fast-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 920 | 2026-09-24 01:23:26 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["97 passed in 12.63s"]} |
| 921 | 2026-09-24 01:23:26 | 499dd527 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 922 | 2026-09-24 01:23:26 | ada8b925 |  | job.dedup | fast-LAPTOP-LRE6PSA8 | {"kind": "probe"} |
| 923 | 2026-09-24 01:23:43 | 499dd527 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "no_tool_call", "before": "VERIFIED", "after": "BLOCKED", "detail": null} |
| 924 | 2026-09-24 01:23:43 | 499dd527 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "or-ling-30-flash-vl", "outcome": "gone", "before": "VERIFIED", "after": "BLOCKED", "detail": "{\"error\":{\"message\":\"this mode |
| 925 | 2026-09-24 01:23:43 | bcb0ba61 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-09-24", "trigger": "blocked:gemini-flash36,or-ling-30-flash-vl"}} |
| 926 | 2026-09-24 01:23:43 | 26e7235d |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-09-24", "trigger": "blocked:gemini-flash36,or-ling-30-flash-vl"}} |
| 927 | 2026-09-24 01:23:43 | 39a61954 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-09-24", "trigger": "blocked:gemini-flash36,or-ling-30-flash-vl"}} |
| 928 | 2026-09-24 01:23:43 | 6a46a820 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-09-24", "trigger": "blocked:gemini-flash36,or-ling-30-flash-vl"}} |
| 929 | 2026-09-24 01:23:43 | 499dd527 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3b",  |
| 930 | 2026-09-24 01:23:51 | bdee72b1 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 931 | 2026-09-24 01:23:51 | ada8b925 |  | job.dedup | fast-LAPTOP-LRE6PSA8 | {"kind": "probe"} |
| 932 | 2026-09-24 01:24:07 | bdee72b1 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash38", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "[{\n  \"error\": {\n    \"code\": 503,\ |
| 933 | 2026-09-24 01:24:07 | e30126b8 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-09-24", "trigger": "blocked:gemini-flash38"}} |
| 934 | 2026-09-24 01:24:07 | 8b22fe5c |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-09-24", "trigger": "blocked:gemini-flash38"}} |
| 935 | 2026-09-24 01:24:07 | f800e68b |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-09-24", "trigger": "blocked:gemini-flash38"}} |
| 936 | 2026-09-24 01:24:07 | aa0b21ba |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-09-24", "trigger": "blocked:gemini-flash38"}} |
| 937 | 2026-09-24 01:24:07 | bdee72b1 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3b",  |
| 938 | 2026-09-24 01:24:13 | bcb0ba61 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 939 | 2026-09-24 01:24:24 | bcb0ba61 |  | lane.discovered | fast-LAPTOP-LRE6PSA8 | {"model": "inclusionai/ling-3.0-flash-sante:free", "reason": "probe 1.22s loop 3.94s", "provider": "openrouter"} |
| 940 | 2026-09-24 01:24:24 | bcb0ba61 |  | lane.discovered | fast-LAPTOP-LRE6PSA8 | {"model": "inclusionai/ling-3.0-flash-fin:free", "reason": "probe 1.71s loop 3.01s", "provider": "openrouter"} |
| 941 | 2026-09-24 01:24:24 | bcb0ba61 |  | config.presets | fast-LAPTOP-LRE6PSA8 | {"added": ["or-ling-30-flash-sante", "or-ling-30-flash-fin"]} |
| 942 | 2026-09-24 01:24:24 | ad7a13c3 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "bench", "payload": {"lanes": ["or-ling-30-flash-sante", "or-ling-30-flash-fin"], "day": "2026-09-24"}} |
| 943 | 2026-09-24 01:24:24 | bcb0ba61 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": ["or-ling-30-flash-sante", "or-ling-30-flash-fin"]}} |
| 944 | 2026-09-24 01:24:32 | 26e7235d |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 945 | 2026-09-24 01:24:32 | 26e7235d |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 946 | 2026-09-24 01:24:40 | 39a61954 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 947 | 2026-09-24 01:24:40 | 39a61954 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 948 | 2026-09-24 01:24:46 | 6a46a820 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 949 | 2026-09-24 01:24:46 | 6a46a820 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 950 | 2026-09-24 01:24:54 | e30126b8 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 951 | 2026-09-24 01:28:26 | 581618e9 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 239s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 241s [TIMEOUT] report expect='FACTORY' cmd=False \| T3 PASS  |
| 952 | 2026-09-24 01:28:26 | 581618e9 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 239s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 241s [TIMEOUT] report expect='FACTORY' cmd=False \| T3 PASS  |
| 953 | 2026-09-24 01:28:26 | 581618e9 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 954 | 2026-09-24 01:28:26 | 7b4d176b | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "ec7ed62485264d62b34fc744deeb0c6f", "retry_of": "581618e95bdc448cac249a3a9d2422f |
| 955 | 2026-09-24 01:28:26 | 581618e9 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 5, "total": 7, "status": "testing", "verified": "UNVERIFIED"}} |
| 956 | 2026-09-24 01:28:33 |  |  | worker.restart | svc-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 957 | 2026-09-24 01:28:38 | c3c35810 | 002 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 958 | 2026-09-24 01:28:39 | c3c35810 | 002 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": null, "rounds": [], "boundary_diff": {}} |
| 959 | 2026-09-24 01:28:39 | c3c35810 | 002 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: repair only runs on demoted bots (status=active)\nT |
| 960 | 2026-09-24 01:28:44 | 8b22fe5c |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 961 | 2026-09-24 01:28:44 | 8b22fe5c |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 962 | 2026-09-24 01:28:48 | f800e68b |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 963 | 2026-09-24 01:28:48 | f800e68b |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 964 | 2026-09-24 01:28:52 | aa0b21ba |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 965 | 2026-09-24 01:28:52 | aa0b21ba |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 966 | 2026-09-24 01:28:58 | bc494d29 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 967 | 2026-09-24 01:28:58 | c5a39c84 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "bc494d298add4d7a90181803429c5b8a", "day": "2026-09-24"}} |
| 968 | 2026-09-24 01:28:58 | 6ebf5d8b | 002 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "002", "monitor_of": "bc494d298add4d7a90181803429c5b8a", "day": "2026-09-24"}} |
| 969 | 2026-09-24 01:28:58 | c20c2407 | 003 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "003", "monitor_of": "bc494d298add4d7a90181803429c5b8a", "day": "2026-09-24"}} |
| 970 | 2026-09-24 01:28:58 | 7ee5ebb8 | 004 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "004", "monitor_of": "bc494d298add4d7a90181803429c5b8a", "day": "2026-09-24"}} |
| 971 | 2026-09-24 01:28:58 | 9ce55607 | 005 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "005", "monitor_of": "bc494d298add4d7a90181803429c5b8a", "day": "2026-09-24"}} |
| 972 | 2026-09-24 01:28:58 | 29002603 | 006 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "006", "monitor_of": "bc494d298add4d7a90181803429c5b8a", "day": "2026-09-24"}} |
| 973 | 2026-09-24 01:28:58 | ff6fe1b9 | 007 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "007", "monitor_of": "bc494d298add4d7a90181803429c5b8a", "day": "2026-09-24"}} |
| 974 | 2026-09-24 01:28:58 | 1ddf7b9f | 008 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "008", "monitor_of": "bc494d298add4d7a90181803429c5b8a", "day": "2026-09-24"}} |
| 975 | 2026-09-24 01:28:58 | ab3a25c4 | 009 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "009", "monitor_of": "bc494d298add4d7a90181803429c5b8a", "day": "2026-09-24"}} |
| 976 | 2026-09-24 01:28:58 | 8b60cad0 | 011 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "011", "monitor_of": "bc494d298add4d7a90181803429c5b8a", "day": "2026-09-24"}} |
| 977 | 2026-09-24 01:28:58 | 67703501 | 012 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "012", "monitor_of": "bc494d298add4d7a90181803429c5b8a", "day": "2026-09-24"}} |
| 978 | 2026-09-24 01:28:58 | 240be6ff | 013 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "013", "monitor_of": "bc494d298add4d7a90181803429c5b8a", "day": "2026-09-24"}} |
| 979 | 2026-09-24 01:28:58 | 356da82f | 014 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "014", "monitor_of": "bc494d298add4d7a90181803429c5b8a", "day": "2026-09-24"}} |
| 980 | 2026-09-24 01:28:58 | 34c93c2f | 016 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "016", "monitor_of": "bc494d298add4d7a90181803429c5b8a", "day": "2026-09-24"}} |
| 981 | 2026-09-24 01:28:58 | 8e9fd24a | 017 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "017", "monitor_of": "bc494d298add4d7a90181803429c5b8a", "day": "2026-09-24"}} |
| 982 | 2026-09-24 01:28:58 | 09de5024 | 018 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "018", "monitor_of": "bc494d298add4d7a90181803429c5b8a", "day": "2026-09-24"}} |
| 983 | 2026-09-24 01:28:58 | ca4a7aeb | 019 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "019", "monitor_of": "bc494d298add4d7a90181803429c5b8a", "day": "2026-09-24"}} |
| 984 | 2026-09-24 01:28:58 | a51e46b5 | 020 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "020", "monitor_of": "bc494d298add4d7a90181803429c5b8a", "day": "2026-09-24"}} |
| 985 | 2026-09-24 01:28:58 | 764e7481 | 021 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "021", "monitor_of": "bc494d298add4d7a90181803429c5b8a", "day": "2026-09-24"}} |
| 986 | 2026-09-24 01:28:58 | 58a57670 | 022 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "022", "monitor_of": "bc494d298add4d7a90181803429c5b8a", "day": "2026-09-24"}} |
| 987 | 2026-09-24 01:28:58 | 6a5c5393 | 023 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "023", "monitor_of": "bc494d298add4d7a90181803429c5b8a", "day": "2026-09-24"}} |
| 988 | 2026-09-24 01:28:58 | a735d64e | 024 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "024", "monitor_of": "bc494d298add4d7a90181803429c5b8a", "day": "2026-09-24"}} |
| 989 | 2026-09-24 01:28:58 | 356d0905 | 025 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "025", "monitor_of": "bc494d298add4d7a90181803429c5b8a", "day": "2026-09-24"}} |
| 990 | 2026-09-24 01:28:58 | bc494d29 |  | monitor.fanout | svc-LAPTOP-LRE6PSA8 | {"bots": ["001", "002", "003", "004", "005", "006", "007", "008", "009", "011", "012", "013", "014", "016", "017", "018", "019", "020", "021 |
| 991 | 2026-09-24 01:28:58 | bc494d29 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 992 | 2026-09-24 01:29:02 | ad7a13c3 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 993 | 2026-09-24 01:29:40 | e30126b8 |  | lane.rejected | fast-LAPTOP-LRE6PSA8 | {"model": "dots-studio/dots-3-note-preview:free", "reason": "probe error: URLError", "provider": "openrouter"} |
| 994 | 2026-09-24 01:29:40 | e30126b8 |  | lane.rejected | fast-LAPTOP-LRE6PSA8 | {"model": "liquid/lfm-2.5-2.6b:free", "reason": "loop: HTTP 429 {\"error\":{\"message\":\"Provider returned error\",\"code\":429,\"metadata\ |
| 995 | 2026-09-24 01:29:40 | e30126b8 |  | lane.discovered | fast-LAPTOP-LRE6PSA8 | {"model": "nvidia/nemotron-3.5-lightning:free", "reason": "probe 59.9s loop 171.02s", "provider": "openrouter"} |
| 996 | 2026-09-24 01:29:40 | e30126b8 |  | config.presets | fast-LAPTOP-LRE6PSA8 | {"added": ["or-nemotron-35-lightning"]} |
| 997 | 2026-09-24 01:29:40 | faef1fd6 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "bench", "payload": {"lanes": ["or-nemotron-35-lightning"], "day": "2026-09-24"}} |
| 998 | 2026-09-24 01:29:40 | e30126b8 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": ["or-nemotron-35-lightning"]}} |
| 999 | 2026-09-24 01:29:52 | 1eedd036 | 004 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1000 | 2026-09-24 01:31:46 | 1eedd036 | 004 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 22s [done] expect='CHANGELOG_OK' last='CHANGELOG_OK' \| T2 PASS 22s [done] expect='3' last='3' \| T3 PASS 51s [done] exp |
| 1001 | 2026-09-24 01:31:46 | 1eedd036 | 004 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 22s [done] expect='CHANGELOG_OK' last='CHANGELOG_OK' \| T2 PASS 22s [done] expect='3' last='3' \| T3 PASS 51s [done] exp |
| 1002 | 2026-09-24 01:31:46 | 1eedd036 | 004 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "004", "status": "active", "verified": "VERIFIED"}} |
| 1003 | 2026-09-24 01:31:56 | 192d34a1 | 005 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1004 | 2026-09-24 01:33:32 | ad7a13c3 |  | lane.benchmarked | svc-LAPTOP-LRE6PSA8 | {"lane": "or-ling-30-flash-sante", "result": "4/4", "quota": 0, "secs": 89} |
| 1005 | 2026-09-24 01:33:32 | ad7a13c3 |  | lane.benchmarked | svc-LAPTOP-LRE6PSA8 | {"lane": "or-ling-30-flash-fin", "result": "4/4", "quota": 0, "secs": 100} |
| 1006 | 2026-09-24 01:33:32 | ad7a13c3 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"benchmarked": [["or-ling-30-flash-sante", "4/4"], ["or-ling-30-flash-fin", "4/4"]]}} |
| 1007 | 2026-09-24 01:33:37 | faef1fd6 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1008 | 2026-09-24 01:34:30 | 192d34a1 | 005 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 48s [done] expect='1' last='RESULT: 1' \| T3 PASS 63s [done] expect='0'  |
| 1009 | 2026-09-24 01:34:30 | 192d34a1 | 005 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 48s [done] expect='1' last='RESULT: 1' \| T3 PASS 63s [done] expect='0'  |
| 1010 | 2026-09-24 01:34:30 | 192d34a1 | 005 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "005", "status": "active", "verified": "VERIFIED"}} |
| 1011 | 2026-09-24 01:34:38 | 80275837 | 006 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1012 | 2026-09-24 01:36:01 | 80275837 | 006 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 16s [done] expect='X_OK' last='X_OK' \| T2 PASS 24s [done] expect='2' last='2' \| T3 FAIL 25s [done] expect='0' last='ER |
| 1013 | 2026-09-24 01:36:01 | 80275837 | 006 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 16s [done] expect='X_OK' last='X_OK' \| T2 PASS 24s [done] expect='2' last='2' \| T3 FAIL 25s [done] expect='0' last='ER |
| 1014 | 2026-09-24 01:36:01 | 80275837 | 006 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 1015 | 2026-09-24 01:36:01 | 754d191f | 006 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "006", "max_rounds": 2}} |
| 1016 | 2026-09-24 01:36:01 | 80275837 | 006 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "006", "status": "testing", "verified": "UNVERIFIED"}} |
| 1017 | 2026-09-24 01:36:09 | 902b8c56 | 007 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1018 | 2026-09-24 01:37:37 | c3c35810 |  | job.cancelled | owner | {} |
| 1019 | 2026-09-24 01:37:56 | 902b8c56 | 007 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] expect='X_OK' last='X_OK' \| T2 PASS 36s [done] expect='2' last='2' \| T3 FAIL 42s [done] expect='0' last='\u |
| 1020 | 2026-09-24 01:37:56 | 902b8c56 | 007 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] expect='X_OK' last='X_OK' \| T2 PASS 36s [done] expect='2' last='2' \| T3 FAIL 42s [done] expect='0' last='\u |
| 1021 | 2026-09-24 01:37:56 | 902b8c56 | 007 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 1022 | 2026-09-24 01:37:56 | 000fb61b | 007 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "007", "max_rounds": 2}} |
| 1023 | 2026-09-24 01:37:56 | 902b8c56 | 007 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "007", "status": "testing", "verified": "UNVERIFIED"}} |
| 1024 | 2026-09-24 01:38:04 |  |  | worker.restart | fast-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 1025 | 2026-09-24 01:38:20 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["98 passed in 14.17s"]} |
| 1026 | 2026-09-24 01:38:20 | 84f90993 | 008 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1027 | 2026-09-24 01:38:44 | c5a39c84 | 001 | job.cancelled | builder | {"reason": "duplicate nightly sweep (D-101)"} |
| 1028 | 2026-09-24 01:38:44 | 6ebf5d8b | 002 | job.cancelled | builder | {"reason": "duplicate nightly sweep (D-101)"} |
| 1029 | 2026-09-24 01:38:44 | c20c2407 | 003 | job.cancelled | builder | {"reason": "duplicate nightly sweep (D-101)"} |
| 1030 | 2026-09-24 01:38:44 | 7ee5ebb8 | 004 | job.cancelled | builder | {"reason": "duplicate nightly sweep (D-101)"} |
| 1031 | 2026-09-24 01:38:44 | 9ce55607 | 005 | job.cancelled | builder | {"reason": "duplicate nightly sweep (D-101)"} |
| 1032 | 2026-09-24 01:38:44 | 29002603 | 006 | job.cancelled | builder | {"reason": "duplicate nightly sweep (D-101)"} |
| 1033 | 2026-09-24 01:38:44 | ff6fe1b9 | 007 | job.cancelled | builder | {"reason": "duplicate nightly sweep (D-101)"} |
| 1034 | 2026-09-24 01:38:44 | 1ddf7b9f | 008 | job.cancelled | builder | {"reason": "duplicate nightly sweep (D-101)"} |
| 1035 | 2026-09-24 01:38:44 | ab3a25c4 | 009 | job.cancelled | builder | {"reason": "duplicate nightly sweep (D-101)"} |
| 1036 | 2026-09-24 01:38:44 | 8b60cad0 | 011 | job.cancelled | builder | {"reason": "duplicate nightly sweep (D-101)"} |
| 1037 | 2026-09-24 01:38:44 | 67703501 | 012 | job.cancelled | builder | {"reason": "duplicate nightly sweep (D-101)"} |
| 1038 | 2026-09-24 01:38:44 | 240be6ff | 013 | job.cancelled | builder | {"reason": "duplicate nightly sweep (D-101)"} |
| 1039 | 2026-09-24 01:38:44 | 356da82f | 014 | job.cancelled | builder | {"reason": "duplicate nightly sweep (D-101)"} |
| 1040 | 2026-09-24 01:38:44 | 34c93c2f | 016 | job.cancelled | builder | {"reason": "duplicate nightly sweep (D-101)"} |
| 1041 | 2026-09-24 01:38:44 | 8e9fd24a | 017 | job.cancelled | builder | {"reason": "duplicate nightly sweep (D-101)"} |
| 1042 | 2026-09-24 01:38:44 | 09de5024 | 018 | job.cancelled | builder | {"reason": "duplicate nightly sweep (D-101)"} |
| 1043 | 2026-09-24 01:38:44 | ca4a7aeb | 019 | job.cancelled | builder | {"reason": "duplicate nightly sweep (D-101)"} |
| 1044 | 2026-09-24 01:38:44 | a51e46b5 | 020 | job.cancelled | builder | {"reason": "duplicate nightly sweep (D-101)"} |
| 1045 | 2026-09-24 01:38:44 | 764e7481 | 021 | job.cancelled | builder | {"reason": "duplicate nightly sweep (D-101)"} |
| 1046 | 2026-09-24 01:38:44 | 58a57670 | 022 | job.cancelled | builder | {"reason": "duplicate nightly sweep (D-101)"} |
| 1047 | 2026-09-24 01:38:44 | 6a5c5393 | 023 | job.cancelled | builder | {"reason": "duplicate nightly sweep (D-101)"} |
| 1048 | 2026-09-24 01:38:44 | a735d64e | 024 | job.cancelled | builder | {"reason": "duplicate nightly sweep (D-101)"} |
| 1049 | 2026-09-24 01:38:44 | 356d0905 | 025 | job.cancelled | builder | {"reason": "duplicate nightly sweep (D-101)"} |
| 1050 | 2026-09-24 01:39:31 | 84f90993 | 008 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 15s [done] expect='apple' last='RESULT: apple' \| T3 PASS 26s [done] exp |
| 1051 | 2026-09-24 01:39:31 | 84f90993 | 008 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 15s [done] expect='apple' last='RESULT: apple' \| T3 PASS 26s [done] exp |
| 1052 | 2026-09-24 01:39:31 | 84f90993 | 008 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "008", "status": "active", "verified": "VERIFIED"}} |
| 1053 | 2026-09-24 01:39:37 | d67880ac | 009 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1054 | 2026-09-24 01:41:40 | d67880ac | 009 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='RESULT: X_OK' \| T2 PASS 54s [done] expect='3' last='RESULT: 3' \| T3 PASS 43s [done] exp |
| 1055 | 2026-09-24 01:41:40 | d67880ac | 009 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='RESULT: X_OK' \| T2 PASS 54s [done] expect='3' last='RESULT: 3' \| T3 PASS 43s [done] exp |
| 1056 | 2026-09-24 01:41:40 | d67880ac | 009 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "009", "status": "active", "verified": "VERIFIED"}} |
| 1057 | 2026-09-24 01:41:48 |  |  | worker.restart | fast-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 1058 | 2026-09-24 01:41:51 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": false, "tail": ["."]} |
| 1059 | 2026-09-24 01:41:51 |  |  | worker.blocked_by_tests | fast-LAPTOP-LRE6PSA8 | {"reason": "core/tests red on current code; refusing to process jobs until code changes"} |
| 1060 | 2026-09-24 01:43:02 | faef1fd6 |  | lane.benchmarked | svc-LAPTOP-LRE6PSA8 | {"lane": "or-nemotron-35-lightning", "result": "2/4", "quota": 0, "secs": 564} |
| 1061 | 2026-09-24 01:43:03 | faef1fd6 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"benchmarked": [["or-nemotron-35-lightning", "2/4"]]}} |
| 1062 | 2026-09-24 01:43:07 |  |  | worker.restart | svc-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 1063 | 2026-09-24 01:43:25 |  |  | worker.selftest | svc-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["100 passed in 13.98s"]} |
| 1064 | 2026-09-24 01:43:25 | 754d191f | 006 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1065 | 2026-09-24 01:46:36 | 754d191f | 006 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": "4/4", "rejected": null}], "boundary_ |
| 1066 | 2026-09-24 01:46:36 | 754d191f | 006 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 1067 | 2026-09-24 01:46:36 | 754d191f | 006 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "006", "name": "json-to-markdown-table", "status": "active", "verified": "VERIFIED"}} |
| 1068 | 2026-09-24 01:46:42 | 000fb61b | 007 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1069 | 2026-09-24 01:51:44 | 000fb61b | 007 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 1070 | 2026-09-24 01:51:44 | 000fb61b | 007 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 1071 | 2026-09-24 01:51:44 | 000fb61b | 007 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "007", "status": "active"}} |
| 1072 | 2026-09-24 01:51:49 | b31aa10e | 011 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1073 | 2026-09-24 01:55:19 | b31aa10e | 011 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 81s [done] expect='2' last='2' \| T3 PASS 74s [done] expect='3' last='3' |
| 1074 | 2026-09-24 01:55:19 | b31aa10e | 011 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 81s [done] expect='2' last='2' \| T3 PASS 74s [done] expect='3' last='3' |
| 1075 | 2026-09-24 01:55:19 | b31aa10e | 011 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "011", "status": "active", "verified": "VERIFIED"}} |
| 1076 | 2026-09-24 01:55:23 |  |  | worker.restart | svc-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 1077 | 2026-09-24 01:55:44 |  |  | worker.selftest | svc-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["100 passed in 13.92s"]} |
| 1078 | 2026-09-24 01:55:44 | e6ebfe8c | 012 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1079 | 2026-09-24 01:55:44 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["100 passed in 14.24s"]} |
| 1080 | 2026-09-24 01:55:44 | 7a134c31 | 013 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1081 | 2026-09-24 01:58:20 | e6ebfe8c | 012 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 22s [done] expect='X_OK' last='X_OK' \| T2 PASS 47s [done] expect='60' last='RESULT: 60' \| T3 PASS 51s [done] expect='2 |
| 1082 | 2026-09-24 01:58:20 | e6ebfe8c | 012 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 22s [done] expect='X_OK' last='X_OK' \| T2 PASS 47s [done] expect='60' last='RESULT: 60' \| T3 PASS 51s [done] expect='2 |
| 1083 | 2026-09-24 01:58:20 | e6ebfe8c | 012 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "012", "status": "active", "verified": "VERIFIED"}} |
