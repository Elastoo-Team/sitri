import typing

import redis

from sitri.providers.base import ConfigProvider


class RedisConfigProvider(ConfigProvider):
    """Config provider for redis storage."""

    provider_code = "redis"
    _prefix = "redis"

    def __init__(self, prefix: str, redis_connector: typing.Callable[[], redis.Redis], *args, **kwargs):
        """

        :param prefix: prefix for create "namespace" for project variables in redis
        :param redis_connector: function return connection to Redis
        """
        super().__init__(*args, **kwargs)

        self._prefix = prefix.upper()
        self._redis_get = redis_connector

        self._redis_instance: typing.Optional[redis.Redis] = None

    @property
    def _redis(self) -> redis.Redis:
        if not self._redis_instance:
            self._redis_instance = self._redis_get()

        return self._redis_instance

    def prefixize(self, key: str) -> str:
        """Get key with prefix.

        :param key: varname without prefix
        """
        return f"{self._prefix}_{key.upper()}"

    def unprefixize(self, var_name: str) -> str:
        """Remove prefix from variable name.

        :param var_name: variable name
        """

        return var_name.replace(f"{self._prefix}_", "").lower()

    def get(self, key: str, **kwargs) -> typing.Optional[str]:
        result = self._redis.get(self.prefixize(key))

        if isinstance(result, bytes):
            return result.decode()

        return None

    def keys(self, **kwargs) -> typing.List[str]:
        var_list = []

        for var in self._redis.keys():
            if self._prefix in var.decode():
                var_list.append(self.unprefixize(var.decode()))

        return var_list
