from __future__ import annotations

import pytest

from sitri.providers.base import ConfigProviderManager


@pytest.fixture(scope="module")
def config_manager() -> type[ConfigProviderManager]:
    """config_manager.

    :rtype: type[ConfigProviderManager]
    """
    return ConfigProviderManager
