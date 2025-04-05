import pytest
from adventure import linear_search, binary_search, selection_sort

# Test 1: Linear Search - Target Found
def test_linear_search_finds_target():
    """Tests if linear_search returns the correct index when the target exists."""
    artifacts = ["Golden Idol", "Crystal Skull", "Sunstone", "Ancient Vase", "Jeweled Dagger"]
    target = "Sunstone"
    expected_index = 2
    assert linear_search(artifacts, target) == expected_index
