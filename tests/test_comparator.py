from coding_challenge.sort.comparator import Comparator


def test_greater_than():
    assert Comparator.greater_than(5, 4)
    assert not Comparator.greater_than(5, 5)
    assert not Comparator.greater_than(1, 7)


def test_less_or_equal():
    assert Comparator.less_or_equal(4, 5)
    assert Comparator.less_or_equal(5, 5)
    assert not Comparator.less_or_equal(7, 5)
