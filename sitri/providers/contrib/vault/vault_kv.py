from __future__ import annotations

import typing

import hvac

from sitri.providers.base import ConfigProvider


class VaultKVConfigProvider(ConfigProvider):
    """Config provider for vault_kv storage.

    Only for kv first version at the moment.
    """

    provider_code = "vault_kv"

    def __init__(
        self,
        vault_connector: typing.Callable[[], hvac.Client],
        mount_point: str | None = None,
        secret_path: str | None = None,
        *args: typing.Any,
        **kwargs: typing.Any,
    ) -> None:
        """
        :param vault_connector: function return connection to Vault
        :param mount_point: default vault_kv kv1 storage mount point
        :param secret_path: default path to the secret in mounted
        """
        super().__init__(*args, **kwargs)

        self._vault_get = vault_connector
        self._vault_hvac_instance = None
        self._mount_point = mount_point
        self._secret_path = secret_path

    @property
    def _vault(self) -> hvac.Client:
        """_vault.

        :rtype: hvac.Client
        """
        if not self._vault_hvac_instance:
            self._vault_hvac_instance = self._vault_get()

        return self._vault_hvac_instance

    def get(
        self, key: str, mount_point: str | None = None, secret_path: str | None = None, **kwargs: typing.Any
    ) -> str | None:
        """get.

        :param key:
        :type key: str
        :param mount_point:
        :type mount_point: typing.Optional[str]
        :param secret_path:
        :type secret_path: typing.Optional[str]
        :param kwargs:
        :rtype: typing.Optional[str]
        """
        request_params = {
            "path": secret_path if secret_path else self._secret_path,
            "mount_point": mount_point if mount_point else self._mount_point,
        }

        response = self._vault.secrets.kv.v1.read_secret(**request_params)

        return response["data"].get(key)

    def keys(self, mount_point: str | None = None, secret_path: str | None = None, **kwargs: typing.Any) -> list[str]:
        """keys.

        :param mount_point:
        :type mount_point: typing.Optional[str]
        :param secret_path:
        :type secret_path: typing.Optional[str]
        :param kwargs:
        :rtype: typing.List[str]
        """
        request_params = {
            "path": secret_path if secret_path else self._secret_path,
            "mount_point": mount_point if mount_point else self._mount_point,
        }

        response = self._vault.secrets.kv.v1.read_secret(**request_params)

        return list(response["data"].keys())
