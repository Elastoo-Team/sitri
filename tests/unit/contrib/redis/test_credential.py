def test_metadata(redis_credential) -> None:
    assert redis_credential.provider_code == "redis"
    assert redis_credential._project_prefix == "TEST"


def test_prefixize(redis_credential) -> None:
    assert redis_credential.prefixize("key1") == "TEST_KEY1"


def test_get_credential(monkeypatch, redis_credential) -> None:
    monkeypatch.setenv("TEST_KEY1", "1")
    monkeypatch.setenv("TEST_KEY2", "2")

    assert redis_credential.get("key1") == "1"
    assert redis_credential.get("key2") == "2"

    monkeypatch.undo()
