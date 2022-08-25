from __future__ import annotations

import typing as t

from sitri.providers.contrib.system import SystemConfigProvider


def test_metadata(system_config: SystemConfigProvider) -> None:
    """test_metadata.

    :param system_config:
    :rtype: None
    """
    assert system_config.provider_code == "system"
    assert system_config._prefix == "TEST"


def test_prefixize(system_config: SystemConfigProvider) -> None:
    """test_prefixize.

    :param system_config:
    :rtype: None
    """
    assert system_config.prefixize("key1") == "TEST_KEY1"
    assert system_config.unprefixize("TEST_KEY1") == "key1"


def test_get_variable(monkeypatch: t.Any, system_config: SystemConfigProvider) -> None:
    """test_get_variable.

    :param monkeypatch:
    :param system_config:
    :rtype: None
    """
    monkeypatch.setenv("TEST_KEY1", "1")
    monkeypatch.setenv("TEST_KEY2", "2")

    assert system_config.get("key1") == "1"
    assert system_config.get("key2") == "2"

    monkeypatch.undo()


def test_get_variables_list(monkeypatch: t.Any, system_config: SystemConfigProvider) -> None:
    """test_get_variables_list.

    :param monkeypatch:
    :param system_config:
    :rtype: None
    """
    monkeypatch.setenv("TEST_KEY1", "1")
    monkeypatch.setenv("TEST_KEY2", "2")

    monkeypatch.setenv("TEZT_T1", "1")
    monkeypatch.setenv("TEZT_T2", "2")

    assert "key1" in system_config.keys()
    assert "key2" in system_config.keys()
    assert "t1" not in system_config.keys()
    assert "t2" not in system_config.keys()

    monkeypatch.undo()
