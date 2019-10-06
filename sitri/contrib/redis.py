import typing

import redis

from ..config.providers import ConfigProvider
from ..credentials.providers import CredentialProvider


class RedisConfigProvider(ConfigProvider):
    provider_code = "redis"
    project_prefix = "redis"

    def __init__(self, project_prefix: str, redis_connection: redis.Redis):
        self._project_prefix = project_prefix.upper()
        self._redis = redis_connection

    def prefixize(self, varname: str) -> str:
        return f"{self._project_prefix}_{varname.upper()}"

    def get(self, key: str) -> typing.Optional[str]:
        result = self._redis.get(self.prefixize(key))

        if isinstance(result, bytes):
            return result.decode()

        return None

    def keys(self) -> typing.List[str]:
        var_list = []

        for var in self._redis.keys():
            if self._project_prefix in var.decode():
                var_list.append(var.decode())

        return var_list


class RedisCredentialProvider(CredentialProvider):
    provider_code = "redis"
    project_prefix = "redis"

    def __init__(self, project_prefix: str, redis_connection: redis.Redis):
        self._project_prefix = project_prefix.upper()
        self._redis = redis_connection

    def prefixize(self, varname: str) -> str:
        return f"{self._project_prefix}_{varname.upper()}"

    def get(self, key: str) -> typing.Any:
        result = self._redis.get(self.prefixize(key))

        if isinstance(result, bytes):
            return result.decode()
