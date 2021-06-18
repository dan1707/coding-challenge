import pytest
from coding_challenge.kata.args.handler import IntArgument


def test_marshal_does_consume_and_return_next_arg():
    args = ['1', 'bb']
    value, r_args = IntArgument.marshal(args)
    assert len(r_args) == 1
    assert r_args == ['bb']
    assert value == 1


def test_marshal_fails_with_non_integer_argument():
    args = ['aa', 'bb']
    with pytest.raises(ValueError):
        _, _ = IntArgument.marshal(args)


def test_marshal_fails_without_next_arg():
    with pytest.raises(IndexError):
        _, _ = IntArgument.marshal([])


def test_default_value_is_empty_string():
    assert IntArgument.default_value() == 0
