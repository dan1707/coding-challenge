import pytest
from coding_challenge.kata.args.arg_parser import ArgumentParser
from coding_challenge.kata.args.handler import BooleanArgument, StringArgument, IntArgument


def test_with_bool_string_int_flags_and_arguments():
    parser = ArgumentParser()
    parser.add_argument('l', BooleanArgument)
    parser.add_argument('p', IntArgument)
    parser.add_argument('f', StringArgument)
    parser.parse_args(['-l', '-p', '8080', '-f', '/usr/logs'])
    assert parser.l is True
    assert parser.p == 8080
    assert parser.f == '/usr/logs'


def test_with_bool_string_int_flags_and_missing_arguments():
    parser = ArgumentParser()
    parser.add_argument('l', BooleanArgument)
    parser.add_argument('p', IntArgument)
    parser.add_argument('f', StringArgument)
    parser.parse_args([])
    assert parser.l is False
    assert parser.p == 0
    assert parser.f == ''


def test_with_flags_and_negative_int_arguments():
    parser = ArgumentParser()
    parser.add_argument('l', BooleanArgument)
    parser.add_argument('p', IntArgument)
    parser.add_argument('f', StringArgument)
    parser.parse_args(['-l', '-p', '-1', '-f', '-3'])
    assert parser.l is True
    assert parser.p == -1
    assert parser.f == '-3'
