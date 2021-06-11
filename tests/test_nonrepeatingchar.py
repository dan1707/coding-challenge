from coding_challenge.string.nonrepeatingchar import first_non_repeating_char


def test_first_non_repeating_char():
    assert 'b' == first_non_repeating_char('abcdefghija')
    assert 'h' == first_non_repeating_char('hello')
    assert 'J' == first_non_repeating_char('Java')
    assert 'i' == first_non_repeating_char('simplest')
    assert first_non_repeating_char('simppims') is None
