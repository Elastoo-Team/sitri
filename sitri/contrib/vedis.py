import contextlib
import typing

from loguru import logger

from ..config.providers import ConfigProvider
from ..credentials.providers import CredentialProvider


class VedisConfigProvider(ConfigProvider):
    """Config provider for vedis storage."""

    provider_code = "vedis"
    _hash_name = "sitri_config_hash"

    def __init__(self, vedis_connector: typing.Callable, hash_name: str = "sitri_config_hash"):
        """

        :param vedis_connector: return connection to vedis
        :param hash_name: name for hash (key-value object) in vedis
        """
        self._vedis_get = vedis_connector
        self._hash_name = hash_name

    @property
    def _vedis(self):
        return self._vedis_get()

    @property
    def _config_hash(self):
        return self._vedis.Hash(self._hash_name)

    @logger.catch(level="ERROR")
    def get(self, key: str, **kwargs) -> typing.Optional[str]:
        result = self._config_hash.get(key)

        if isinstance(result, bytes):
            return result.decode()

    @logger.catch(level="ERROR")
    def keys(self) -> typing.List[str]:
        var_list = []
        vars = self._config_hash.keys() if self._config_hash.keys() is not None else []

        for var in vars:
            var_list.append(var.decode())

        return var_list


class VedisCredentialProvider(CredentialProvider):
    """Credential provider for vedis storage."""

    provider_code = "vedis"
    prefix = "vedis"
    _hash_name = "vedis"

    def __init__(self, vedis_connector: typing.Callable, hash_name: str = "sitri_credential_hash"):
        """

        :param vedis_connector: return connection to vedis
        :param hash_name: name for hash (key-value object) in vedis
        """
        self._vedis_get = vedis_connector
        self._hash_name = hash_name

    @property
    def _vedis(self):
        return self._vedis_get()

    @property
    def _config_hash(self):
        return self._vedis.Hash(self._hash_name)

    @logger.catch(level="ERROR")
    def get(self, key: str, **kwargs) -> typing.Any:
        result = self._config_hash.get(key)

        if isinstance(result, bytes):
            with contextlib.suppress(Exception):
                return result.decode()
