from __future__ import annotations

import typing as t

import pytest
from pydantic.env_settings import SettingsError
from pydantic.error_wrappers import ValidationError

from sitri.providers.contrib.yaml import YamlConfigProvider
from sitri.settings.contrib.yaml import YamlSettings


def test_metadata(yaml_settings_empty: YamlSettings) -> None:
    """test_metadata.

    :param yaml_settings_empty:
    :rtype: None
    """
    assert yaml_settings_empty.Config.provider.provider_code == "yaml"


def test_get_variable(
    monkeypatch: t.Any,
    yaml_config: YamlConfigProvider,
    yaml_settings: t.Callable[[YamlConfigProvider], YamlSettings],
    yaml_settings_raise: t.Callable[[YamlConfigProvider], YamlSettings],
    yaml_settings_complex: t.Callable[[YamlConfigProvider], YamlSettings],
    yaml_settings_complex_raise: t.Callable[[YamlConfigProvider], YamlSettings],
) -> None:
    """test_get_variable.

    :param monkeypatch:
    :param yaml_config:
    :param yaml_settings:
    :param yaml_settings_raise:
    :param yaml_settings_complex:
    :param yaml_settings_complex_raise:
    :rtype: None
    """
    test_settings = yaml_settings(provider_instance=yaml_config)()

    assert test_settings.key1 == "1"
    assert test_settings.key2 == "2"
    assert test_settings.key3 == "3"

    test_settings_complex = yaml_settings_complex(provider_instance=yaml_config)()

    assert "test_key4_field" in test_settings_complex.key4.dict()
    assert test_settings_complex.key4.test_key4_field == "test"

    with pytest.raises(ValidationError):
        yaml_settings_raise(provider_instance=yaml_config)()

    with pytest.raises(SettingsError):
        yaml_settings_complex_raise(provider_instance=yaml_config)()
