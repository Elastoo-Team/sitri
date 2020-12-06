from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, Optional, Type, Union

from pydantic import BaseConfig
from pydantic import BaseSettings as PydanticBaseSettings

from sitri.providers.base import ConfigProvider


class BaseMetaConfig(BaseConfig):
    provider: Type[ConfigProvider]


class BaseSettings(ABC, PydanticBaseSettings):
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
