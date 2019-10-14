import typing

import pytest

from sitri.contrib.vedis import VedisConfigProvider, VedisCredentialProvider

from .mock import VedisMock


@pytest.fixture(scope="module")
def vedis_connection() -> typing.Callable:
    return lambda: VedisMock()


@pytest.fixture(scope="module")
def vedis_config(vedis_connection) -> VedisConfigProvider:
    return VedisConfigProvider(vedis_connector=vedis_connection, hash_name="test")


@pytest.fixture(scope="module")
def vedis_credential(vedis_connection) -> VedisCredentialProvider:
    return VedisCredentialProvider(vedis_connector=vedis_connection, hash_name="test")
