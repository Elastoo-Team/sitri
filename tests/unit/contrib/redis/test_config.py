def test_metadata(redis_config) -> None:
    assert redis_config.provider_code == "redis"
    assert redis_config._project_prefix == "TEST"


def test_prefixize(redis_config) -> None:
    assert redis_config.prefixize("key1") == "TEST_KEY1"
    assert redis_config.unprefixize("TEST_KEY1") == "key1"


def test_get_variable(monkeypatch, redis_config) -> None:
    monkeypatch.setenv("TEST_KEY1", "1")
    monkeypatch.setenv("TEST_KEY2", "2")

    assert redis_config.get("key1") == "1"
    assert redis_config.get("key2") == "2"

    monkeypatch.undo()


def test_get_variables_list(monkeypatch, redis_config) -> None:
    monkeypatch.setenv("TEST_KEY1", "1")
    monkeypatch.setenv("TEST_KEY2", "2")

    monkeypatch.setenv("TEZT_T1", "1")
    monkeypatch.setenv("TEZT_T2", "2")

    assert "key1" in redis_config.keys()
    assert "key2" in redis_config.keys()
    assert "t1" not in redis_config.keys()
    assert "t2" not in redis_config.keys()

    monkeypatch.undo()
