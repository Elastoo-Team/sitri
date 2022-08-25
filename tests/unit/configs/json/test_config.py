from __future__ import annotations

import pytest

from sitri.providers.contrib.json import JsonConfigProvider


def test_no_file_error() -> None:
    """test_no_file_error."""
    with pytest.raises(FileNotFoundError):
        JsonConfigProvider(json_path="_data.json")

    JsonConfigProvider(json_path="_data.json", found_file_error=False)


@pytest.mark.parametrize(
    "json_config_obj",
    [pytest.lazy_fixture("json_config"), pytest.lazy_fixture("json_config_data")],
)
def test_metadata(json_config_obj: JsonConfigProvider) -> None:
    """test_metadata.

    :param json_config_obj:
    :rtype: None
    """
    assert json_config_obj.provider_code == "json"
    assert json_config_obj.separator == "/"


@pytest.mark.parametrize(
    "json_config_obj",
    [pytest.lazy_fixture("json_config"), pytest.lazy_fixture("json_config_data")],
)
def test_get_by_other(json_config_obj: JsonConfigProvider) -> None:
    """test_get_by_other.

    :param json_config_obj:
    :rtype: None
    """
    assert isinstance(json_config_obj._get_by_path("test", separator=json_config_obj.separator), dict)
    assert json_config_obj._get_by_key("test.test_key2") is None
    assert json_config_obj._get_by_path("test.test_key2", separator=json_config_obj.separator) is None
    assert isinstance(json_config_obj._get_by_key("test"), dict)
    assert json_config_obj._get_by_path("test", separator=json_config_obj.separator) == json_config_obj._get_by_key(
        "test",
    )
    assert json_config_obj._get_by_path(
        "test/test_key2",
        separator=json_config_obj.separator,
    ) == json_config_obj._get_by_key("test").get("test_key2")


@pytest.mark.parametrize(
    "json_config_obj",
    [pytest.lazy_fixture("json_config"), pytest.lazy_fixture("json_config_data")],
)
def test_get(json_config_obj: JsonConfigProvider) -> None:
    """test_get.

    :param json_config_obj:
    """
    assert isinstance(json_config_obj.get("test"), dict)
    assert isinstance(json_config_obj.get("test", path_mode=True), dict)
    assert json_config_obj.get("test", path_mode=True) == json_config_obj.get("test")
    assert json_config_obj.get("test/test_key2", path_mode=True) and json_config_obj.get(
        "test/test_key2",
        path_mode=True,
    ) == json_config_obj.get("test").get("test_key2")
    assert json_config_obj.get("test.test_key2", separator=".", path_mode=True) == json_config_obj.get(
        "test/test_key2",
        path_mode=True,
    )
    assert not json_config_obj.get("test/test_key2")


@pytest.mark.parametrize(
    "json_config_obj",
    [pytest.lazy_fixture("json_config"), pytest.lazy_fixture("json_config_data")],
)
def test_keys(json_config_obj: JsonConfigProvider) -> None:
    """test_keys.

    :param json_config_obj:
    """
    assert "test" in json_config_obj.keys()

    with pytest.raises(NotImplementedError):
        json_config_obj.keys(path_mode=True)
