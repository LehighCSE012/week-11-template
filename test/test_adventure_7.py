import pytest
from adventure import binary_search

# Test 4: Binary Search - Target Not Found
def test_binary_search_target_not_present_in_sorted_list():
    """Tests if binary_search returns None when the target is not in the sorted list."""
    # IMPORTANT: Input list MUST be sorted
    scroll_ids = [101, 153, 244, 512, 842, 1024, 1500]
    target = 600 # Value between existing elements
    assert binary_search(scroll_ids, target) is None
