import typing

import vedis

from ..config.providers import ConfigProvider
from ..credentials.providers import CredentialProvider


class VedisConfigProvider(ConfigProvider):
    provider_code = "vedis"
    project_prefix = "vedis"

    def __init__(self, project_prefix: str, vedis_connection: vedis.Vedis):
        self._project_prefix = project_prefix.upper()
        self._vedis = vedis_connection
        self._config_hash = self._vedis.Hash("sitri_config_hash")

    def prefixize(self, varname: str) -> str:
        return f"{self._project_prefix}_{varname.upper()}"

    def get_variable(self, name: str) -> typing.Union[str, None]:
        result = self._config_hash.get(self.prefixize(name))

        if isinstance(result, bytes):
            try:
                return result.decode()
            except Exception:
                return None

    def get_variables_list(self) -> typing.List[str]:
        var_list = []
        vars = self._config_hash.keys() if self._config_hash.keys() is not None else []

        for var in vars:
            if self._project_prefix in var.decode():
                var_list.append(var.decode())

        return var_list


class VedisCredentialProvider(CredentialProvider):
    provider_code = "vedis"
    project_prefix = "vedis"

    def __init__(self, project_prefix: str, vedis_connection: vedis.Vedis):
        self._project_prefix = project_prefix.upper()
        self._vedis = vedis_connection
        self._config_hash = self._vedis.Hash("sitri_config_hash")

    def prefixize(self, varname: str) -> str:
        return f"{self._project_prefix}_{varname.upper()}"

    def get_credential(self, identifier: str) -> typing.Any:
        result = self._config_hash.get(self.prefixize(identifier))

        if isinstance(result, bytes):
            try:
                return result.decode()
            except Exception:
                return None
