from __future__ import annotations

import pytest

from sitri.providers.contrib.system import SystemConfigProvider


@pytest.fixture(scope="module")
def system_config() -> SystemConfigProvider:
    """system_config.

    :rtype: SystemConfigProvider
    """
    return SystemConfigProvider(prefix="test")
