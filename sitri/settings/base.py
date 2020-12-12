from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, Optional, Type, Union

from pydantic import BaseConfig
from pydantic import BaseSettings as PydanticBaseSettings

from sitri.providers.base import ConfigProvider


class BaseMetaConfig(BaseConfig):
    provider: Type[ConfigProvider]
    local_mode: Optional[bool]


class BaseSettings(ABC, PydanticBaseSettings):
    @property
    @abstractmethod
    def local_provider(self) -> Type[ConfigProvider]:
        pass

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
