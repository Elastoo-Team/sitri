import typing

import hvac
from loguru import logger

from sitri.providers.base import ConfigProvider


class VaultKVConfigProvider(ConfigProvider):
    """Config provider for vault_kv storage.

    Only for kv first version at the moment.
    """

    provider_code = "vault_kv"

    def __init__(
        self,
        vault_connector: typing.Callable[[], hvac.Client],
        mount_point: typing.Optional[str] = None,
        secret_path: typing.Optional[str] = None,
    ):
        """
        :param vault_connector: function return connection to Vault
        :param mount_point: default vault_kv kv1 storage mount point
        :param secret_path: default path to the secret in mounted
        """

        self._vault_get = vault_connector
        self._vault_hvac_instance = None
        self._mount_point = mount_point
        self._secret_path = secret_path

    @property
    def _vault(self) -> hvac.Client:
        if not self._vault_hvac_instance:
            self._vault_hvac_instance = self._vault_get()

        return self._vault_hvac_instance

    @logger.catch(level="ERROR")
    def get(
        self, key: str, mount_point: typing.Optional[str] = None, secret_path: typing.Optional[str] = None, **kwargs
    ) -> typing.Optional[str]:
        request_params = {
            "path": secret_path if secret_path else self._secret_path,
            "mount_point": mount_point if mount_point else self._mount_point,
        }

        response = self._vault.secrets.kv.v1.read_secret(**request_params)

        return response["data"].get(key)

    @logger.catch(level="ERROR")
    def keys(
        self, mount_point: typing.Optional[str] = None, secret_path: typing.Optional[str] = None, **kwargs
    ) -> typing.List[str]:
        request_params = {
            "path": secret_path if secret_path else self._secret_path,
            "mount_point": mount_point if mount_point else self._mount_point,
        }

        response = self._vault.secrets.kv.v1.read_secret(**request_params)

        return list(response["data"].keys())
