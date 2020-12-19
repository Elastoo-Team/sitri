from typing import Dict, Optional, Union

from hvac.exceptions import VaultError
from loguru import logger
from pydantic import Field
from pydantic.main import BaseModel

from sitri.providers.contrib.json import JsonConfigProvider
from sitri.providers.contrib.vault import VaultKVConfigProvider
from sitri.settings.base import BaseLocalModeConfig, BaseLocalModeSettings


class VaultKVLocalProviderArgs(BaseModel):
    json_path: str = Field(...)
    default_path_mode_state: bool = Field(default=True)


class VaultKVSettings(BaseLocalModeSettings):
    @property
    def _local_provider_args(self):
        args = self.__config__.local_provider_args
        if args:
            if isinstance(args, dict):
                args = VaultKVLocalProviderArgs(**args)

        return args

    @property
    def local_provider(self) -> JsonConfigProvider:
        if not self.__config__.local_provider:
            args = self._local_provider_args

            if args:
                self.__config__.local_provider = JsonConfigProvider(
                    json_path=args.json_path, default_path_mode_state=args.default_path_mode_state
                )
            else:
                raise ValueError("Local provider arguments not found for local mode")

        return self.__config__.local_provider

    def _build_local(self):
        d: Dict[str, Optional[str]] = {}

        for field in self.__fields__.values():
            value: Optional[str] = None

            if self.__config__.local_mode_path_prefix:
                path = f"{self.__config__.local_mode_path_prefix}{self.local_provider.separator}{field.name}"

            else:
                path = field.name

            try:
                value = self.local_provider.get(key=path)
            except VaultError:
                logger.opt(exception=True).warning(f"Could not get local variable {path}")

            if field.is_complex():
                value = self._build_complex_value(value, path)

            if value is None and field.default is not None:
                value = field.default

            d[field.name] = value

        return d

    def _build_default(self):
        d: Dict[str, Optional[str]] = {}

        provider = self.__config__.provider

        for field in self.__fields__.values():
            vault_val: Optional[str] = None

            vault_secret_path = field.field_info.extra.get("vault_secret_path")
            vault_mount_point = field.field_info.extra.get("vault_mount_point")
            vault_secret_key = field.field_info.extra.get("vault_secret_key")

            if vault_secret_key is None:
                vault_secret_key = field.name

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

            if field.is_complex():
                vault_val = self._build_complex_value(
                    vault_val, f"{vault_mount_point}/{vault_secret_path}:{vault_secret_key}"
                )

            if vault_val is None and field.default is not None:
                vault_val = field.default

            d[field.name] = vault_val

        return d

    class VaultKVSettingsConfig(BaseLocalModeConfig):
        provider: VaultKVConfigProvider
        default_secret_path: Optional[str] = None
        default_mount_point: Optional[str] = None

        local_mode: bool = False

        local_mode_path_prefix: Optional[str] = None
        local_provider_args: Optional[Union[VaultKVLocalProviderArgs, Dict]]

        local_provider: JsonConfigProvider = None

    __config__: VaultKVSettingsConfig
