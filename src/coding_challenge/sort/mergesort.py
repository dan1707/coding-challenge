from typing import List

from coding_challenge.sort.sort import Sorter, CmpCallable


class MergeSort(Sorter):

    @staticmethod
    def sort(sortable_list: List[int], comparator: CmpCallable) -> List[int]:
        if len(sortable_list) == 1:
            return sortable_list

        middle = int(len(sortable_list) / 2)
        left_list = MergeSort.sort(sortable_list[0:middle], comparator)
        right_list = MergeSort.sort(sortable_list[middle:None], comparator)
        return MergeSort.merge(left_list, right_list, comparator)

    @staticmethod
    def merge(left: List[int], right: List[int], comparator: CmpCallable) -> List[int]:
        merged_list = []
        left_index = right_index = 0

        while left_index < len(left) and right_index < len(right):
            lvalue = left[left_index]
            rvalue = right[right_index]
            if comparator(lvalue, rvalue):
                merged_list.append(lvalue)
                left_index += 1
            else:
                merged_list.append(rvalue)
                right_index += 1

        for i in range(left_index, len(left)):
            merged_list.append(left[i])

        for i in range(right_index, len(right)):
            merged_list.append(right[i])

        return merged_list
