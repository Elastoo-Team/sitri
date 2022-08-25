from __future__ import annotations

import typing as t

import pytest
from pydantic import BaseModel, Field

from sitri.providers.contrib.yaml import YamlConfigProvider
from sitri.settings.contrib.yaml import YamlSettings

T = t.TypeVar("T", bound=YamlSettings)


@pytest.fixture(scope="module")
def path_to_yaml() -> str:
    """path_to_yaml.

    :rtype: str
    """
    return "tests/unit/settings/yaml/data.yaml"


@pytest.fixture(scope="module")
def yaml_config(path_to_yaml: str) -> YamlConfigProvider:
    """yaml_config.

    :param path_to_yaml:
    :rtype: YamlConfigProvider
    """
    return YamlConfigProvider(yaml_path=path_to_yaml)  # noqa


@pytest.fixture(scope="module")
def yaml_settings_empty(yaml_config: YamlConfigProvider) -> t.Type[T]:
    """yaml_settings_empty.

    :param yaml_config:
    """

    class TestSettings(YamlSettings):
        """TestSettings."""

        class Config(YamlSettings.YamlSettingsConfig):
            """Config."""

            provider = yaml_config

    return TestSettings


@pytest.fixture(scope="module")
def yaml_settings() -> t.Callable[[YamlConfigProvider], t.Type[T]]:
    """yaml_settings."""

    def wrapper(provider_instance: YamlConfigProvider) -> t.Type[T]:
        """wrapper.

        :param provider_instance:
        """

        class TestSettings(YamlSettings):
            """TestSettings."""

            key1: str = Field(...)
            key2: str = Field(...)
            key3: str = Field(...)

            class Config(YamlSettings.YamlSettingsConfig):
                """Config."""

                provider = provider_instance

        return TestSettings

    return wrapper


@pytest.fixture(scope="module")
def yaml_settings_raise() -> t.Callable[[YamlConfigProvider], t.Type[T]]:
    """yaml_settings_raise."""

    def wrapper(provider_instance: YamlConfigProvider) -> t.Type[T]:
        """wrapper.

        :param provider_instance:
        """

        class TestSettings(YamlSettings):
            """TestSettings."""

            key0: str = Field(...)

            class Config(YamlSettings.YamlSettingsConfig):
                """Config."""

                provider = provider_instance

        return TestSettings

    return wrapper


@pytest.fixture(scope="module")
def yaml_settings_complex() -> t.Callable[[YamlConfigProvider], t.Type[T]]:
    """yaml_settings_complex."""

    def wrapper(provider_instance: YamlConfigProvider) -> t.Type[T]:
        """wrapper.

        :param provider_instance:
        """

        class Key4Model(BaseModel):
            """Key4Model."""

            test_key4_field: str = Field(...)

        class TestSettings(YamlSettings):
            """TestSettings."""

            key4: Key4Model = Field(...)

            class Config(YamlSettings.YamlSettingsConfig):
                """Config."""

                provider = provider_instance

        TestSettings.update_forward_refs(Key4Model=Key4Model)

        return TestSettings

    return wrapper


@pytest.fixture(scope="module")
def yaml_settings_complex_raise() -> t.Callable[[YamlConfigProvider], t.Type[T]]:
    """yaml_settings_complex_raise."""

    def wrapper(provider_instance: YamlConfigProvider) -> t.Type[T]:
        """wrapper.

        :param provider_instance:
        """

        class Key5Model(BaseModel):
            """Key5Model."""

            test: str = Field(...)

        class TestSettings(YamlSettings):
            """TestSettings."""

            key5: Key5Model = Field(...)

            class Config(YamlSettings.YamlSettingsConfig):
                """Config."""

                provider = provider_instance

        TestSettings.update_forward_refs(Key5Model=Key5Model)

        return TestSettings

    return wrapper
