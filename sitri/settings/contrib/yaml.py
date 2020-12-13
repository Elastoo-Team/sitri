from pathlib import Path
from typing import Any, Dict, Optional, Union

from pydantic.env_settings import SettingsError
from pydantic.utils import deep_update

from sitri.providers.contrib.yaml import YamlConfigProvider
from sitri.settings.base import BaseMetaConfig, BaseSettings


class YamlSettings(BaseSettings):
    @property
    def local_provider(self) -> None:
        return None

    def _build_values(
        self,
        init_kwargs: Dict[str, Any],
        _env_file: Union[Path, str, None] = None,
        _env_file_encoding: Optional[str] = None,
        _secrets_dir: Union[Path, str, None] = None,
    ) -> Dict[str, Any]:
        return deep_update(
            deep_update(self._build_yaml()),
            init_kwargs,
        )

    def _build_yaml(self):
        d: Dict[str, Optional[str]] = {}

        provider = self.__config__.provider

        for field in self.__fields__.values():
            key_name: Optional[str] = field.field_info.extra.get("yaml_key_name")
            path_prefix: Optional[str] = field.field_info.extra.get("yaml_path_prefix")

            if key_name is None:
                key_name = field.alias

            if path_prefix is not None:
                key_name = f"{path_prefix}{provider.separator}{key_name}"

            elif self.__config__.default_path_prefix is not None:
                key_name = f"{self.__config__.default_path_prefix}{provider.separator}{key_name}"

            value: Optional[str] = provider.get(key_name)

            if field.is_complex() and (
                isinstance(value, str) or isinstance(value, bytes) or isinstance(value, bytearray)
            ):
                try:
                    value = self.__config__.json_loads(value)  # type: ignore

                except ValueError as e:
                    raise SettingsError(f'Error parsing JSON for "{key_name}"') from e

            if value is None and field.default is not None:
                value = field.default

            d[field.alias] = value

        return d

    class YamlSettingsConfig(BaseMetaConfig):
        provider: YamlConfigProvider

        default_path_prefix: Optional[str] = None

    __config__: YamlSettingsConfig
