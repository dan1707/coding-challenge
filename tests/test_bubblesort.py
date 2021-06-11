from coding_challenge.sort.bubblesort import BubbleSort
from coding_challenge.sort.comparator import Comparator


def test_BubbleSort_sort():
    sortable = [9, 1, 8, 2, 7, 3]
    expected = [1, 2, 3, 7, 8, 9]

    result = BubbleSort.sort(sortable, Comparator.less_or_equal)
    assert expected == result


def test_BubbleSort_sort_reverse():
    sortable = [9, 1, 8, 2, 7, 3]
    expected = [9, 8, 7, 3, 2, 1]

    result = BubbleSort.sort(sortable, Comparator.greater_than)

    assert expected == result


def test_BubbleSort_sort_one_element():
    sortable = [9]
    expected = [9]

    result = BubbleSort.sort(sortable, Comparator.less_or_equal)

    assert expected == result
