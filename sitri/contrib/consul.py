import typing

from consul import Consul

from ..config.providers import ConfigProvider


class ConsulConfigProvider(ConfigProvider):
    provider_code = "consul"
    folder: str

    def __init__(self, consul_connection: Consul, folder: str = "sitri/") -> None:
        self._consul = consul_connection
        self.folder = folder

    def get_variable(self, name: str) -> typing.Optional[typing.Any]:
        index, data = self._consul.kv.get(f"{self.folder}{name}" if self.folder not in name else name)

        if data and data["Value"]:
            return data["Value"].decode()

        return None

    def get_variables_list(self) -> typing.List[typing.Any]:
        index, data = self._consul.kv.get(self.folder, recurse=True)
        var_list = []

        for var in data:
            if var["Value"]:
                var_list.append(var["Key"])

        return var_list
