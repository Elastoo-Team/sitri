import pytest

from sitri.strategy.index_priority import IndexPriorityStrategy

from .mock import MockProvider


@pytest.fixture(scope="module")
def test_mock_provider1():
    return MockProvider(json_path="tests/unit/strategy/index_priority/data.json")


@pytest.fixture(scope="module")
def test_mock_provider2():
    return MockProvider(json_path="tests/unit/strategy/index_priority/data_one.json")


@pytest.fixture
def test_index_priority_strategy(test_mock_provider1, test_mock_provider2):
    return IndexPriorityStrategy((test_mock_provider1, test_mock_provider2))
