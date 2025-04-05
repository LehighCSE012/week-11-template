# test_temple_explorer.py
import pytest
from adventure import linear_search, binary_search, selection_sort


# Test 5: Linear Search - Target Not Found
def test_linear_search_target_not_present():
    """Tests if linear_search returns None when the target does not exist."""
    artifacts = ["Golden Idol", "Crystal Skull", "Ancient Vase"]
    target = "Sunstone"
    assert linear_search(artifacts, target) is None
