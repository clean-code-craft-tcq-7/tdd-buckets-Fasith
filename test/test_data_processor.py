import pytest

from src.data_processor import get_range_and_frequency



test_data = [
    {
        "input" : [4,5],
        "output" : [(4,5,2)]
    },
    {
        "input" : [3, 3, 5, 4, 10, 11, 12],
        "output" : [(3,5,4), (10,12,3)]
    }
]


def test_get_range_and_frequency():
    for data in test_data:
        expected_output = data["output"]
        output = get_range_and_frequency(data["input"])
        for (min_val, max_val, freq), (expected_min, expected_max, expected_freq) in zip(output,expected_output):
            assert(min_val == expected_min)
            assert(max_val == expected_max)
            assert(freq == expected_freq)

