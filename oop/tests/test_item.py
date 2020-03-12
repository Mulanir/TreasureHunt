import pytest

from oop.classes import Item


def test_item():
    initial_value = 34
    target_result = (3, 4)

    item = Item(initial_value)

    assert item.direction == target_result
