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

    def get_variable(self, name: str) -> typing.Union[str, None]:
        result = self._redis.get(self.prefixize(name))

        if isinstance(result, bytes):
            try:
                return result.decode()
            except Exception:
                return None

    def get_variables_list(self) -> typing.List[str]:
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

    def get_credential(self, identifier: str) -> typing.Any:
        result = self._redis.get(self.prefixize(identifier))

        if not isinstance(result, bytes):
            try:
                return result.decode()
            except Exception:
                return None
