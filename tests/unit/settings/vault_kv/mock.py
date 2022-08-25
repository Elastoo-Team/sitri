from __future__ import annotations

import typing as t

import hvac


class VaultClientMock:
    """VaultClientMock."""

    _env: t.Dict[str, t.Any] = {}

    def read_secret(self, mount_point: str, path: str) -> t.Any | None:
        """read_secret.

        :param mount_point:
        :type mount_point: str
        :param path:
        :type path: str
        :rtype: t.Any | None
        """

        return self._env.get(mount_point, {}).get(path)

    def __instancecheck__(self, instance: t.Any) -> bool:
        """__instancecheck__.

        :param instance:
        """
        return isinstance(instance, hvac.Client)

    def __getattribute__(self, item: str) -> t.Any:
        """__getattribute__.

        :param item:
        :rtype: t.Any
        """
        if item in ("secrets", "kv", "v1"):
            return self

        return super().__getattribute__(item)
