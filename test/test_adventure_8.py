import pytest
from adventure import selection_sort  # Assuming student's code is in adventure.py

def test_selection_sort_basic_numeric_list():
    """Tests if selection_sort correctly sorts a simple list of numbers."""
    treasure_values = [150, 20, 80, 500, 10, 95, 300]
    expected_sorted = [10, 20, 80, 95, 150, 300, 500]
    assert selection_sort(treasure_values) == expected_sorted
