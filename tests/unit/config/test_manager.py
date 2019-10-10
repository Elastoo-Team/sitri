from sitri.contrib.consul import ConsulConfigProvider
from sitri.contrib.json import JsonConfigProvider
from sitri.contrib.redis import RedisConfigProvider
from sitri.contrib.system import SystemConfigProvider
from sitri.contrib.vedis import VedisConfigProvider


def test_get_by_codes(config_manager):
    assert config_manager.get_by_code(VedisConfigProvider.provider_code) == VedisConfigProvider
    assert config_manager.get_by_code(ConsulConfigProvider.provider_code) == ConsulConfigProvider
    assert config_manager.get_by_code(RedisConfigProvider.provider_code) == RedisConfigProvider
    assert config_manager.get_by_code(SystemConfigProvider.provider_code) == SystemConfigProvider
    assert config_manager.get_by_code(JsonConfigProvider.provider_code) == JsonConfigProvider
