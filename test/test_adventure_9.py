import pytest
from adventure import selection_sort  # Assuming student's code is in adventure.py

def test_selection_sort_duplicates_and_negatives():
    """Tests if selection_sort handles lists with duplicate and negative values."""
    values = [5, -2, 4, 1, -8, 4, 0]
    expected_sorted = [-8, -2, 0, 1, 4, 4, 5]
    assert selection_sort(values) == expected_sorted
