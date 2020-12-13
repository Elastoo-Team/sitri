import pytest
from pydantic import BaseModel, Field

from sitri.providers.contrib.yaml import YamlConfigProvider
from sitri.settings.contrib.yaml import YamlSettings


@pytest.fixture(scope="module")
def path_to_yaml() -> str:
    return "tests/unit/settings/yaml/data.yaml"


@pytest.fixture(scope="module")
def yaml_config(path_to_yaml) -> YamlConfigProvider:
    return YamlConfigProvider(yaml_path=path_to_yaml)  # noqa


@pytest.fixture(scope="module")
def yaml_settings_empty(yaml_config):
    class TestSettings(YamlSettings):
        class Config(YamlSettings.YamlSettingsConfig):
            provider = yaml_config

    return TestSettings


@pytest.fixture(scope="module")
def yaml_settings():
    def wrapper(provider_instance):
        class TestSettings(YamlSettings):
            key1: str = Field(...)
            key2: str = Field(...)
            key3: str = Field(...)

            class Config(YamlSettings.YamlSettingsConfig):
                provider = provider_instance

        return TestSettings

    return wrapper


@pytest.fixture(scope="module")
def yaml_settings_raise():
    def wrapper(provider_instance):
        class TestSettings(YamlSettings):
            key0: str = Field(...)

            class Config(YamlSettings.YamlSettingsConfig):
                provider = provider_instance

        return TestSettings

    return wrapper


@pytest.fixture(scope="module")
def yaml_settings_complex():
    def wrapper(provider_instance):
        class Key4Model(BaseModel):
            test_key4_field: str = Field(...)

        class TestSettings(YamlSettings):
            key4: Key4Model = Field(...)

            class Config(YamlSettings.YamlSettingsConfig):
                provider = provider_instance

        return TestSettings

    return wrapper


@pytest.fixture(scope="module")
def yaml_settings_complex_raise():
    def wrapper(provider_instance):
        class Key5Model(BaseModel):
            test: str = Field(...)

        class TestSettings(YamlSettings):
            key5: Key5Model = Field(...)

            class Config(YamlSettings.YamlSettingsConfig):
                provider = provider_instance

        return TestSettings

    return wrapper
