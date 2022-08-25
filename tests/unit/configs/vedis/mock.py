from __future__ import annotations

import os
import typing as t

import vedis


class VedisMock:
    """VedisMock."""

    _env = os.environ

    def get(self, key: str) -> bytes | None:
        """get.

        :param key:
        :type key: str
        :rtype: bytes | None
        """
        result = self._env.get(key)

        if result:
            return bytes(result, encoding="utf-8")
        else:
            return None

    def keys(self) -> t.List[bytes]:
        """keys.

        :rtype: t.List[bytes]
        """
        return [bytes(key, encoding="utf-8") for key in self._env.keys()]

    def __instancecheck__(self, instance: t.Any) -> bool:
        """__instancecheck__.

        :param instance:
        """
        return isinstance(instance, vedis.Vedis)

    def Hash(self, name: str) -> VedisMock:
        """Hash.

        :param name:
        :type name: str
        :rtype: "VedisMock"
        """
        return self
