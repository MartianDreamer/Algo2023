from math import ceil
from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        possible_min = ceil(sum(quantities) / n)
        quantities.sort(reverse=True)


        def distributable(quantities: List[int]) -> bool:
            nonlocal possible_min, n
            start = 0
            search = possible_min
            c = 1
            remain_n = n
            while start < len(quantities) and remain_n >= len(quantities) - start:
                end = bin_s(search, start, quantities)
                remain_n -= (end - start) * c
                start = end
                c += 1
                search = possible_min * c

            return remain_n >= len(quantities) - start

        while not distributable(quantities):
            possible_min += 1
        return possible_min




def bin_s(search: int, start: int, quantities: List[int]) -> int:
    left, right = start, len(quantities) - 1
    if search >= quantities[right]:
        return len(quantities)
    if search < quantities[left]:
        return left
    while right - 1 > left:
        mid = (left + right) // 2
        if quantities[mid] > search:
            right = mid
        elif quantities[mid] <= search:
            left = mid
    return right
