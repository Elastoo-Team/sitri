from __future__ import annotations

import typing as t

from sitri.providers.contrib.yaml import YamlConfigProvider
from sitri.settings.base import BaseConfig, BaseSettings


class YamlSettings(BaseSettings):
    """YamlSettings."""

    def _build_default(self, *args: t.Any, **kwargs: t.Any) -> t.Dict[str, t.Any]:
        """_build_default."""
        d: t.Dict[str, str | None] = {}

        provider = self.__config__.provider

        for field in self.__fields__.values():
            key_name: str | None = field.field_info.extra.get("yaml_key_name")
            path_prefix: str | None = field.field_info.extra.get("yaml_path_prefix")

            if key_name is None:
                key_name = field.name

            if path_prefix is not None:
                key_name = f"{path_prefix}{provider.separator}{key_name}"

            elif self.__config__.default_path_prefix is not None:
                key_name = f"{self.__config__.default_path_prefix}{provider.separator}{key_name}"

            value: str | None = provider.get(key_name)

            if field.is_complex():
                value = self._build_complex_value(value, key_name)

            if value is None and field.default is not None:
                value = field.default

            d[field.name] = value

        return d

    class YamlSettingsConfig(BaseConfig):
        """YamlSettingsConfig."""

        provider: YamlConfigProvider

        default_path_prefix: str | None = None

    __config__: YamlSettingsConfig
