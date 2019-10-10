import pytest


def test_metadata(yaml_config) -> None:
    assert yaml_config.provider_code == "yaml"
    assert yaml_config.separator == "/"


def test_get_by_other(yaml_config) -> None:
    assert isinstance(yaml_config._get_by_path("test", separator=yaml_config.separator), dict)
    assert yaml_config._get_by_key("test.test_key2") is None
    assert yaml_config._get_by_path("test.test_key2", separator=yaml_config.separator) is None
    assert isinstance(yaml_config._get_by_key("test"), dict)
    assert yaml_config._get_by_path("test", separator=yaml_config.separator) == yaml_config._get_by_key("test")
    assert yaml_config._get_by_path("test/test_key2", separator=yaml_config.separator) == yaml_config._get_by_key(
        "test"
    ).get("test_key2")


def test_get(yaml_config):
    assert isinstance(yaml_config.get("test"), dict)
    assert isinstance(yaml_config.get("test", path_mode=True), dict)
    assert yaml_config.get("test", path_mode=True) == yaml_config.get("test")
    assert yaml_config.get("test/test_key2", path_mode=True) and yaml_config.get(
        "test/test_key2", path_mode=True
    ) == yaml_config.get("test").get("test_key2")
    assert yaml_config.get("test.test_key2", separator=".", path_mode=True) == yaml_config.get(
        "test/test_key2", path_mode=True
    )
    assert not yaml_config.get("test/test_key2")


def test_keys(yaml_config):
    assert "test" in yaml_config.keys()

    with pytest.raises(NotImplementedError):
        yaml_config.keys(path_mode=True)
