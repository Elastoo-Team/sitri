from __future__ import annotations

import typing

import vedis

from sitri.providers.base import ConfigProvider


class VedisConfigProvider(ConfigProvider):
    """Config provider for vedis storage."""

    provider_code = "vedis"
    _hash_name = "sitri_config_hash"

    def __init__(
        self,
        vedis_connector: typing.Callable[[], vedis.Vedis],
        hash_name: str = "sitri_config_hash",
        *args: typing.Any,
        **kwargs: typing.Any,
    ) -> None:
        """

        :param vedis_connector: return connection to vedis
        :param hash_name: name for hash (key-value object) in vedis
        """
        super().__init__(*args, **kwargs)

        self._vedis_get = vedis_connector
        self._hash_name = hash_name
        self._vedis_instance = None

    @property
    def _vedis(self) -> vedis.Vedis:
        """_vedis.

        :rtype: vedis.Vedis
        """
        if not self._vedis_instance:
            self._vedis_instance = self._vedis_get()

        return self._vedis_instance

    @property
    def _config_hash(self) -> typing.Any:
        """_config_hash."""
        return self._vedis.Hash(self._hash_name)

    def get(self, key: str, **kwargs: typing.Any) -> str | None:
        """get.

        :param key:
        :type key: str
        :param kwargs:
        :rtype: typing.Optional[str]
        """
        result = self._config_hash.get(key)

        if isinstance(result, bytes):
            return result.decode()

        return None

    def keys(self, **kwargs: typing.Any) -> list[str]:
        """keys.

        :param kwargs:
        :rtype: typing.List[str]
        """
        var_list = []
        variables = self._config_hash.keys() if self._config_hash.keys() is not None else []

        for var in variables:
            var_list.append(var.decode())

        return var_list
