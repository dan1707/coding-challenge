import abc
from abc import abstractmethod
from typing import TypeVar, Generic, List

T = TypeVar('T')


class ArgumentHandler(abc.ABC, Generic[T]):

    @staticmethod
    @abstractmethod
    def marshal(args: List[str]) -> (T, List[str]):
        pass

    @staticmethod
    @abstractmethod
    def default_value() -> T:
        pass


class BooleanArgument(ArgumentHandler[bool]):

    @staticmethod
    def marshal(args: List[str]) -> (bool, List[str]):
        return True, args

    @staticmethod
    def default_value() -> bool:
        return False


class StringArgument(ArgumentHandler[str]):

    @staticmethod
    def marshal(args: List[str]) -> (str, List[str]):
        try:
            value = args.pop(0)
        except(IndexError):
            raise IndexError('Missing value of string flag')
        return value, args

    @staticmethod
    def default_value() -> str:
        return ''


class IntArgument(ArgumentHandler[int]):

    @staticmethod
    def marshal(args: List[str]) -> (int, List[str]):
        try:
            value = args.pop(0)
        except(IndexError):
            raise IndexError('Missing value of int flag')
        try:
            int_value = int(value)
        except(ValueError):
            raise ValueError(f'Value "{value}" of integer flag is not a valid integer')
        return int_value, args

    @staticmethod
    def default_value() -> int:
        return 0