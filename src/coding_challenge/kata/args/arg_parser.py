import abc
import re
from abc import abstractstaticmethod, abstractmethod
from typing import Sequence, Any, List, TypeVar, Generic, Type

from coding_challenge.kata.args.handler import ArgumentHandler

ALLOWED_FLAG_LETTERS = 'A-Za-z'
FLAG_LETTER_PATTERN = re.compile(f'[{ALLOWED_FLAG_LETTERS}]')
VALID_FLAG_PATTERN = re.compile(f'-(?P<flag>[{ALLOWED_FLAG_LETTERS}])')

class InvalidArgumentError(Exception):
    pass

class ArgumentParser():
    def __init__(self):
        self._schema: Dict[str, Type[ArgumentHandler]] = dict()
        self._arguments: Dict[str, Any] = dict()

    def add_argument(self, flag: str, handler: Type[ArgumentHandler]):
        if len(flag) != 1:
            raise ValueError(f'Invalid flag name length: A flag name must only contain one character.')

        if FLAG_LETTER_PATTERN.match(flag) is None:
            raise ValueError(
                f'Invalid flag name: Only a character from this range is allowed: {ALLOWED_FLAG_LETTERS}'
            )

        self._schema[flag] = handler

    def parse_args(self, args: List[str]):
        _args = args.copy()
        while _args:
            raw_flag = _args.pop()
            match = VALID_FLAG_PATTERN.match(raw_flag)
            if match is None:
                raise InvalidArgumentError(f'Unexpected flag format: "{raw_flag}". Must be -<flag character>')
            flag = match.group('flag')

            if flag not in self._schema:
                raise InvalidArgumentError(f'Unknown flag "{flag}"')

            handler = self._schema[flag]
            self._arguments[flag], args = handler.marshal(_args)

    def __getattr__(self, flag: str):
        if flag in self._arguments:
            return self._arguments[flag]
        if flag not in self._arguments and flag in self._schema:
            handler = self._schema[flag]
            return handler.default_value()
