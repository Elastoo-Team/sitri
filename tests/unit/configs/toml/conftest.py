import pytest
import toml

from sitri.providers.contrib.toml import TomlConfigProvider

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


@pytest.fixture(scope="module")
def toml_data() -> str:
    data = {"test": {"test_key1": "1", "test_key2": "2", "test_key3": "3"}}

    return toml.dumps(data)


@pytest.fixture(scope="module")
def path_to_toml() -> str:
    return "tests/unit/configs/toml/data.toml"


@pytest.fixture(scope="module")
def toml_data_config(toml_data) -> TomlConfigProvider:
    print(toml_data)
    return TomlConfigProvider(toml_data=toml_data, default_separator="/")


@pytest.fixture(scope="module")
def toml_config(path_to_toml) -> TomlConfigProvider:
    return TomlConfigProvider(toml_path=path_to_toml, default_separator="/")
