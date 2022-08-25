from __future__ import annotations

import typing

import pytest

from sitri.providers.contrib.redis import RedisConfigProvider

from .mock import RedisMock


@pytest.fixture(scope="module")
def redis_connection() -> typing.Callable[[], RedisMock]:
    """redis_connection.

    :rtype: typing.Callable
    """
    return lambda: RedisMock()


@pytest.fixture(scope="module")
def redis_config(redis_connection: typing.Callable[[], RedisMock]) -> RedisConfigProvider:
    """redis_config.

    :param redis_connection:
    :rtype: RedisConfigProvider
    """
    return RedisConfigProvider(prefix="test", redis_connector=redis_connection)
