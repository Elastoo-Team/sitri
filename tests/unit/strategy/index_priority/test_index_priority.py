def test_get_equal(test_index_priority_strategy, test_mock_provider1, test_mock_provider2):
    assert test_mock_provider1.get("test") == test_index_priority_strategy.get("test")
    assert test_mock_provider1.get("test.test_key1", path_mode=True) == test_index_priority_strategy.get(
        "test.test_key1", path_mode=True
    )
    assert test_mock_provider2.get("test.test_key4", path_mode=True) == test_index_priority_strategy.get(
        "test.test_key4", path_mode=True
    )


def test_get(test_index_priority_strategy, test_mock_provider1, test_mock_provider2):
    assert test_mock_provider1.get("test.test_key1", path_mode=True) == test_index_priority_strategy.get(
        "test.test_key1", path_mode=True
    )
    assert test_mock_provider2.get("test.test_key4", path_mode=True) == test_index_priority_strategy.get(
        "test.test_key4", path_mode=True
    )
