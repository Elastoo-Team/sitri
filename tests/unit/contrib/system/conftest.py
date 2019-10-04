import pytest

from sitri.contrib.system import SystemConfigProvider, SystemCredentialProvider


@pytest.fixture(scope="module")
def system_config() -> SystemConfigProvider:
    return SystemConfigProvider(project_prefix="test")


@pytest.fixture(scope="module")
def system_credential() -> SystemCredentialProvider:
    return SystemCredentialProvider(project_prefix="test")
