import pytest

from functional.functions import get_treasure_solver


def test_matrix():
    initial_array = [
        [55, 14, 25, 52, 21],
        [44, 31, 11, 53, 43],
        [24, 13, 45, 12, 34],
        [42, 22, 43, 32, 41],
        [51, 23, 33, 54, 15]
    ]
    target_result = [11, 55, 15, 21, 44, 32, 13, 25, 43]

    treasure_solver = get_treasure_solver(initial_array)
    result = treasure_solver()

    assert result == target_result
