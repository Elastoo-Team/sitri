def test_metadata(system_credential) -> None:
    assert system_credential.provider_code == "system"
    assert system_credential._project_prefix == "TEST"


def test_prefixize(system_credential) -> None:
    assert system_credential.prefixize("key1") == "TEST_KEY1"


def test_get_credential(monkeypatch, system_credential) -> None:
    monkeypatch.setenv("TEST_KEY1", "1")
    monkeypatch.setenv("TEST_KEY2", "2")

    assert system_credential.get_credential("key1") == "1"
    assert system_credential.get_credential("key2") == "2"

    monkeypatch.undo()
