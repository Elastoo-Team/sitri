import typing

from loguru import logger

from ..config.providers import ConfigProvider


class ConsulConfigProvider(ConfigProvider):
    """Provider for HashiCorp Consul config storage."""

    provider_code = "consul"
    folder: str

    def __init__(self, consul_connector: typing.Callable, folder: str = "sitri/") -> None:
        """

        :param consul_connector: function return connection to Consul
        :param folder: consul folder with config vars
        """
        self._consul_get = consul_connector
        self.folder = folder

    @property
    def _consul(self):
        return self._consul_get()

    @logger.catch(level="ERROR")
    def get(self, key: str, **kwargs) -> typing.Optional[typing.Any]:
        """Get value from consul by key.

        :param key: key from consul folder
        """
        index, data = self._consul.kv.get(f"{self.folder}{key}" if self.folder not in key else key)

        if data and data["Value"]:
            return data["Value"].decode()

        return None

    @logger.catch(level="ERROR")
    def keys(self) -> typing.List[typing.Any]:
        """Get keys list from consul folder."""
        index, data = self._consul.kv.get(self.folder, recurse=True)
        var_list = []

        if data:
            for var in data:
                if var["Value"]:
                    var_list.append(var["Key"])

        return var_list
