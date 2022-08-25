from __future__ import annotations

import typing as t

import pytest

from sitri.providers.base import ConfigProviderManager


@pytest.fixture(scope="module")
def config_manager() -> t.Type[ConfigProviderManager]:
    """config_manager.

    :rtype: t.Type[ConfigProviderManager]
    """
    return ConfigProviderManager
