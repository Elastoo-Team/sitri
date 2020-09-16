import typing

import consul


class ConsulMock:

    _env: typing.Dict[str, typing.Any] = {}

    def get(self, key: str, recurse=False) -> typing.Tuple[int, typing.Any]:
        if not recurse:
            result = str(self._env.get(key))

            return 0, {"Value": bytes(result, encoding="utf-8")} if result else None
        else:
            keys = self.keys()

            data = []

            for key_ in keys:
                if key in key_:
                    data.append({"Value": self.get(key_)[1].get("Value"), "Key": key_})
            return 0, data

    def keys(self) -> typing.List[str]:
        return list(self._env.keys())

    def __instancecheck__(self, instance):
        return isinstance(instance, consul.Consul)

    def __getattribute__(self, item) -> typing.Any:
        if item == "kv":
            return self

        return super().__getattribute__(item)
