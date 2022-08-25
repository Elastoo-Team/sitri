from __future__ import annotations

from _pytest.monkeypatch import MonkeyPatch

from sitri.providers.contrib.vedis import VedisConfigProvider


def test_metadata(vedis_config: VedisConfigProvider) -> None:
    """test_metadata.

    :param vedis_config:
    :rtype: None
    """
    assert vedis_config.provider_code == "vedis"
    assert vedis_config._hash_name == "test"


def test_get_variable(monkeypatch: MonkeyPatch, vedis_config: VedisConfigProvider) -> None:
    """test_get_variable.

    :param monkeypatch:
    :param vedis_config:
    :rtype: None
    """
    monkeypatch.setenv("key1", "1")
    monkeypatch.setenv("key2", "2")

    assert vedis_config.get("key1") == "1"
    assert vedis_config.get("key2") == "2"

    monkeypatch.undo()


def test_get_variables_list(monkeypatch: MonkeyPatch, vedis_config: VedisConfigProvider) -> None:
    """test_get_variables_list.

    :param monkeypatch:
    :param vedis_config:
    :rtype: None
    """
    monkeypatch.setenv("key1", "1")
    monkeypatch.setenv("key2", "2")

    assert "key1" in vedis_config.keys()
    assert "key2" in vedis_config.keys()
    assert "kZ1" not in vedis_config.keys()
    assert "kZ2" not in vedis_config.keys()

    monkeypatch.undo()
