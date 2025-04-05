# test_temple_explorer.py
import pytest
from adventure import linear_search, binary_search, selection_sort

# Test 3: Binary Search - Target Found (Middle)
def test_binary_search_finds_target_in_sorted_list():
    """Tests if binary_search returns the correct index for a target in a sorted list."""
    # IMPORTANT: Input list MUST be sorted for binary_search
    scroll_ids = [101, 153, 244, 512, 842, 1024, 1500]
    target = 842
    expected_index = 4
    assert binary_search(scroll_ids, target) == expected_index
