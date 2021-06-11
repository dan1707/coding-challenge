from coding_challenge.sort.mergesort import MergeSort
from coding_challenge.sort.comparator import Comparator


def test_MergeSort_merge():
    left = [1, 3, 5]
    right = [2, 4, 6]
    expected = [1, 2, 3, 4, 5, 6]

    result = MergeSort.merge(left, right, Comparator.less_or_equal)
    assert expected == result


def test_MergeSort_one_element():
    sortable = [9]
    expected = [9]

    result = MergeSort.sort(sortable, Comparator.less_or_equal)

    assert expected == result


def test_MergeSort_sort():
    sortable = [9, 1, 8, 2, 7, 3]
    expected = [1, 2, 3, 7, 8, 9]

    result = MergeSort.sort(sortable, Comparator.less_or_equal)
    assert expected == result
