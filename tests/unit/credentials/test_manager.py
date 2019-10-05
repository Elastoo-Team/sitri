from sitri.contrib.vedis import VedisCredentialProvider
from sitri.contrib.redis import RedisCredentialProvider
from sitri.contrib.system import SystemCredentialProvider


def test_get_by_codes(credential_manager):
    assert credential_manager.get_by_code(VedisCredentialProvider.provider_code) == VedisCredentialProvider
    assert credential_manager.get_by_code(RedisCredentialProvider.provider_code) == RedisCredentialProvider
    assert credential_manager.get_by_code(SystemCredentialProvider.provider_code) == SystemCredentialProvider
