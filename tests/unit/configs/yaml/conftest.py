import pytest
import yaml

from sitri.providers.contrib.yaml import YamlConfigProvider

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


@pytest.fixture(scope="module")
def yaml_data() -> str:
    data = {"test": {"test_key1": "1", "test_key2": "2", "test_key3": "3"}}

    stream = StringIO()

    yaml.dump(data, stream)

    return stream.getvalue()


@pytest.fixture(scope="module")
def path_to_yaml() -> str:
    return "tests/unit/configs/yaml/data.yaml"


@pytest.fixture(scope="module")
def yaml_data_config(yaml_data) -> YamlConfigProvider:
    return YamlConfigProvider(yaml_data=yaml_data, default_separator="/")


@pytest.fixture(scope="module")
def yaml_config(path_to_yaml) -> YamlConfigProvider:
    return YamlConfigProvider(yaml_path=path_to_yaml, default_separator="/")
