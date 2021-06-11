import typing
from typing import List, Callable

from coding_challenge.sort.sort import Sorter, CmpCallable


class BubbleSort(Sorter):

    @staticmethod
    def sort(a: List[int], cmp: CmpCallable) -> List[int]:
        sortable = a.copy()
        swapped = True
        while swapped:
            swapped = False
            for i in range(0, len(sortable) - 1):
                if not cmp(sortable[i], sortable[i + 1]):
                    tmp = sortable[i]
                    sortable[i] = sortable[i+1]
                    sortable[i + 1] = tmp
                    swapped = True
        return sortable
