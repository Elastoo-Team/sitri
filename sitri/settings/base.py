from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Callable, Dict, Optional, Type, Union

from pydantic import BaseConfig as PydanticBaseConfig
from pydantic import BaseSettings as PydanticBaseSettings
from pydantic.env_settings import SettingsError
from pydantic.utils import deep_update

from sitri.providers.base import ConfigProvider


class BaseConfig(PydanticBaseConfig):
    provider: Type[ConfigProvider]


class BaseLocalModeConfig(BaseConfig):
    provider: Type[ConfigProvider]

    local_mode: Optional[bool]


class BaseSettings(ABC, PydanticBaseSettings):
    def fill(self, call: Callable):
        data = self.dict()
        return call(**data)

    def _build_complex_value(self, value: Union[str, bytes, bytearray], path: str):
        if isinstance(value, str) or isinstance(value, bytes) or isinstance(value, bytearray):
            try:
                value = self.__config__.json_loads(value)  # type: ignore
            except ValueError as e:
                raise SettingsError(f"Error parsing for variable {path}") from e

        return value

    def _build_values(
        self,
        init_kwargs: Dict[str, Any],
        _env_file: Union[Path, str, None] = None,
        _env_file_encoding: Optional[str] = None,
        _secrets_dir: Union[Path, str, None] = None,
    ) -> Dict[str, Any]:
        return deep_update(
            deep_update(self._build_default()),
            init_kwargs,
        )

    @abstractmethod
    def _build_default(self, *args, **kwargs) -> Dict[str, Any]:
        pass

    __config__: Type[BaseConfig]


class BaseLocalModeSettings(BaseSettings):
    @property
    @abstractmethod
    def local_provider(self) -> Type[ConfigProvider]:
        pass

    @abstractmethod
    def _build_local(self, *args, **kwargs) -> Dict[str, Any]:
        pass

    def _build_values(
        self,
        init_kwargs: Dict[str, Any],
        _env_file: Union[Path, str, None] = None,
        _env_file_encoding: Optional[str] = None,
        _secrets_dir: Union[Path, str, None] = None,
    ) -> Dict[str, Any]:
        if not self.__config__.local_mode:
            return deep_update(
                deep_update(self._build_default()),
                init_kwargs,
            )
        else:
            return deep_update(deep_update(self._build_local()), init_kwargs)

    __config__: Type[BaseLocalModeConfig]
