from __future__ import annotations

import pytest

from sitri.providers.contrib.ini import IniConfigProvider


def test_no_file_error() -> None:
    """test_no_file_error."""
    with pytest.raises(FileNotFoundError):
        IniConfigProvider(ini_path="not_exists.ini")


def test_metadata(ini_config: IniConfigProvider) -> None:
    """test_metadata.

    :param ini_config:
    :rtype: None
    """
    assert ini_config.provider_code == "ini"


def test_sections(ini_config: IniConfigProvider) -> None:
    """test_sections.

    :param ini_config:
    """
    assert isinstance(ini_config.sections, list)
    assert sorted(ini_config.sections) == ["DEFAULT", "test_a", "test_b"]


def test_keys(ini_config: IniConfigProvider) -> None:
    """test_keys.

    :param ini_config:
    """
    assert ini_config.keys("test_a") == ["hello"]
    assert ini_config.keys("test_b") == ["str", "int"]
    assert ini_config.keys("not_exist") == []


def test_get(ini_config: IniConfigProvider) -> None:
    """test_get.

    :param ini_config:
    """
    assert ini_config.get(section="test_a", key="hello") == "world"
    assert ini_config.get(section="test_a", key="not_exist") is None
    assert ini_config.get(section="test_b", key="str") == "str"
    assert ini_config.get(section="test_b", key="int") == "1"
    assert ini_config.get(section="not_exist", key="int") is None
