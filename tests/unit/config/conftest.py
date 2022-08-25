from __future__ import annotations

from typing import Type

import pytest

from sitri.providers.base import ConfigProviderManager


@pytest.fixture(scope="module")
def config_manager() -> Type[ConfigProviderManager]:
    """config_manager.

    :rtype: Type[ConfigProviderManager]
    """
    return ConfigProviderManager
