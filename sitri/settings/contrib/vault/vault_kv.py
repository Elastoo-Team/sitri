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
            deep_update(self._build_vault(), self._build_environ(_env_file)),
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

            if vault_secret_key is None:
                vault_secret_key = field.name

            try:
                vault_val = provider.get(
                    key=vault_secret_key, secret_path=vault_secret_path, vault_mount_point=vault_mount_point
                )
            except VaultError:
                logger.opt(exception=True).warning(
                    f'Could not get secret "{vault_mount_point}/{vault_secret_path}:{vault_secret_key}"'
                )

            if field.is_complex():
                try:
                    vault_val = self.__config__.json_loads(vault_val)  # type: ignore
                except ValueError as e:
                    raise SettingsError(
                        f'Error parsing JSON for "{vault_mount_point}/{vault_secret_path}:{vault_secret_key}"'
                    ) from e

            d[field.alias] = vault_val

        return d

    class Config(BaseMetaConfig):
        provider: VaultKVConfigProvider

    __config__: Config
