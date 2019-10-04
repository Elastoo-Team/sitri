def test_metadata(system_config) -> None:
    assert system_config.provider_code == "system"
    assert system_config._project_prefix == "TEST"


def test_prefixize(system_config) -> None:
    assert system_config.prefixize("key1") == "TEST_KEY1"


def test_get_variable(monkeypatch, system_config) -> None:
    monkeypatch.setenv("TEST_KEY1", "1")
    monkeypatch.setenv("TEST_KEY2", "2")

    assert system_config.get_variable("key1") == "1"
    assert system_config.get_variable("key2") == "2"

    monkeypatch.undo()


def test_get_variables_list(monkeypatch, system_config) -> None:
    monkeypatch.setenv("TEST_KEY1", "1")
    monkeypatch.setenv("TEST_KEY2", "2")

    monkeypatch.setenv("TEZT_KEY1", "1")
    monkeypatch.setenv("TEZT_KEY2", "2")

    assert "TEST_KEY1" in system_config.get_variables_list()
    assert "TEST_KEY2" in system_config.get_variables_list()
    assert "TEZT_KEY1" not in system_config.get_variables_list()
    assert "TEZT_KEY2" not in system_config.get_variables_list()

    monkeypatch.undo()
