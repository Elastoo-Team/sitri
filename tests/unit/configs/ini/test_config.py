import pytest

from sitri.providers.contrib.ini import IniConfigProvider


def test_no_file_error():
    with pytest.raises(FileNotFoundError):
        IniConfigProvider(ini_path="not_exists.ini")


@pytest.mark.parametrize(
    "ini_config_obj", [pytest.lazy_fixture("ini_config")]
)
def test_metadata(ini_config_obj) -> None:
    assert ini_config_obj.provider_code == "ini"


@pytest.mark.parametrize(
    "ini_config_obj", [pytest.lazy_fixture("ini_config")]
)
def test_sections(ini_config_obj):
    assert isinstance(ini_config_obj.sections, list)
    assert sorted(ini_config_obj.sections) == ["DEFAULTS", "test_a", "test_b"]


@pytest.mark.parametrize(
    "ini_config_obj", [pytest.lazy_fixture("ini_config")]
)
def test_keys(ini_config_obj):
    assert ini_config_obj.keys("test_a") == ["hello"]
    assert ini_config_obj.keys("test_b") == ["test_a", "test_b"]
    assert ini_config_obj.keys("not_exist") == []


@pytest.mark.parametrize(
    "ini_config_obj", [pytest.lazy_fixture("ini_config")]
)
def test_get(ini_config_obj):
    assert ini_config_obj.keys(section="test_a", key="hello") == "world"
    assert ini_config_obj.keys(section="test_a", key="not_exist") is None
    assert ini_config_obj.keys(section="test_a", key="not_exist", default="fallback") == "fallback"
    assert ini_config_obj.keys(section="test_b", key="str") == "str"
    assert ini_config_obj.keys(section="test_b", key="int") == "1"
    assert ini_config_obj.keys(section="not_exist", key="int") is None
