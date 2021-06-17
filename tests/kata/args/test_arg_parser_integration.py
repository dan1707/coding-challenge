import pytest
from coding_challenge.kata.args.arg_parser import ArgumentParser
from coding_challenge.kata.args.handler import BooleanArgument, StringArgument


def test_bool_flag_with_argument_returns_true():
    parser = ArgumentParser()
    parser.add_argument('l', BooleanArgument)
    parser.parse_args(['-l'])
    assert parser.l is True


def test_bool_flag_without_argument_returns_default_value():
    parser = ArgumentParser()
    parser.add_argument('l', BooleanArgument)
    assert parser.l is BooleanArgument.default_value()


def test_string_flag_with_argument_returns_string_value():
    parser = ArgumentParser()
    parser.add_argument('f', StringArgument)
    parser.parse_args(['-f', '/myfile'])
    assert parser.f == '/myfile'


def test_string_flag_without_argument_fails():
    parser = ArgumentParser()
    parser.add_argument('f', StringArgument)
    with pytest.raises(IndexError):
        parser.parse_args(['-f'])


def test_string_flag_without_argument_returns_default_value():
    parser = ArgumentParser()
    parser.add_argument('f', StringArgument)
    assert parser.f == StringArgument.default_value()

