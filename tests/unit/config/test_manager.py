from __future__ import annotations

import typing as t

from sitri.providers.base import ConfigProviderManager
from sitri.providers.contrib.json import JsonConfigProvider
from sitri.providers.contrib.redis import RedisConfigProvider
from sitri.providers.contrib.system import SystemConfigProvider
from sitri.providers.contrib.vedis import VedisConfigProvider


def test_get_by_codes(config_manager: t.Type[ConfigProviderManager]) -> None:
    """test_get_by_codes.

    :param config_manager:
    """
    assert config_manager.get_by_code(VedisConfigProvider.provider_code) == VedisConfigProvider
    assert config_manager.get_by_code(RedisConfigProvider.provider_code) == RedisConfigProvider
    assert config_manager.get_by_code(SystemConfigProvider.provider_code) == SystemConfigProvider
    assert config_manager.get_by_code(JsonConfigProvider.provider_code) == JsonConfigProvider
