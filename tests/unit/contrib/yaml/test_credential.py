import pytest

from sitri.contrib.yaml import YamlCredentialProvider


def test_no_file_error():
    with pytest.raises(FileNotFoundError):
        YamlCredentialProvider(yaml_path="_data.yaml")

    YamlCredentialProvider(yaml_path="_data.yaml", found_file_error=False)


@pytest.mark.parametrize(
    "yaml_credential_obj", [pytest.lazy_fixture("yaml_credential"), pytest.lazy_fixture("yaml_data_credential")]
)
def test_metadata(yaml_credential_obj) -> None:
    assert yaml_credential_obj.provider_code == "yaml"
    assert yaml_credential_obj.separator == "/"


@pytest.mark.parametrize(
    "yaml_credential_obj", [pytest.lazy_fixture("yaml_credential"), pytest.lazy_fixture("yaml_data_credential")]
)
def test_get_by_other(yaml_credential_obj) -> None:
    assert isinstance(yaml_credential_obj._get_by_path("test", separator=yaml_credential_obj.separator), dict)
    assert yaml_credential_obj._get_by_key("test.test_key2") is None
    assert yaml_credential_obj._get_by_path("test.test_key2", separator=yaml_credential_obj.separator) is None
    assert isinstance(yaml_credential_obj._get_by_key("test"), dict)
    assert yaml_credential_obj._get_by_path(
        "test", separator=yaml_credential_obj.separator
    ) == yaml_credential_obj._get_by_key("test")
    assert yaml_credential_obj._get_by_path(
        "test/test_key2", separator=yaml_credential_obj.separator
    ) == yaml_credential_obj._get_by_key("test").get("test_key2")


@pytest.mark.parametrize(
    "yaml_credential_obj", [pytest.lazy_fixture("yaml_credential"), pytest.lazy_fixture("yaml_data_credential")]
)
def test_get(yaml_credential_obj):
    assert isinstance(yaml_credential_obj.get("test"), dict)
    assert isinstance(yaml_credential_obj.get("test", path_mode=True), dict)
    assert yaml_credential_obj.get("test", path_mode=True) == yaml_credential_obj.get("test")
    assert yaml_credential_obj.get("test/test_key2", path_mode=True) and yaml_credential_obj.get(
        "test/test_key2", path_mode=True
    ) == yaml_credential_obj.get("test").get("test_key2")
    assert yaml_credential_obj.get("test.test_key2", separator=".", path_mode=True) == yaml_credential_obj.get(
        "test/test_key2", path_mode=True
    )
    assert not yaml_credential_obj.get("test/test_key2")


@pytest.mark.parametrize(
    "yaml_credential_obj", [pytest.lazy_fixture("yaml_credential"), pytest.lazy_fixture("yaml_data_credential")]
)
def test_keys(yaml_credential_obj):
    assert "test" in yaml_credential_obj.keys()

    with pytest.raises(NotImplementedError):
        yaml_credential_obj.keys(path_mode=True)
