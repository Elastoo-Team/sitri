from pathlib import Path
from typing import Any, Dict, Optional, Union

from hvac.exceptions import VaultError
from loguru import logger
from pydantic import Field
from pydantic.env_settings import SettingsError
from pydantic.main import BaseModel
from pydantic.utils import deep_update

from sitri.providers.contrib.json import JsonConfigProvider
from sitri.providers.contrib.vault import VaultKVConfigProvider
from sitri.settings.base import BaseMetaConfig, BaseSettings


class VaultKVLocalProviderArgs(BaseModel):
    json_path: str = Field(...)
    default_path_mode_state: bool = Field(default=True)


class VaultKVSettings(BaseSettings):
    @property
    def local_provider(self) -> JsonConfigProvider:
        if not self._local_provider:
            if args := self.__config__.local_provider_args:
                if isinstance(args, dict):
                    args = VaultKVLocalProviderArgs(**args)

                self._local_provider = JsonConfigProvider(
                    json_path=args.json_path, default_path_mode_state=args.default_path_mode_state
                )
            else:
                raise ValueError("Local provider arguments not found for local mode")

        return self._local_provider

    def _build_values(
        self,
        init_kwargs: Dict[str, Any],
        _env_file: Union[Path, str, None] = None,
        _env_file_encoding: Optional[str] = None,
        _secrets_dir: Union[Path, str, None] = None,
    ) -> Dict[str, Any]:
        if not self.__config__.local_mode:
            return deep_update(
                deep_update(self._build_vault()),
                init_kwargs,
            )
        else:
            return deep_update(deep_update(self._build_local()), init_kwargs)

    def _build_local(self):
        d: Dict[str, Optional[str]] = {}

        provider = self.local_provider

        for field in self.__fields__.values():
            value: Optional[str] = None

            if self.__config__.local_mode_path_prefix:
                path = f"{self.__config__.local_mode_path_prefix}.{field.alias}"

            else:
                path = field.alias

            try:
                value = provider.get(key=path, separator=".")
            except VaultError:
                logger.opt(exception=True).warning(f"Could not get local variable {path}")

            if field.is_complex() and (
                isinstance(value, str) or isinstance(value, bytes) or isinstance(value, bytearray)
            ):
                try:
                    value = self.__config__.json_loads(value)  # type: ignore
                except ValueError as e:
                    raise SettingsError(f"Error parsing JSON for variable {path}") from e

            if value is None and field.default is not None:
                value = field.default

            d[field.alias] = value

        return d

    def _build_vault(self):
        d: Dict[str, Optional[str]] = {}

        provider = self.__config__.provider

        for field in self.__fields__.values():
            vault_val: Optional[str] = None

            vault_secret_path = field.field_info.extra.get("vault_secret_path")
            vault_mount_point = field.field_info.extra.get("vault_mount_point")
            vault_secret_key = field.field_info.extra.get("vault_secret_key")

            if vault_secret_key is None:
                vault_secret_key = field.alias

            try:
                vault_val = provider.get(
                    key=vault_secret_key,
                    secret_path=vault_secret_path if vault_secret_path else self.__config__.default_secret_path,
                    mount_point=vault_mount_point if vault_mount_point else self.__config__.default_mount_point,
                )
            except VaultError:
                logger.opt(exception=True).warning(
                    f'Could not get secret "{vault_mount_point}/{vault_secret_path}:{vault_secret_key}"'
                )

            if field.is_complex() and (
                isinstance(vault_val, str) or isinstance(vault_val, bytes) or isinstance(vault_val, bytearray)
            ):
                try:
                    vault_val = self.__config__.json_loads(vault_val)  # type: ignore
                except ValueError as e:
                    raise SettingsError(
                        f'Error parsing JSON for "{vault_mount_point}/{vault_secret_path}:{vault_secret_key}"'
                    ) from e

            if vault_val is None and field.default is not None:
                vault_val = field.default

            d[field.alias] = vault_val

        return d

    class VaultKVSettingsConfig(BaseMetaConfig):
        provider: VaultKVConfigProvider
        default_secret_path: Optional[str] = None
        default_mount_point: Optional[str] = None

        local_mode: bool = False

        local_mode_path_prefix: Optional[str] = None
        local_provider_args: Optional[Union[VaultKVLocalProviderArgs, Dict]]

    __config__: VaultKVSettingsConfig
    _local_provider: JsonConfigProvider
