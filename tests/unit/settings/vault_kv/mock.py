import typing

import hvac


class VaultClientMock:

    _env: typing.Dict[str, typing.Any] = {}

    def read_secret(self, mount_point: str, path: str) -> typing.Optional[typing.Any]:
        print(mount_point, path, self._env.get(mount_point, {}).get(path))
        return self._env.get(mount_point, {}).get(path)

    def __instancecheck__(self, instance):
        return isinstance(instance, hvac.Client)

    def __getattribute__(self, item) -> typing.Any:
        if item in ("secrets", "kv", "v1"):
            return self

        return super().__getattribute__(item)
