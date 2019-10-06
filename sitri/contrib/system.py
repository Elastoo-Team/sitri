import os
import typing

from ..config.providers import ConfigProvider
from ..credentials.providers import CredentialProvider


class SystemCredentialProvider(CredentialProvider):
    _project_prefix = "system"
    provider_code = "system"

    def __init__(self, project_prefix: str):
        self._project_prefix = project_prefix.upper()

    def prefixize(self, varname: str) -> str:
        return f"{self._project_prefix}_{varname.upper()}"

    def get(self, key: str) -> typing.Union[str, None]:
        return os.getenv(self.prefixize(key), None)


class SystemConfigProvider(ConfigProvider):
    _project_prefix = "system"
    provider_code = "system"

    def __init__(self, project_prefix: str):
        self._project_prefix = project_prefix.upper()

    def prefixize(self, varname: str) -> str:
        return f"{self._project_prefix}_{varname.upper()}"

    def get(self, key: str) -> typing.Union[str, None]:
        return os.getenv(self.prefixize(key), None)

    def keys(self) -> typing.List[str]:
        var_list = []

        for var in os.environ:
            if self._project_prefix in var:
                var_list.append(var)

        return var_list
