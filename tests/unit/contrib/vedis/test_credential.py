def test_metadata(vedis_credential) -> None:
    assert vedis_credential.provider_code == "vedis"
    assert vedis_credential._hash_name == "test"


def test_get_credential(monkeypatch, vedis_credential) -> None:
    monkeypatch.setenv("key1", "1")
    monkeypatch.setenv("key2", "2")

    assert vedis_credential.get("key1") == "1"
    assert vedis_credential.get("key2") == "2"

    monkeypatch.undo()
