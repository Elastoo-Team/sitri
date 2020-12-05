import typing

import pytest

from sitri.contrib.vedis import VedisConfigProvider

from .mock import VedisMock


@pytest.fixture(scope="module")
def vedis_connection() -> typing.Callable:
    return lambda: VedisMock()


@pytest.fixture(scope="module")
def vedis_config(vedis_connection) -> VedisConfigProvider:
    return VedisConfigProvider(vedis_connector=vedis_connection, hash_name="test")
