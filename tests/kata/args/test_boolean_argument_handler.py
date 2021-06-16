from coding_challenge.kata.args.handler import BooleanArgument


def test_marshal_does_not_consume_args():
    args = ['1', '2']
    _, r_args = BooleanArgument.marshal(args.copy())
    assert args == r_args


def test_marshal_returns_true():
    value, _ = BooleanArgument.marshal([])
    assert value is True


def test_default_value_is_false():
    assert BooleanArgument.default_value() is False
