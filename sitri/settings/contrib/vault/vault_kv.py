from pathlib import Path
from typing import Any, Dict, Optional, Union

from hvac.exceptions import VaultError
from loguru import logger
from pydantic.env_settings import SettingsError
from pydantic.utils import deep_update

from sitri.providers.contrib.vault import VaultKVConfigProvider
from sitri.settings.base import BaseMetaConfig, BaseSettings


class VaultKVSettings(BaseSettings):
    def _build_values(
        self,
        init_kwargs: Dict[str, Any],
        _env_file: Union[Path, str, None] = None,
        _env_file_encoding: Optional[str] = None,
        _secrets_dir: Union[Path, str, None] = None,
    ) -> Dict[str, Any]:
        return deep_update(
            deep_update(self._build_vault()),
            init_kwargs,
        )

    def _build_vault(self):
        d: Dict[str, Optional[str]] = {}

        provider = self.__config__.provider

        for field in self.__fields__.values():
            vault_val: Optional[str] = None

            vault_secret_path = field.field_info.extra.get("vault_secret_path")
            vault_mount_point = field.field_info.extra.get("vault_mount_point")
            vault_secret_key = field.field_info.extra.get("vault_secret_key")
            use_default = field.field_info.extra.get("use_default", False)

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

            if field.is_complex() and (isinstance(vault_val, str) or isinstance(vault_val, bytes)):
                try:
                    vault_val = self.__config__.json_loads(vault_val)  # type: ignore
                except ValueError as e:
                    raise SettingsError(
                        f'Error parsing JSON for "{vault_mount_point}/{vault_secret_path}:{vault_secret_key}"'
                    ) from e

            if vault_val is None and field.default and use_default:
                vault_val = field.default

            d[field.alias] = vault_val

        return d

    class Config(BaseMetaConfig):
        provider: VaultKVConfigProvider
        default_secret_path: Optional[str] = None
        default_mount_point: Optional[str] = None

    __config__: Config
