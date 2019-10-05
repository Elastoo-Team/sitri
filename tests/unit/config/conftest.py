import pytest
import typing

from sitri.config.providers import ConfigProviderManager


@pytest.fixture(scope="module")
def config_manager() -> typing.Type[ConfigProviderManager]:
    return ConfigProviderManager
