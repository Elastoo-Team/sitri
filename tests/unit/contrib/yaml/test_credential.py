import pytest


def test_metadata(yaml_credential) -> None:
    assert yaml_credential.provider_code == "yaml"
    assert yaml_credential.separator == "/"


def test_get_by_other(yaml_credential) -> None:
    assert isinstance(yaml_credential._get_by_path("test", separator=yaml_credential.separator), dict)
    assert yaml_credential._get_by_key("test.test_key2") is None
    assert yaml_credential._get_by_path("test.test_key2", separator=yaml_credential.separator) is None
    assert isinstance(yaml_credential._get_by_key("test"), dict)
    assert yaml_credential._get_by_path("test", separator=yaml_credential.separator) == yaml_credential._get_by_key(
        "test"
    )
    assert yaml_credential._get_by_path(
        "test/test_key2", separator=yaml_credential.separator
    ) == yaml_credential._get_by_key("test").get("test_key2")


def test_get(yaml_credential):
    assert isinstance(yaml_credential.get("test"), dict)
    assert isinstance(yaml_credential.get("test", path_mode=True), dict)
    assert yaml_credential.get("test", path_mode=True) == yaml_credential.get("test")
    assert yaml_credential.get("test/test_key2", path_mode=True) and yaml_credential.get(
        "test/test_key2", path_mode=True
    ) == yaml_credential.get("test").get("test_key2")
    assert yaml_credential.get("test.test_key2", separator=".", path_mode=True) == yaml_credential.get(
        "test/test_key2", path_mode=True
    )
    assert not yaml_credential.get("test/test_key2")


def test_keys(yaml_credential):
    assert "test" in yaml_credential.keys()

    with pytest.raises(NotImplementedError):
        yaml_credential.keys(path_mode=True)
