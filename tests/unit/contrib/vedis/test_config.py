def test_metadata(vedis_config) -> None:
    assert vedis_config.provider_code == "vedis"
    assert vedis_config._hash_name == "test"


def test_get_variable(monkeypatch, vedis_config) -> None:
    monkeypatch.setenv("key1", "1")
    monkeypatch.setenv("key2", "2")

    assert vedis_config.get("key1") == "1"
    assert vedis_config.get("key2") == "2"

    monkeypatch.undo()


def test_get_variables_list(monkeypatch, vedis_config) -> None:
    monkeypatch.setenv("key1", "1")
    monkeypatch.setenv("key2", "2")

    assert "key1" in vedis_config.keys()
    assert "key2" in vedis_config.keys()
    assert "kZ1" not in vedis_config.keys()
    assert "kZ2" not in vedis_config.keys()

    monkeypatch.undo()
