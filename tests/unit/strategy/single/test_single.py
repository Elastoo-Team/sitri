def test_get_equal(test_mock_provider, test_single_strategy):
    assert test_mock_provider.get("test") == test_single_strategy.get("test")
    assert test_mock_provider.get("test.test_key1", path_mode=True) == test_single_strategy.get(
        "test.test_key1", path_mode=True
    )
