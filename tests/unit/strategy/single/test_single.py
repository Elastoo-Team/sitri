from __future__ import annotations

from sitri.strategy.single import SingleStrategy

from .mock import MockProvider


def test_get_equal(test_mock_provider: MockProvider, test_single_strategy: SingleStrategy) -> None:
    """test_get_equal.

    :param test_mock_provider:
    :param test_single_strategy:
    """
    assert test_mock_provider.get("test") == test_single_strategy.get("test")
    assert test_mock_provider.get("test.test_key1", path_mode=True) == test_single_strategy.get(
        "test.test_key1",
        path_mode=True,
    )
