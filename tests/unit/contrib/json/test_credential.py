import pytest

from sitri.contrib.json import JsonCredentialProvider


def test_no_file_error():
    with pytest.raises(FileNotFoundError):
        JsonCredentialProvider(json_path="_data.json")

    JsonCredentialProvider(json_path="_data.json", found_file_error=False)


@pytest.mark.parametrize(
    "json_credential_obj", [pytest.lazy_fixture("json_credential"), pytest.lazy_fixture("json_data_credential")]
)
def test_metadata(json_credential_obj) -> None:
    assert json_credential_obj.provider_code == "json"
    assert json_credential_obj.separator == "/"


@pytest.mark.parametrize(
    "json_credential_obj", [pytest.lazy_fixture("json_credential"), pytest.lazy_fixture("json_data_credential")]
)
def test_get_by_other(json_credential_obj) -> None:
    assert isinstance(json_credential_obj._get_by_path("test", separator=json_credential_obj.separator), dict)
    assert json_credential_obj._get_by_key("test.test_key2") is None
    assert json_credential_obj._get_by_path("test.test_key2", separator=json_credential_obj.separator) is None
    assert isinstance(json_credential_obj._get_by_key("test"), dict)
    assert json_credential_obj._get_by_path(
        "test", separator=json_credential_obj.separator
    ) == json_credential_obj._get_by_key("test")
    assert json_credential_obj._get_by_path(
        "test/test_key2", separator=json_credential_obj.separator
    ) == json_credential_obj._get_by_key("test").get("test_key2")


@pytest.mark.parametrize(
    "json_credential_obj", [pytest.lazy_fixture("json_credential"), pytest.lazy_fixture("json_data_credential")]
)
def test_get(json_credential_obj):
    assert isinstance(json_credential_obj.get("test"), dict)
    assert isinstance(json_credential_obj.get("test", path_mode=True), dict)
    assert json_credential_obj.get("test", path_mode=True) == json_credential_obj.get("test")
    assert json_credential_obj.get("test/test_key2", path_mode=True) and json_credential_obj.get(
        "test/test_key2", path_mode=True
    ) == json_credential_obj.get("test").get("test_key2")
    assert json_credential_obj.get("test.test_key2", separator=".", path_mode=True) == json_credential_obj.get(
        "test/test_key2", path_mode=True
    )
    assert not json_credential_obj.get("test/test_key2")


@pytest.mark.parametrize(
    "json_credential_obj", [pytest.lazy_fixture("json_credential"), pytest.lazy_fixture("json_data_credential")]
)
def test_keys(json_credential_obj):
    assert "test" in json_credential_obj.keys()

    with pytest.raises(NotImplementedError):
        json_credential_obj.keys(path_mode=True)
