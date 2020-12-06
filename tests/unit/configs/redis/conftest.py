import typing

import pytest

from sitri.providers.contrib.redis import RedisConfigProvider

from .mock import RedisMock


@pytest.fixture(scope="module")
def redis_connection() -> typing.Callable:
    return lambda: RedisMock()


@pytest.fixture(scope="module")
def redis_config(redis_connection) -> RedisConfigProvider:
    return RedisConfigProvider(prefix="test", redis_connector=redis_connection)
