def test_metadata(vault_kv_config) -> None:
    assert vault_kv_config.provider_code == "vault_kv"
    assert vault_kv_config._mount_point == "test"
    assert vault_kv_config._secret_path == "test"


def test_get_variable(monkeypatch, vault_kv_config) -> None:
    vault_kv_config._vault._env.update({"test": {"test": {"data": {}}}})

    vault_kv_config._vault._env["test"]["test"]["data"]["key1"] = "1"
    vault_kv_config._vault._env["test"]["test"]["data"]["key2"] = "2"

    assert vault_kv_config.get("key1") == "1"
    assert vault_kv_config.get("key2") == "2"


def test_get_variables_list(monkeypatch, vault_kv_config) -> None:
    vault_kv_config._vault._env.update({"test": {"test": {"data": {}}}})

    vault_kv_config._vault._env["test"]["test"]["data"]["key1"] = "1"
    vault_kv_config._vault._env["test"]["test"]["data"]["key2"] = "2"

    assert "key1" in vault_kv_config.keys()
    assert "key2" in vault_kv_config.keys()
    assert "key3" not in vault_kv_config.keys()

    monkeypatch.undo()
