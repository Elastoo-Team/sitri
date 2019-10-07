import typing

import vedis

from ..config.providers import ConfigProvider
from ..credentials.providers import CredentialProvider


class VedisConfigProvider(ConfigProvider):
    """Config provider for vedis storage
    """

    provider_code = "vedis"
    _hash_name = "sitri_config_hash"

    def __init__(self, vedis_connection: vedis.Vedis, hash_name: str = "sitri_config_hash"):
        """

        :param vedis_connection: connection to vedis
        :param hash_name: name for hash (key-value object) in vedis
        """
        self._vedis = vedis_connection
        self._hash_name = hash_name
        self._config_hash = self._vedis.Hash(self._hash_name)

    def get(self, key: str) -> typing.Optional[str]:
        result = self._config_hash.get(key)

        if isinstance(result, bytes):
            return result.decode()
        return None

    def keys(self) -> typing.List[str]:
        var_list = []
        vars = self._config_hash.keys() if self._config_hash.keys() is not None else []

        for var in vars:
            var_list.append(var.decode())

        return var_list


class VedisCredentialProvider(CredentialProvider):
    """Credential provider for vedis storage
    """

    provider_code = "vedis"
    project_prefix = "vedis"
    _hash_name = "sitri_config_hash"

    def __init__(self, vedis_connection: vedis.Vedis, hash_name: str = "sitri_config_hash"):
        """

        :param vedis_connection: connection to vedis
        :param hash_name: name for hash (key-value object) in vedis
        """
        self._vedis = vedis_connection
        self._hash_name = hash_name
        self._config_hash = self._vedis.Hash(self._hash_name)

    def get(self, key: str) -> typing.Any:
        result = self._config_hash.get(key)

        if isinstance(result, bytes):
            try:
                return result.decode()
            except Exception:
                return None
