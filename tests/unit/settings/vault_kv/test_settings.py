from __future__ import annotations

import typing as t

import pytest
from pydantic.env_settings import SettingsError
from pydantic.error_wrappers import ValidationError

from sitri.providers.contrib.vault import VaultKVConfigProvider
from sitri.settings.contrib.vault import VaultKVSettings


def test_metadata(vault_kv_settings_empty: VaultKVSettings) -> None:
    """test_metadata.

    :param vault_kv_settings_empty:
    :rtype: None
    """
    assert vault_kv_settings_empty.Config.provider.provider_code == "vault_kv"


def test_get_variable(
    monkeypatch: t.Any,
    vault_kv_config: VaultKVConfigProvider,
    vault_kv_settings: t.Callable[[VaultKVConfigProvider], VaultKVSettings],
    vault_kv_settings_vault_raise: t.Callable[[VaultKVConfigProvider], VaultKVSettings],
    vault_kv_settings_complex_raise: t.Callable[[VaultKVConfigProvider], VaultKVSettings],
    vault_kv_settings_complex: t.Callable[[VaultKVConfigProvider], VaultKVSettings],
) -> None:
    """test_get_variable.

    :param monkeypatch:
    :param vault_kv_config:
    :param vault_kv_settings:
    :param vault_kv_settings_vault_raise:
    :param vault_kv_settings_complex_raise:
    :param vault_kv_settings_complex:
    :rtype: None
    """
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
        vault_kv_config._vault._env["test"]["test"]["data"]["key0"],
    )

    with pytest.raises(ValidationError):
        vault_kv_settings_vault_raise(provider_instance=vault_kv_config)()

    with pytest.raises(SettingsError):
        vault_kv_settings_complex_raise(provider_instance=vault_kv_config)()


def test_get_variable_local_mode(
    vault_kv_config: VaultKVConfigProvider,
    vault_kv_local_mode: t.Callable[[VaultKVConfigProvider], VaultKVSettings],
) -> None:
    """test_get_variable_local_mode.

    :param vault_kv_config:
    :param vault_kv_local_mode:
    """
    test_settings = vault_kv_local_mode(provider_instance=vault_kv_config)()

    assert test_settings.key1 == "1"
    assert test_settings.key2 == "2"
    assert test_settings.key3 == "3"

    assert "test" in test_settings.key4.dict()
    assert test_settings.key4.test == "test"
