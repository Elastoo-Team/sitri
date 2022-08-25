import os
from typing import Any

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

    def keys(self) -> list[bytes]:
        """keys.

        :rtype: list[bytes]
        """
        return [bytes(key, encoding="utf-8") for key in self._env.keys()]

    def __instancecheck__(self, instance: Any) -> bool:
        """__instancecheck__.

        :param instance:
        """
        return isinstance(instance, vedis.Vedis)

    def Hash(self, name: str) -> "VedisMock":
        """Hash.

        :param name:
        :type name: str
        :rtype: "VedisMock"
        """
        return self
