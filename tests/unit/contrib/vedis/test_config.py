def test_metadata(vedis_config) -> None:
    assert vedis_config.provider_code == "vedis"
    assert vedis_config._project_prefix == "TEST"
    assert vedis_config._hash_name == "test"


def test_prefixize(vedis_config) -> None:
    assert vedis_config.prefixize("key1") == "TEST_KEY1"


def test_get_variable(monkeypatch, vedis_config) -> None:
    monkeypatch.setenv("TEST_KEY1", "1")
    monkeypatch.setenv("TEST_KEY2", "2")

    assert vedis_config.get("key1") == "1"
    assert vedis_config.get("key2") == "2"

    monkeypatch.undo()


def test_get_variables_list(monkeypatch, vedis_config) -> None:
    monkeypatch.setenv("TEST_KEY1", "1")
    monkeypatch.setenv("TEST_KEY2", "2")

    monkeypatch.setenv("TEZT_KEY1", "1")
    monkeypatch.setenv("TEZT_KEY2", "2")

    assert "TEST_KEY1" in vedis_config.keys()
    assert "TEST_KEY2" in vedis_config.keys()
    assert "TEZT_KEY1" not in vedis_config.keys()
    assert "TEZT_KEY2" not in vedis_config.keys()

    monkeypatch.undo()
