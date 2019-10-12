import pytest

from sitri import Sitri
from sitri.contrib.system import SystemConfigProvider, SystemCredentialProvider


def test_sitri_init():
    with pytest.raises(TypeError):
        Sitri(credential_provider=SystemCredentialProvider(prefix="test"))

    with pytest.raises(TypeError):
        Sitri(config_provider=SystemConfigProvider(prefix="test"))


def test_sitri_get_credential(test_sitri, monkeypatch):
    monkeypatch.setenv("TEST_KEY1", "1")
    monkeypatch.setenv("TEST_KEY2", "2")

    assert test_sitri.get_credential("key1") == "1"
    assert test_sitri.get_credential("key2") == "2"
    assert not test_sitri.get_credential("key3")

    monkeypatch.undo()


def test_sitri_get_config(test_sitri, monkeypatch):
    monkeypatch.setenv("TEST_KEY1", "1")
    monkeypatch.setenv("TEST_KEY2", "2")

    assert test_sitri.get_config("key1") == "1"
    assert test_sitri.get_config("key2") == "2"
    assert not test_sitri.get_config("key3")

    monkeypatch.undo()
