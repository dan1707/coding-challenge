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
            raise IndexError(f'Missing value of string flag')
        return value, args

    @staticmethod
    def default_value() -> str:
        return ''