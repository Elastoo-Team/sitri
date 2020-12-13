import pytest
from pydantic.env_settings import SettingsError
from pydantic.error_wrappers import ValidationError


def test_metadata(vault_kv_settings_empty) -> None:
    assert vault_kv_settings_empty.Config.provider.provider_code == "vault_kv"


def test_get_variable(
    monkeypatch,
    vault_kv_config,
    vault_kv_settings,
    vault_kv_settings_vault_raise,
    vault_kv_settings_complex_raise,
    vault_kv_settings_complex,
) -> None:
    vault_kv_config._vault._env.update({"test": {"test": {"data": {}}}})

    vault_kv_config._vault._env["test"]["test"]["data"]["key1"] = "1"
    vault_kv_config._vault._env["test"]["test"]["data"]["key2"] = "2"
    vault_kv_config._vault._env["test"]["test"]["data"]["key4"] = r'{"test" "test"}'
    vault_kv_config._vault._env["test"]["test"]["data"]["key0"] = r'{"test": "test"}'

    test_settings = vault_kv_settings(provider_instance=vault_kv_config)()
    assert test_settings.key1 == "1"
    assert test_settings.key2 == "2"

    test_settings_complex = vault_kv_settings_complex(provider_instance=vault_kv_config)()
    assert test_settings_complex.key0 == test_settings_complex.__config__.json_loads(
        vault_kv_config._vault._env["test"]["test"]["data"]["key0"]
    )

    with pytest.raises(ValidationError):
        vault_kv_settings_vault_raise(provider_instance=vault_kv_config)()

    with pytest.raises(SettingsError):
        vault_kv_settings_complex_raise(provider_instance=vault_kv_config)()


def test_get_variable_local_mode(vault_kv_config, vault_kv_local_mode):
    test_settings = vault_kv_local_mode(provider_instance=vault_kv_config)()

    assert test_settings.key1 == "1"
    assert test_settings.key2 == "2"
    assert test_settings.key3 == "3"

    assert "test" in test_settings.key4.dict()
    assert test_settings.key4.test == "test"
