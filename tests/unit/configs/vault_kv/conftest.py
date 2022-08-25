from __future__ import annotations

import typing as t

import pytest

from sitri.providers.contrib.vault import VaultKVConfigProvider

from .mock import VaultClientMock


@pytest.fixture(scope="module")
def vault_connection() -> t.Callable[[], VaultClientMock]:
    """vault_connection.

    :rtype: t.Callable
    """
    return lambda: VaultClientMock()


@pytest.fixture(scope="module")
def vault_kv_config(vault_connection: t.Callable[[], VaultClientMock]) -> VaultKVConfigProvider:
    """vault_kv_config.

    :param vault_connection:
    :rtype: VaultKVConfigProvider
    """
    return VaultKVConfigProvider(vault_connector=vault_connection, mount_point="test", secret_path="test")  # noqa
