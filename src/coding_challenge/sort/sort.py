from abc import ABC, abstractmethod
from typing import List, Callable

CmpCallable = Callable[[int, int], bool]


class Sorter(ABC):

    @staticmethod
    @abstractmethod
    def sort(sortable_list: List[int], comparator: CmpCallable) -> List[int]:
        pass
