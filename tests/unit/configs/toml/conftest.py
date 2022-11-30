from __future__ import annotations

import pytest
import tomli_w

from sitri.providers.contrib.toml import TomlConfigProvider


@pytest.fixture(scope="module")
def toml_data() -> str:
    """toml_data.

    :rtype: str
    """
    data = {"test": {"test_key1": "1", "test_key2": "2", "test_key3": "3"}}

    return tomli_w.dumps(data)


@pytest.fixture(scope="module")
def path_to_toml() -> str:
    """path_to_toml.

    :rtype: str
    """
    return "tests/unit/configs/toml/data.toml"


@pytest.fixture(scope="module")
def toml_data_config(toml_data: str) -> TomlConfigProvider:
    """toml_data_config.

    :param toml_data:
    :rtype: TomlConfigProvider
    """

    return TomlConfigProvider(toml_data=toml_data, default_separator="/")


@pytest.fixture(scope="module")
def toml_config(path_to_toml: str) -> TomlConfigProvider:
    """toml_config.

    :param path_to_toml:
    :rtype: TomlConfigProvider
    """
    return TomlConfigProvider(toml_path=path_to_toml, default_separator="/")
