from __future__ import annotations

import typing as t

import pytest

from sitri.providers.contrib.redis import RedisConfigProvider

from .mock import RedisMock


@pytest.fixture(scope="module")
def redis_connection() -> t.Callable[[], RedisMock]:
    """redis_connection.

    :rtype: t.Callable
    """
    return lambda: RedisMock()


@pytest.fixture(scope="module")
def redis_config(redis_connection: t.Callable[[], RedisMock]) -> RedisConfigProvider:
    """redis_config.

    :param redis_connection:
    :rtype: RedisConfigProvider
    """
    return RedisConfigProvider(prefix="test", redis_connector=redis_connection)
