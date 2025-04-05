import pytest
from adventure import selection_sort  # Assuming student's code is in adventure.py

# Test 7: Selection Sort - Original List Unchanged
def test_selection_sort_does_not_modify_original_list():
    """Tests that selection_sort returns a new sorted list and leaves the original unchanged."""
    original_list = [3, 1, 4, 2]
    original_copy = original_list[:] # Create a shallow copy for comparison
    
    # Call the function
    sorted_list = selection_sort(original_list)
    
    # Assert the returned list is sorted (optional, covered by other tests)
    assert sorted_list == [1, 2, 3, 4] 
    # Assert the original list remains unchanged
    assert original_list == original_copy
    # Also check that the returned list is a different object (new list)
    assert id(original_list) != id(sorted_list)
