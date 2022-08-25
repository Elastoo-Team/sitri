from __future__ import annotations

import pytest

from sitri.providers.contrib.toml import TomlConfigProvider


def test_no_file_error() -> None:
    """test_no_file_error."""
    with pytest.raises(FileNotFoundError):
        TomlConfigProvider(toml_path="_data.toml")

    TomlConfigProvider(toml_path="_data.toml", found_file_error=False)


@pytest.mark.parametrize(
    "toml_config_obj",
    [pytest.lazy_fixture("toml_config"), pytest.lazy_fixture("toml_data_config")],
)
def test_metadata(toml_config_obj: TomlConfigProvider) -> None:
    """test_metadata.

    :param toml_config_obj:
    :rtype: None
    """
    assert toml_config_obj.provider_code == "toml"
    assert toml_config_obj.separator == "/"


@pytest.mark.parametrize(
    "toml_config_obj",
    [pytest.lazy_fixture("toml_config"), pytest.lazy_fixture("toml_data_config")],
)
def test_get_by_other(toml_config_obj: TomlConfigProvider) -> None:
    """test_get_by_other.

    :param toml_config_obj:
    :rtype: None
    """
    assert isinstance(toml_config_obj._get_by_path("test", separator=toml_config_obj.separator), dict)
    assert toml_config_obj._get_by_key("test.test_key2") is None
    assert toml_config_obj._get_by_path("test.test_key2", separator=toml_config_obj.separator) is None
    assert isinstance(toml_config_obj._get_by_key("test"), dict)
    assert toml_config_obj._get_by_path("test", separator=toml_config_obj.separator) == toml_config_obj._get_by_key(
        "test",
    )
    assert toml_config_obj._get_by_path(
        "test/test_key2",
        separator=toml_config_obj.separator,
    ) == toml_config_obj._get_by_key("test").get("test_key2")


@pytest.mark.parametrize(
    "toml_config_obj",
    [pytest.lazy_fixture("toml_config"), pytest.lazy_fixture("toml_data_config")],
)
def test_get(toml_config_obj: TomlConfigProvider) -> None:
    """test_get.

    :param toml_config_obj:
    """
    assert isinstance(toml_config_obj.get("test"), dict)
    assert isinstance(toml_config_obj.get("test", path_mode=True), dict)
    assert toml_config_obj.get("test", path_mode=True) == toml_config_obj.get("test")
    assert toml_config_obj.get("test/test_key2", path_mode=True) and toml_config_obj.get(
        "test/test_key2",
        path_mode=True,
    ) == toml_config_obj.get("test").get("test_key2")
    assert toml_config_obj.get("test.test_key2", separator=".", path_mode=True) == toml_config_obj.get(
        "test/test_key2",
        path_mode=True,
    )
    assert not toml_config_obj.get("test/test_key2")


@pytest.mark.parametrize(
    "toml_config_obj",
    [pytest.lazy_fixture("toml_config"), pytest.lazy_fixture("toml_data_config")],
)
def test_keys(toml_config_obj: TomlConfigProvider) -> None:
    """test_keys.

    :param toml_config_obj:
    """
    assert "test" in toml_config_obj.keys()

    with pytest.raises(NotImplementedError):
        toml_config_obj.keys(path_mode=True)
