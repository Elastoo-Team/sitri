from __future__ import annotations

import pytest

from sitri.providers.contrib.yaml import YamlConfigProvider


def test_no_file_error() -> None:
    """test_no_file_error."""
    with pytest.raises(FileNotFoundError):
        YamlConfigProvider(yaml_path="_data.yaml")

    YamlConfigProvider(yaml_path="_data.yaml", found_file_error=False)


@pytest.mark.parametrize(
    "yaml_config_obj",
    [pytest.lazy_fixture("yaml_config"), pytest.lazy_fixture("yaml_data_config")],
)
def test_metadata(yaml_config_obj: YamlConfigProvider) -> None:
    """test_metadata.

    :param yaml_config_obj:
    :rtype: None
    """
    assert yaml_config_obj.provider_code == "yaml"
    assert yaml_config_obj.separator == "/"


@pytest.mark.parametrize(
    "yaml_config_obj",
    [pytest.lazy_fixture("yaml_config"), pytest.lazy_fixture("yaml_data_config")],
)
def test_get_by_other(yaml_config_obj: YamlConfigProvider) -> None:
    """test_get_by_other.

    :param yaml_config_obj:
    :rtype: None
    """
    assert isinstance(yaml_config_obj._get_by_path("test", separator=yaml_config_obj.separator), dict)
    assert yaml_config_obj._get_by_key("test.test_key2") is None
    assert yaml_config_obj._get_by_path("test.test_key2", separator=yaml_config_obj.separator) is None
    assert isinstance(yaml_config_obj._get_by_key("test"), dict)
    assert yaml_config_obj._get_by_path("test", separator=yaml_config_obj.separator) == yaml_config_obj._get_by_key(
        "test",
    )
    assert yaml_config_obj._get_by_path(
        "test/test_key2",
        separator=yaml_config_obj.separator,
    ) == yaml_config_obj._get_by_key("test").get("test_key2")


@pytest.mark.parametrize(
    "yaml_config_obj",
    [pytest.lazy_fixture("yaml_config"), pytest.lazy_fixture("yaml_data_config")],
)
def test_get(yaml_config_obj: YamlConfigProvider) -> None:
    """test_get.

    :param yaml_config_obj:
    """
    assert isinstance(yaml_config_obj.get("test"), dict)
    assert isinstance(yaml_config_obj.get("test", path_mode=True), dict)
    assert yaml_config_obj.get("test", path_mode=True) == yaml_config_obj.get("test")
    assert yaml_config_obj.get("test/test_key2", path_mode=True) and yaml_config_obj.get(
        "test/test_key2",
        path_mode=True,
    ) == yaml_config_obj.get("test").get("test_key2")
    assert yaml_config_obj.get("test.test_key2", separator=".", path_mode=True) == yaml_config_obj.get(
        "test/test_key2",
        path_mode=True,
    )
    assert not yaml_config_obj.get("test/test_key2")


@pytest.mark.parametrize(
    "yaml_config_obj",
    [pytest.lazy_fixture("yaml_config"), pytest.lazy_fixture("yaml_data_config")],
)
def test_keys(yaml_config_obj: YamlConfigProvider) -> None:
    """test_keys.

    :param yaml_config_obj:
    """
    assert "test" in yaml_config_obj.keys()

    with pytest.raises(NotImplementedError):
        yaml_config_obj.keys(path_mode=True)
