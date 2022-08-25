from __future__ import annotations

import pytest

from sitri import Sitri
from sitri.providers.contrib.system import SystemConfigProvider


@pytest.fixture(scope="module")
def test_sitri() -> Sitri:
    """test_sitri."""
    return Sitri(config_provider=SystemConfigProvider(prefix="test"))
