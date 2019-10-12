import pytest

from sitri.strategy.single import SingleStrategy

from .mock import MockProvider


@pytest.fixture(scope="module")
def test_mock_provider():
    return MockProvider(json_path="tests/unit/strategy/single/data.json")


@pytest.fixture
def test_single_strategy(test_mock_provider):
    return SingleStrategy(test_mock_provider)
