import typing

import pytest

from sitri.contrib.consul import ConsulConfigProvider

from .mock import ConsulMock


@pytest.fixture(scope="module")
def consul_connection() -> typing.Callable:
    return lambda: ConsulMock()


@pytest.fixture(scope="module")
def consul_config(consul_connection) -> ConsulConfigProvider:
    return ConsulConfigProvider(consul_connector=consul_connection, folder="test/")
