from sitri.contrib.json import JsonCredentialProvider
from sitri.contrib.redis import RedisCredentialProvider
from sitri.contrib.system import SystemCredentialProvider
from sitri.contrib.vedis import VedisCredentialProvider


def test_get_by_codes(credential_manager):
    assert credential_manager.get_by_code(VedisCredentialProvider.provider_code) == VedisCredentialProvider
    assert credential_manager.get_by_code(RedisCredentialProvider.provider_code) == RedisCredentialProvider
    assert credential_manager.get_by_code(SystemCredentialProvider.provider_code) == SystemCredentialProvider
    assert credential_manager.get_by_code(JsonCredentialProvider.provider_code) == JsonCredentialProvider
