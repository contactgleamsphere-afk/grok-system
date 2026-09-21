import json, time, pathlib, sys
import pytest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from factory.jobs import JobStore, classify_failure
from factory.guard import assert_no_silent_expansion, SecurityViolation, diff_boundaries


def test_enqueue_dedups_and_claims_in_priority_order(tmp_path):
    s = JobStore(tmp_path / "j.sqlite3")
    a = s.enqueue("create", {"objective": "x"}, priority=5)
    b = s.enqueue("create", {"objective": "x"}, priority=5)          # duplicate while queued -> same job
    c = s.enqueue("repair", {"bot_id": "004"}, priority=1)
    assert a["id"] == b["id"] and s.summary() == {"queued": 2}
    first = s.claim("w1"); assert first["id"] == c["id"] and first["attempts"] == 1
    assert s.claim("w2")["id"] == a["id"]
    assert s.claim("w3") is None
    events = [r["event"] for r in s.audit_rows()]
    assert "job.dedup" in events and events.count("job.claimed") == 2


def test_lease_expiry_recovers_crashed_worker_without_duplicate(tmp_path):
    s = JobStore(tmp_path / "j.sqlite3")
    j = s.enqueue("test", {"bot_id": "002"}, max_attempts=3)
    s.claim("crashy", lease_s=1)                                      # worker dies here
    assert s.claim("other") is None                                    # still leased
    time.sleep(1.2)
    again = s.claim("other")                                           # lease expired -> re-claimed exactly once
    assert again and again["id"] == j["id"] and again["attempts"] == 2
    assert s.claim("third") is None
    assert "job.lease_expired" in [r["event"] for r in s.audit_rows()]


def test_failure_classification_and_retry_policy(tmp_path):
    s = JobStore(tmp_path / "j.sqlite3")
    assert classify_failure("HTTP 429 tokens per day") == "quota"
    assert classify_failure("frozen fields changed: ['permissions']") == "security"
    assert classify_failure("runner error: tunnel closed") == "transient"
    assert classify_failure("repair: chain did not return usable instructions") == "model"
    assert classify_failure("expected 3 got 5") == "logic"
    q = s.enqueue("repair", {"bot_id": "004"}, max_attempts=5); s.claim("w")
    j = s.fail(q["id"], "HTTP 429 rate limit", "w"); assert j["state"] == "queued" and j["not_before"] > time.time() + 100
    l = s.enqueue("repair", {"bot_id": "005"}); s.claim("w")
    j = s.fail(l["id"], "expected 3 got 5", "w"); assert j["state"] == "paused" and j["failure_class"] == "logic"
    sec = s.enqueue("repair", {"bot_id": "003"}); s.claim("w")
    j = s.fail(sec["id"], "security: silent boundary expansion", "w"); assert j["state"] == "paused" and j["failure_class"] == "security"
    assert s.resume(j["id"])["state"] == "queued"
    s.audit_export(tmp_path / "AUDIT.md"); assert "job.failed" in (tmp_path / "AUDIT.md").read_text()


def test_guard_blocks_silent_expansion_and_credentials():
    before = {"permissions": ["fs:read"], "tools": ["read_file"], "model_policy": {"primary": "a", "fallbacks": ["local4b"]},
              "env": {"AIFACTORY_DISABLED_TOOLS": "exec,write_file"}}
    same = json.loads(json.dumps(before))
    assert assert_no_silent_expansion(before, same) == {}
    with pytest.raises(SecurityViolation, match="shell_expanded|permissions_added"):
        assert_no_silent_expansion(before, {**before, "permissions": ["fs:read", "shell:workspace"]})
    with pytest.raises(SecurityViolation, match="network_expanded|permissions_added"):
        assert_no_silent_expansion(before, {**before, "permissions": ["fs:read", "net:fetch"]})
    with pytest.raises(SecurityViolation, match="tools_reenabled"):
        assert_no_silent_expansion(before, {**before, "env": {"AIFACTORY_DISABLED_TOOLS": "write_file"}})
    with pytest.raises(SecurityViolation, match="credential"):
        assert_no_silent_expansion(before, {**before, "notes": "key gsk_abc123"})
    d = diff_boundaries(before, {**before, "model_policy": {"primary": "b", "fallbacks": ["local4b"]}})
    assert "model_policy_changed" in d
    with pytest.raises(SecurityViolation):   # model policy change is not silent-allowed either through the worker path
        assert_no_silent_expansion(before, {**before, "permissions": ["fs:read", "fs:write"]})


def test_resolve_prefix(tmp_path):
    from factory.jobs import JobStore
    st = JobStore(tmp_path / "j.sqlite3")
    j = st.enqueue("test", {"bot_id": "001"})
    assert st.resolve(j["id"][:8]) == j["id"]
    import pytest
    with pytest.raises(KeyError): st.resolve("zzzzzzzz")
