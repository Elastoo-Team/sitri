import os
import typing

from ..config.providers import ConfigProvider
from ..credentials.providers import CredentialProvider


class SystemCredentialProvider(CredentialProvider):
    """Provider for get credentials from system environment."""

    _prefix: str = "system"
    provider_code: str = "system"

    def __init__(self, prefix: str):
        """
        :param prefix: prefix for create "namespace" for project variables in environment
        """
        self._prefix = prefix.upper()

    def prefixize(self, key: str) -> str:
        """Get key with prefix.

        :param key: varname without prefix
        """
        return f"{self._prefix}_{key.upper()}"

    def get(self, key: str, **kwargs) -> typing.Union[str, None]:
        """Get config variable from system env.

        :param key: key without prefix from env
        """
        return os.getenv(self.prefixize(key), None)


class SystemConfigProvider(ConfigProvider):
    """Provider for get config from system environment."""

    _prefix = "system"
    provider_code = "system"

    def __init__(self, prefix: str):
        """
        :param prefix: prefix for create "namespace" for project variables in environment
        """
        self._prefix = prefix.upper()

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

    def get(self, key: str, **kwargs) -> typing.Union[str, None]:
        """Get value from system env.

        :param key: key without prefix from env
        """
        return os.getenv(self.prefixize(key), None)

    def keys(self) -> typing.List[str]:
        """Get keys list with prefix from system env."""
        var_list = []

        for var in os.environ:
            if self._prefix in var:
                var_list.append(self.unprefixize(var))

        return var_list
