import pytest
from coding_challenge.kata.args.arg_parser import ArgumentParser, InvalidArgumentError
from coding_challenge.kata.args.handler import BooleanArgument


def test_add_argument_fail_with_empty_flag_name():
    parser = ArgumentParser()
    with pytest.raises(ValueError):
        parser.add_argument('', BooleanArgument)


def test_add_argument_fail_with_multiple_char_flag_name():
    parser = ArgumentParser()
    with pytest.raises(ValueError):
        parser.add_argument('ll', BooleanArgument)


def test_add_argument_fail_with_flag_name_containing_non_letter():
    parser = ArgumentParser()
    with pytest.raises(ValueError):
        parser.add_argument('+', BooleanArgument)


def test_parse_args_fail_with_empty_argument():
    parser = ArgumentParser()
    parser.add_argument('l', BooleanArgument)
    with pytest.raises(InvalidArgumentError):
        parser.parse_args([''])


def test_parse_args_fail_with_invalid_argument():
    parser = ArgumentParser()
    parser.add_argument('l', BooleanArgument)
    with pytest.raises(InvalidArgumentError):
        parser.parse_args(['jkeh'])


def test_parse_args_fail_with_unknown_argument():
    parser = ArgumentParser()
    parser.add_argument('l', BooleanArgument)
    with pytest.raises(InvalidArgumentError):
        parser.parse_args(['-L'])


def test_get_item_with_unknown_flag_returns_none():
    parser = ArgumentParser()
    parser.add_argument('l', BooleanArgument)
    parser.parse_args([])
    assert parser.x is None


def test_get_item_with_known_flag_but_not_in_args_returns_default_value():
    parser = ArgumentParser()
    parser.add_argument('l', BooleanArgument)
    parser.parse_args([])
    assert parser.l is BooleanArgument.default_value()
