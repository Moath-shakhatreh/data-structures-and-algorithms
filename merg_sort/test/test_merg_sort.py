import pytest 
from merg_Sort import merge_sort

def test_the_default_array():
    default_array_array = [8, 4, 23, 42, 16, 15]
    sorted_array = merge_sort(default_array_array)
    assert sorted_array == [4, 8, 15, 16, 23, 42]

def test_reverse_sorted():
    reversed_array = [20,18,12,8,5,-2]
    sorted_array = merge_sort(reversed_array)
    assert sorted_array == [-2, 5, 8, 12, 18, 20]

def test_Few_uniques():
    Few_uniques_array = [5,12,7,5,5,7]
    sorted_array = merge_sort(Few_uniques_array)
    assert sorted_array == [5,5,5,7,7,12]

def test_Nearl_sorteds_array():
    Nearl_sorteds_array = [2,3,5,7,13,11]
    sorted_array = merge_sort(Nearl_sorteds_array)
    assert sorted_array == [2,3,5,7,11,13]