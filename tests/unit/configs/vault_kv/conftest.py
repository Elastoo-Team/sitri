import typing

import pytest

from sitri.providers.contrib.vault import VaultKVConfigProvider

from .mock import VaultClientMock


@pytest.fixture(scope="module")
def vault_connection() -> typing.Callable[[], VaultClientMock]:
    """vault_connection.

    :rtype: typing.Callable
    """
    return lambda: VaultClientMock()


@pytest.fixture(scope="module")
def vault_kv_config(vault_connection: typing.Callable[[], VaultClientMock]) -> VaultKVConfigProvider:
    """vault_kv_config.

    :param vault_connection:
    :rtype: VaultKVConfigProvider
    """
    return VaultKVConfigProvider(vault_connector=vault_connection, mount_point="test", secret_path="test")  # noqa
