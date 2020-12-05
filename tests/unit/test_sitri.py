import pytest

from sitri import Sitri


def test_sitri_init():
    with pytest.raises(TypeError):
        Sitri()


def test_sitri_get_config(test_sitri, monkeypatch):
    monkeypatch.setenv("TEST_KEY1", "1")
    monkeypatch.setenv("TEST_KEY2", "2")

    assert test_sitri.get_config("key1") == "1"
    assert test_sitri.get_config("key2") == "2"
    assert not test_sitri.get_config("key3")

    monkeypatch.undo()
