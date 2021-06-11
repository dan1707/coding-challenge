from coding_challenge.number_swap import swap_number


def test_swap_number_positive():
    a = 12
    b = 13
    (a_b, b_a) = swap_number(a, b)
    print(f"a:{a} b:{b} a_b:{a_b} b_a:{b_a}")
    assert a_b == b
    assert b_a == a


def test_swap_number_negative():
    a = -12
    b = 13
    (a_b, b_a) = swap_number(a, b)
    print(f"a:{a} b:{b} a_b:{a_b} b_a:{b_a}")
    assert a_b == b
    assert b_a == a
