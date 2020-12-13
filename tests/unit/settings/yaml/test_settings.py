import pytest
from pydantic.env_settings import SettingsError
from pydantic.error_wrappers import ValidationError


def test_metadata(yaml_settings_empty) -> None:
    assert yaml_settings_empty.Config.provider.provider_code == "yaml"


def test_get_variable(
    monkeypatch,
    yaml_config,
    yaml_settings,
    yaml_settings_raise,
    yaml_settings_complex,
    yaml_settings_complex_raise,
) -> None:
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
