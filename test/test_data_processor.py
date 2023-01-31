from src.data_processor import get_range_and_frequency

def test_get_range_and_frequency():
    test_data =  [4, 5]
    [expected_min, expected_max, expected_freq] = [(4,5,2)]
    output = get_range_and_frequency(test_data)
    for (min_val, max_val, freq) in output:
        assert(min_val == expected_min)
        assert(max_val == expected_max)
        assert(freq == expected_freq)

