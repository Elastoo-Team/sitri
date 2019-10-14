import typing

import pytest

from sitri.contrib.redis import RedisConfigProvider, RedisCredentialProvider

from .mock import RedisMock


@pytest.fixture(scope="module")
def redis_connection() -> typing.Callable:
    return lambda: RedisMock()


@pytest.fixture(scope="module")
def redis_config(redis_connection) -> RedisConfigProvider:
    return RedisConfigProvider(prefix="test", redis_connector=redis_connection)


@pytest.fixture(scope="module")
def redis_credential(redis_connection) -> RedisCredentialProvider:
    return RedisCredentialProvider(prefix="test", redis_connector=redis_connection)
