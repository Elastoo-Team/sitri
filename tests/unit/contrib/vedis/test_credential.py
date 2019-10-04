def test_metadata(vedis_credential) -> None:
    assert vedis_credential.provider_code == "vedis"
    assert vedis_credential._project_prefix == "TEST"
    assert vedis_credential._hash_name == "test"


def test_prefixize(vedis_credential) -> None:
    assert vedis_credential.prefixize("key1") == "TEST_KEY1"


def test_get_credential(monkeypatch, vedis_credential) -> None:
    monkeypatch.setenv("TEST_KEY1", "1")
    monkeypatch.setenv("TEST_KEY2", "2")

    assert vedis_credential.get_credential("key1") == "1"
    assert vedis_credential.get_credential("key2") == "2"

    monkeypatch.undo()
