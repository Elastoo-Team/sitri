from __future__ import annotations

import typing as t

import hvac
from hvac.api.vault_api_base import VaultApiBase

from sitri.providers.base import ConfigProvider


class VaultKVConfigProvider(ConfigProvider):
    """Config provider for vault_kv storage."""

    provider_code = "vault_kv"

    def __init__(
        self,
        vault_connector: t.Callable[[], hvac.Client],
        mount_point: str | None = None,
        secret_path: str | None = None,
        version: int | None = 1,
        *args: t.Any,
        **kwargs: t.Any,
    ) -> None:
        """
        :param vault_connector: function return connection to Vault
        :param mount_point: default vault_kv storage mount point
        :param secret_path: default path to the secret in mounted
        """
        super().__init__(*args, **kwargs)
        assert version in (1, 2)

        self._vault_get = vault_connector
        self._vault_hvac_instance = None
        self._mount_point = mount_point
        self._secret_path = secret_path
        self._version = version

    @property
    def _vault(self) -> hvac.Client:
        """_vault.

        :rtype: hvac.Client
        """
        if not self._vault_hvac_instance:
            self._vault_hvac_instance = self._vault_get()

        return self._vault_hvac_instance

    @property
    def _vault_kv(self) -> VaultApiBase:
        return self._vault.secrets.kv.v1 if self._version == 1 else self._vault.secrets.kv.v2

    @property
    def _read_secret(self) -> t.Callable[[t.Any], t.Any]:
        return self._vault_kv.read_secret if self._version == 1 else self._vault_kv.read_secret_version

    def _extract_response(self, response: dict[str, t.Any]) -> dict[str, t.Any]:
        return response["data"] if self._version == 1 else response["data"]["data"]

    def get(
        self,
        key: str,
        mount_point: str | None = None,
        secret_path: str | None = None,
        version: int | None = None,
        **kwargs: t.Any,
    ) -> str | None:
        """get.

        :param key: Specifies the secret key to get
        :type key: str
        :param mount_point: The "path" the secret engine was mounted on.
        :type mount_point: t.Optional[str]
        :param secret_path: Specifies the path of the secret to read. This is specified as part of the URL.
        :type secret_path: t.Optional[str]
        :param version: Specifies the version to return. If not set the latest version is returned.
        :type version: t.Optional[int]
        :param kwargs:
        :rtype: t.Optional[str]
        """
        request_params = {
            "path": secret_path if secret_path else self._secret_path,
            "mount_point": mount_point if mount_point else self._mount_point,
        }
        if version is not None:
            request_params["version"] = version  # type: ignore

        response = self._read_secret(**request_params)

        return self._extract_response(response).get(key)

    def keys(self, mount_point: str | None = None, secret_path: str | None = None, **kwargs: t.Any) -> t.List[str]:
        """keys.

        :param mount_point:
        :type mount_point: t.Optional[str]
        :param secret_path:
        :type secret_path: t.Optional[str]
        :param kwargs:
        :rtype: t.List[str]
        """
        request_params = {
            "path": secret_path if secret_path else self._secret_path,
            "mount_point": mount_point if mount_point else self._mount_point,
        }

        response = self._read_secret(**request_params)

        return list(self._extract_response(response).keys())
