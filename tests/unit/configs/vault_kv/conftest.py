import typing

import pytest

from sitri.providers.contrib.vault import VaultKVConfigProvider

from .mock import VaultClientMock


@pytest.fixture(scope="module")
def vault_connection() -> typing.Callable:
    return lambda: VaultClientMock()


@pytest.fixture(scope="module")
def vault_kv_config(vault_connection) -> VaultKVConfigProvider:
    return VaultKVConfigProvider(vault_connector=vault_connection, mount_point="test", secret_path="test")  # noqa
