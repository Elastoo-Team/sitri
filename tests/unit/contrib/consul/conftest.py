import pytest

from sitri.contrib.consul import ConsulConfigProvider

from .mock import ConsulMock


@pytest.fixture(scope="module")
def consul_connection() -> ConsulMock:
    return ConsulMock()


@pytest.fixture(scope="module")
def consul_config(consul_connection) -> ConsulConfigProvider:
    return ConsulConfigProvider(consul_connection=consul_connection, folder="test/")
