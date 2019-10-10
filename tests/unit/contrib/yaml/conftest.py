import pytest

from sitri.contrib.yaml import YamlConfigProvider, YamlCredentialProvider


@pytest.fixture(scope="module")
def path_to_yaml() -> str:
    return "tests/unit/contrib/yaml/data.yaml"


@pytest.fixture(scope="module")
def yaml_config(path_to_yaml) -> YamlConfigProvider:
    return YamlConfigProvider(yaml_path=path_to_yaml, default_separator="/")


@pytest.fixture(scope="module")
def yaml_credential(path_to_yaml) -> YamlCredentialProvider:
    return YamlCredentialProvider(yaml_path=path_to_yaml, default_separator="/")
