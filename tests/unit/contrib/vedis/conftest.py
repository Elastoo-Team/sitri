import pytest

from sitri.contrib.vedis import VedisConfigProvider, VedisCredentialProvider

from .mock import VedisMock


@pytest.fixture(scope="module")
def vedis_connection() -> VedisMock:
    return VedisMock()


@pytest.fixture(scope="module")
def vedis_config(vedis_connection) -> VedisConfigProvider:
    return VedisConfigProvider(vedis_connection=vedis_connection, hash_name="test")


@pytest.fixture(scope="module")
def vedis_credential(vedis_connection) -> VedisCredentialProvider:
    return VedisCredentialProvider(vedis_connection=vedis_connection, hash_name="test")
