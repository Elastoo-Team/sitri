import typing

import pytest
from pydantic import BaseModel, Field

from sitri.providers.contrib.vault import VaultKVConfigProvider
from sitri.settings.contrib.vault import VaultKVSettings

from .mock import VaultClientMock


@pytest.fixture(scope="module")
def vault_connection() -> typing.Callable:
    return lambda: VaultClientMock()


@pytest.fixture(scope="module")
def vault_kv_config(vault_connection) -> VaultKVConfigProvider:
    return VaultKVConfigProvider(vault_connector=vault_connection, mount_point="test", secret_path="test")  # noqa


@pytest.fixture(scope="module")
def vault_kv_settings_empty(vault_kv_config):
    class TestSettings(VaultKVSettings):
        class Config(VaultKVSettings.VaultKVSettingsConfig):
            provider = vault_kv_config

    return TestSettings


@pytest.fixture(scope="module")
def vault_kv_settings():
    def wrapper(provider_instance):
        class TestSettings(VaultKVSettings):
            key1: str = Field(...)
            key2: str = Field(...)

            class Config(VaultKVSettings.VaultKVSettingsConfig):
                provider = provider_instance

        return TestSettings

    return wrapper


@pytest.fixture(scope="module")
def vault_kv_settings_vault_raise():
    def wrapper(provider_instance):
        class TestSettings(VaultKVSettings):
            key3: str = Field(...)

            class Config(VaultKVSettings.VaultKVSettingsConfig):
                provider = provider_instance

        return TestSettings

    return wrapper


@pytest.fixture(scope="module")
def vault_kv_settings_complex():
    def wrapper(provider_instance):
        class Key0Model(BaseModel):
            test: str = Field(...)

        class TestSettings(VaultKVSettings):
            key0: Key0Model = Field(...)

            class Config(VaultKVSettings.VaultKVSettingsConfig):
                provider = provider_instance

        return TestSettings

    return wrapper


@pytest.fixture(scope="module")
def vault_kv_settings_complex_raise():
    def wrapper(provider_instance):
        class Key4Model(BaseModel):
            test: str = Field(...)

        class TestSettings(VaultKVSettings):
            key4: Key4Model = Field(...)

            class Config(VaultKVSettings.VaultKVSettingsConfig):
                provider = provider_instance

        return TestSettings

    return wrapper


@pytest.fixture(scope="module")
def path_to_json() -> str:
    return "tests/unit/settings/vault_kv/data.json"


@pytest.fixture(scope="module")
def vault_kv_local_mode(path_to_json):
    def wrapper(provider_instance):
        class Key4Model(BaseModel):
            test: str = Field(...)

        class TestSettings(VaultKVSettings):
            key1: str = Field(...)
            key2: str = Field(...)
            key3: str = Field(...)
            key4: Key4Model = Field(...)

            class Config(VaultKVSettings.VaultKVSettingsConfig):
                provider = provider_instance

                local_mode = True
                local_provider_args = {"json_path": path_to_json}
                local_mode_path_prefix = "test"

        return TestSettings

    return wrapper
