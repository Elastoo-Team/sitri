from __future__ import annotations

import pytest
from _pytest.monkeypatch import MonkeyPatch

from sitri import Sitri
from sitri.configurator import SitriProviderConfigurator


def test_sitri_init() -> None:
    """test_sitri_init."""
    with pytest.raises(TypeError):
        Sitri()


def test_sitri_get_config(test_sitri: SitriProviderConfigurator, monkeypatch: MonkeyPatch) -> None:
    """test_sitri_get_config.

    :param test_sitri:
    :param monkeypatch:
    """
    monkeypatch.setenv("TEST_KEY1", "1")
    monkeypatch.setenv("TEST_KEY2", "2")

    assert test_sitri.get("key1") == "1"
    assert test_sitri.get("key2") == "2"
    assert not test_sitri.get("key3")

    monkeypatch.undo()
