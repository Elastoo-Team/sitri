from __future__ import annotations

import typing as t

import pytest

from sitri.providers.contrib.vedis import VedisConfigProvider

from .mock import VedisMock


@pytest.fixture(scope="module")
def vedis_connection() -> t.Callable[[], VedisMock]:
    """vedis_connection.

    :rtype: t.Callable
    """
    return lambda: VedisMock()


@pytest.fixture(scope="module")
def vedis_config(vedis_connection: t.Callable[[], VedisMock]) -> VedisConfigProvider:
    """vedis_config.

    :param vedis_connection:
    :rtype: VedisConfigProvider
    """
    return VedisConfigProvider(vedis_connector=vedis_connection, hash_name="test")
