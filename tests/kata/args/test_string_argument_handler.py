import pytest
from coding_challenge.kata.args.handler import StringArgument


def test_marshal_does_consume_and_return_next_arg():
    args = ['aa', 'bb']
    value, r_args = StringArgument.marshal(args)
    assert len(r_args) == 1
    assert r_args == ['bb']
    assert value == 'aa'


def test_marshal_fails_without_next_arg():
    with pytest.raises(IndexError):
        _, _ = StringArgument.marshal([])


def test_default_value_is_empty_string():
    assert StringArgument.default_value() == ''
