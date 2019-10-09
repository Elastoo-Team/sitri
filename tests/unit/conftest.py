import pytest
from sitri.contrib.system import SystemConfigProvider, SystemCredentialProvider
from sitri import Sitri


@pytest.fixture(scope="module")
def test_sitri():
    return Sitri(config_provider=SystemConfigProvider(prefix="test"),
                 credential_provider=SystemCredentialProvider(prefix="test"))
