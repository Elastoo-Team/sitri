from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Callable, Dict, Optional, Type, Union

from pydantic import BaseConfig
from pydantic import BaseSettings as PydanticBaseSettings

from sitri.providers.base import ConfigProvider


class BaseMetaConfig(BaseConfig):
    provider: Type[ConfigProvider]
    local_mode: Optional[bool]
    local_provider_factory: Optional[Callable[[], Type[ConfigProvider]]]


class BaseSettings(ABC, PydanticBaseSettings):
    @property
    def local_provider(self):
        _local_provider = getattr(self, "_local_provider", None)

        if not _local_provider:
            _local_provider = self.__config__.local_provider_factory()
            setattr(self, "_local_provider", self.__config__.local_provider_factory())  # noqa

        return _local_provider

    @abstractmethod
    def _build_values(
        self,
        init_kwargs: Dict[str, Any],
        _env_file: Union[Path, str, None] = None,
        _env_file_encoding: Optional[str] = None,
        _secrets_dir: Union[Path, str, None] = None,
    ) -> Dict[str, Any]:
        pass

    __config__: Type[BaseMetaConfig]
