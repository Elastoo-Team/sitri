import json

import pytest

from sitri.providers.contrib.json import JsonConfigProvider


@pytest.fixture(scope="module")
def path_to_json() -> str:
    return "tests/unit/configs/json/data.json"


@pytest.fixture(scope="module")
def json_data() -> str:
    data = {"test": {"test_key1": "1", "test_key2": "2", "test_key3": "3"}}

    return json.dumps(data)


@pytest.fixture(scope="module")
def json_config_data(json_data) -> JsonConfigProvider:
    return JsonConfigProvider(json_data=json_data, default_separator="/")


@pytest.fixture(scope="module")
def json_config(path_to_json) -> JsonConfigProvider:
    return JsonConfigProvider(json_path=path_to_json, default_separator="/")
