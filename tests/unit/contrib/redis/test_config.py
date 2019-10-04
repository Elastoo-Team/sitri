def test_metadata(redis_config) -> None:
    assert redis_config.provider_code == "redis"
    assert redis_config._project_prefix == "TEST"


def test_prefixize(redis_config) -> None:
    assert redis_config.prefixize("key1") == "TEST_KEY1"


def test_get_variable(monkeypatch, redis_config) -> None:
    monkeypatch.setenv("TEST_KEY1", "1")
    monkeypatch.setenv("TEST_KEY2", "2")

    assert redis_config.get_variable("key1") == "1"
    assert redis_config.get_variable("key2") == "2"

    monkeypatch.undo()


def test_get_variables_list(monkeypatch, redis_config) -> None:
    monkeypatch.setenv("TEST_KEY1", "1")
    monkeypatch.setenv("TEST_KEY2", "2")

    monkeypatch.setenv("TEZT_KEY1", "1")
    monkeypatch.setenv("TEZT_KEY2", "2")

    assert "TEST_KEY1" in redis_config.get_variables_list()
    assert "TEST_KEY2" in redis_config.get_variables_list()
    assert "TEZT_KEY1" not in redis_config.get_variables_list()
    assert "TEZT_KEY2" not in redis_config.get_variables_list()

    monkeypatch.undo()
