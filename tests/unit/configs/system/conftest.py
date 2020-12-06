import pytest

from sitri.providers.contrib.system import SystemConfigProvider


@pytest.fixture(scope="module")
def system_config() -> SystemConfigProvider:
    return SystemConfigProvider(prefix="test")
