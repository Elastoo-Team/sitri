import typing

import pytest

from sitri.providers.base import ConfigProviderManager


@pytest.fixture(scope="module")
def config_manager() -> typing.Type[ConfigProviderManager]:
    return ConfigProviderManager
