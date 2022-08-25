from __future__ import annotations

from sitri.strategy.index_priority import IndexPriorityStrategy

from .mock import MockProvider


def test_get_equal(
    test_index_priority_strategy: IndexPriorityStrategy,
    test_mock_provider1: MockProvider,
    test_mock_provider2: MockProvider,
) -> None:
    """test_get_equal.

    :param test_index_priority_strategy:
    :param test_mock_provider1:
    :param test_mock_provider2:
    """
    assert test_mock_provider1.get("test") == test_index_priority_strategy.get("test")
    assert test_mock_provider1.get("test.test_key1", path_mode=True) == test_index_priority_strategy.get(
        "test.test_key1",
        path_mode=True,
    )
    assert test_mock_provider2.get("test.test_key4", path_mode=True) == test_index_priority_strategy.get(
        "test.test_key4",
        path_mode=True,
    )


def test_get(
    test_index_priority_strategy: IndexPriorityStrategy,
    test_mock_provider1: MockProvider,
    test_mock_provider2: MockProvider,
) -> None:
    """test_get.

    :param test_index_priority_strategy:
    :param test_mock_provider1:
    :param test_mock_provider2:
    """
    assert test_mock_provider1.get("test.test_key1", path_mode=True) == test_index_priority_strategy.get(
        "test.test_key1",
        path_mode=True,
    )
    assert test_mock_provider2.get("test.test_key4", path_mode=True) == test_index_priority_strategy.get(
        "test.test_key4",
        path_mode=True,
    )
