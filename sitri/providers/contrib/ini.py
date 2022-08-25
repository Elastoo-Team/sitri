from __future__ import annotations

import configparser
import os
import typing as t

from sitri.providers.base import ConfigProvider


class IniConfigProvider(ConfigProvider):
    """Config provider for Initialization file (Ini)."""

    provider_code = "ini"

    def __init__(self, ini_path: str = "./config.ini", *args: t.Any, **kwargs: t.Any) -> None:
        """

        :param ini_path: path to ini file
        """
        super().__init__(*args, **kwargs)

        self.configparser = configparser.ConfigParser()

        with open(os.path.abspath(ini_path)) as f:
            self.configparser.read_file(f)

        self._sections = None

    @property
    def sections(self) -> t.List[str]:
        """sections."""
        if not self._sections:
            self._sections = list(self.configparser.keys())  # type: ignore

        return self._sections

    def get(self, key: str, section: str, **kwargs: t.Any) -> t.Any | None:  # type: ignore
        """Get value from ini file.

        :param key: key or path for search
        :param section: section of ini file
        """
        if section not in self.sections:
            return None

        return self.configparser[section].get(key)

    def keys(self, section: str, **kwargs: t.Any) -> t.List[str]:  # type: ignore
        """Get keys of section.

        :param section: section of ini file
        """
        if section not in self.sections:
            return []

        return list(self.configparser[section].keys())
