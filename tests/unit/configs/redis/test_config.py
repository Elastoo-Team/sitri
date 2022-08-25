from __future__ import annotations

import typing as t

from sitri.providers.contrib.redis import RedisConfigProvider


def test_metadata(redis_config: RedisConfigProvider) -> None:
    """test_metadata.

    :param redis_config:
    :rtype: None
    """
    assert redis_config.provider_code == "redis"
    assert redis_config._prefix == "TEST"


def test_prefixize(redis_config: RedisConfigProvider) -> None:
    """test_prefixize.

    :param redis_config:
    :rtype: None
    """
    assert redis_config.prefixize("key1") == "TEST_KEY1"
    assert redis_config.unprefixize("TEST_KEY1") == "key1"


def test_get_variable(monkeypatch: t.Any, redis_config: RedisConfigProvider) -> None:
    """test_get_variable.

    :param monkeypatch:
    :param redis_config:
    :rtype: None
    """
    monkeypatch.setenv("TEST_KEY1", "1")
    monkeypatch.setenv("TEST_KEY2", "2")

    assert redis_config.get("key1") == "1"
    assert redis_config.get("key2") == "2"

    monkeypatch.undo()


def test_get_variables_list(monkeypatch: t.Any, redis_config: RedisConfigProvider) -> None:
    """test_get_variables_list.

    :param monkeypatch:
    :param redis_config:
    :rtype: None
    """
    monkeypatch.setenv("TEST_KEY1", "1")
    monkeypatch.setenv("TEST_KEY2", "2")

    monkeypatch.setenv("TEZT_T1", "1")
    monkeypatch.setenv("TEZT_T2", "2")

    assert "key1" in redis_config.keys()
    assert "key2" in redis_config.keys()
    assert "t1" not in redis_config.keys()
    assert "t2" not in redis_config.keys()

    monkeypatch.undo()
