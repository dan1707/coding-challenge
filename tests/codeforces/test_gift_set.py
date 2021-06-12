from coding_challenge.codeforces.gift_set import max_possible_gift_sets


def test_max_possible_gift_sets():
    result = max_possible_gift_sets(10, 12, 5, 2)
    assert 3 == result

    result = max_possible_gift_sets(1, 1, 2, 2)
    assert 0 == result

    result = max_possible_gift_sets(52, 311, 13, 27)
    assert 4 == result

    result = max_possible_gift_sets(1000000000, 1000000000, 1, 1)
    assert 1000000000 == result

    result = max_possible_gift_sets(1000000000, 1, 1, 1000000000)
    assert 1 == result

    result = max_possible_gift_sets(1, 1000000000, 1000000000, 1)
    assert 1 == result

    result = max_possible_gift_sets(1, 2, 1, 1)
    assert 1 == result

    result = max_possible_gift_sets(7, 8, 1, 2)
    assert 5 == result

    result = max_possible_gift_sets(4, 1, 2, 3)
    assert 0 == result
