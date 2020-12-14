import pytest

from sitri.providers.contrib.ini import IniConfigProvider


@pytest.fixture(scope="module")
def path_to_ini() -> str:
    return "tests/unit/configs/ini/test.ini"


@pytest.fixture(scope="module")
def ini_config(path_to_init) -> IniConfigProvider:
    return IniConfigProvider(ini_path=path_to_init)
