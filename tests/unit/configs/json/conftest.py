from __future__ import annotations

import json

import pytest

from sitri.providers.contrib.json import JsonConfigProvider


@pytest.fixture(scope="module")
def path_to_json() -> str:
    """path_to_json.

    :rtype: str
    """
    return "tests/unit/configs/json/data.json"


@pytest.fixture(scope="module")
def json_data() -> str:
    """json_data.

    :rtype: str
    """
    data = {"test": {"test_key1": "1", "test_key2": "2", "test_key3": "3"}}

    return json.dumps(data)


@pytest.fixture(scope="module")
def json_config_data(json_data: str) -> JsonConfigProvider:
    """json_config_data.

    :param json_data:
    :rtype: JsonConfigProvider
    """
    return JsonConfigProvider(json_data=json_data, default_separator="/")


@pytest.fixture(scope="module")
def json_config(path_to_json: str) -> JsonConfigProvider:
    """json_config.

    :param path_to_json:
    :rtype: JsonConfigProvider
    """
    return JsonConfigProvider(json_path=path_to_json, default_separator="/")
