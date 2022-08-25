import typing

import hvac


class VaultClientMock:
    """VaultClientMock."""

    _env: dict[str, typing.Any] = {}

    def read_secret(self, mount_point: str, path: str) -> typing.Any | None:
        """read_secret.

        :param mount_point:
        :type mount_point: str
        :param path:
        :type path: str
        :rtype: typing.Any | None
        """
        print(mount_point, path)
        return self._env.get(mount_point, {}).get(path)

    def __instancecheck__(self, instance: typing.Any) -> bool:
        """__instancecheck__.

        :param instance:
        """
        return isinstance(instance, hvac.Client)

    def __getattribute__(self, item: str) -> typing.Any:
        """__getattribute__.

        :param item:
        :rtype: typing.Any
        """
        if item in ("secrets", "kv", "v1"):
            return self

        return super().__getattribute__(item)
