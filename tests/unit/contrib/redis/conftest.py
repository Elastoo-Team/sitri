import pytest

from sitri.contrib.redis import RedisConfigProvider, RedisCredentialProvider

from .mock import RedisMock


@pytest.fixture(scope="module")
def redis_connection() -> RedisMock:
    return RedisMock()


@pytest.fixture(scope="module")
def redis_config(redis_connection) -> RedisConfigProvider:
    return RedisConfigProvider(prefix="test", redis_connection=redis_connection)


@pytest.fixture(scope="module")
def redis_credential(redis_connection) -> RedisCredentialProvider:
    return RedisCredentialProvider(prefix="test", redis_connection=redis_connection)
