import pytest

from oop.classes import Matrix


def test_matrix():
    initial_array = [
        [55, 14, 25, 52, 21],
        [44, 31, 11, 53, 43],
        [24, 13, 45, 12, 34],
        [42, 22, 43, 32, 41],
        [51, 23, 33, 54, 15]
    ]
    target_result = [11, 55, 15, 21, 44, 32, 13, 25, 43]

    matrix = Matrix(initial_array)
    result = matrix.find_treasure()

    assert result == target_result
