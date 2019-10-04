import os
import typing

import redis


class RedisMock:

    _env = os.environ

    def get(self, key: str) -> typing.Optional[bytes]:
        result = self._env.get(key)

        if result:
            return bytes(result, encoding="utf-8")
        else:
            return None

    def keys(self) -> typing.List[bytes]:
        return [bytes(key, encoding="utf-8") for key in self._env.keys()]

    def __instancecheck__(self, instance):
        return isinstance(instance, redis.Redis)
