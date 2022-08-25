from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Callable

from pydantic import BaseConfig as PydanticBaseConfig
from pydantic import BaseSettings as PydanticBaseSettings
from pydantic.env_settings import SettingsError
from pydantic.utils import deep_update

from sitri.providers.base import ConfigProvider


class BaseConfig(PydanticBaseConfig):
    """BaseConfig."""

    provider: type[ConfigProvider] | ConfigProvider


class BaseLocalModeConfig(BaseConfig):
    """BaseLocalModeConfig."""

    provider: type[ConfigProvider] | ConfigProvider

    local_mode: bool | None


class BaseSettings(ABC, PydanticBaseSettings):
    """BaseSettings."""

    def fill(self, call: Callable[[Any], Any], *args: Any, **kwargs: Any) -> Any:
        """fill.

        :param call:
        :type call: Callable
        """
        data = self.dict()
        return call(**data)

    def _build_complex_value(self, value: str | bytes | bytearray, path: str) -> Any:
        """_build_complex_value.

        :param value:
        :type value: Union[str, bytes, bytearray]
        :param path:
        :type path: str
        """
        if isinstance(value, str) or isinstance(value, bytes) or isinstance(value, bytearray):
            try:
                value = self.__config__.json_loads(value)
            except ValueError as e:
                raise SettingsError(f"Error parsing for variable {path}") from e

        return value

    def _build_values(
        self,
        init_kwargs: dict[str, Any],
        _env_file: Path | str | None = None,
        _env_file_encoding: str | None = None,
        _env_nested_delimiter: str | None = None,
        _secrets_dir: Path | str | None = None,
    ) -> dict[str, Any]:
        """_build_values.

        :param init_kwargs:
        :type init_kwargs: Dict[str, Any]
        :param _env_file:
        :type _env_file: Union[Path, str, None]
        :param _env_file_encoding:
        :type _env_file_encoding: Optional[str]
        :param _env_nested_delimiter:
        :type _env_nested_delimiter: Optional[str]
        :param _secrets_dir:
        :type _secrets_dir: Union[Path, str, None]
        :rtype: Dict[str, Any]
        """
        return deep_update(
            deep_update(self._build_default()),
            init_kwargs,
        )

    @abstractmethod
    def _build_default(self, *args: Any, **kwargs: Any) -> dict[str, Any]:
        """_build_default.

        :param args:
        :param kwargs:
        :rtype: Dict[str, Any]
        """
        pass

    __config__: type[BaseConfig]


class BaseLocalModeSettings(BaseSettings):
    """BaseLocalModeSettings."""

    @property
    @abstractmethod
    def local_provider(self) -> type[ConfigProvider] | ConfigProvider:
        """local_provider.

        :rtype: Union[Type[ConfigProvider], ConfigProvider]
        """
        pass

    @abstractmethod
    def _build_local(self, *args: Any, **kwargs: Any) -> dict[str, Any]:
        """_build_local.

        :param args:
        :param kwargs:
        :rtype: Dict[str, Any]
        """
        pass

    def _build_values(
        self,
        init_kwargs: dict[str, Any],
        _env_file: Path | str | None = None,
        _env_file_encoding: str | None = None,
        _env_nested_delimiter: str | None = None,
        _secrets_dir: Path | str | None = None,
    ) -> dict[str, Any]:
        """_build_values.

        :param init_kwargs:
        :type init_kwargs: Dict[str, Any]
        :param _env_file:
        :type _env_file: Union[Path, str, None]
        :param _env_file_encoding:
        :type _env_file_encoding: Optional[str]
        :param _env_nested_delimiter:
        :type _env_nested_delimiter: Optional[str]
        :param _secrets_dir:
        :type _secrets_dir: Union[Path, str, None]
        :rtype: Dict[str, Any]
        """
        if not self.__config__.local_mode:
            return deep_update(
                deep_update(self._build_default()),
                init_kwargs,
            )
        else:
            return deep_update(deep_update(self._build_local()), init_kwargs)

    __config__: type[BaseLocalModeConfig]
