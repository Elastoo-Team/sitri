import pytest

from sitri import Sitri
from sitri.contrib.system import SystemConfigProvider, SystemCredentialProvider


@pytest.fixture(scope="module")
def test_sitri():
    return Sitri(
        config_provider=SystemConfigProvider(prefix="test"), credential_provider=SystemCredentialProvider(prefix="test")
    )
