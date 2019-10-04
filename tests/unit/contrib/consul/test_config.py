def test_metadata(consul_config) -> None:
    assert consul_config.provider_code == "consul"
    assert consul_config.folder == "test/"


def test_get_variable(monkeypatch, consul_config) -> None:
    consul_config._consul._env["test/key1"] = "1"
    consul_config._consul._env["test/key2"] = "2"

    assert consul_config.get_variable("key1") == "1"
    assert consul_config.get_variable("key2") == "2"


def test_get_variables_list(monkeypatch, consul_config) -> None:
    consul_config._consul._env["test/key1"] = "1"
    consul_config._consul._env["test/key2"] = "2"

    consul_config._consul._env["tezt/key1"] = "1"
    consul_config._consul._env["tezt/key2"] = "2"

    assert "test/key1" in consul_config.get_variables_list()
    assert "test/key2" in consul_config.get_variables_list()
    assert "tezt/key1" not in consul_config.get_variables_list()
    assert "tezt/key2" not in consul_config.get_variables_list()

    monkeypatch.undo()
