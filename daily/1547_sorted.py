from typing import List
from bisect import bisect_right


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        head_idx, tail_idx = -1, -1
        length = len(arr)
        for i in range(1, length):
            if arr[i] < arr[i - 1]:
                if head_idx == -1:
                    head_idx = i
                tail_idx = i

        if head_idx == -1:
            return 0
        removed_middle = tail_idx - head_idx

        rs = min(head_idx + removed_middle, length - tail_idx + removed_middle)
        print(rs)
        for i in range(tail_idx, length):
            sect = bisect_right(arr, arr[i], 0, head_idx)
            new_rs = (
                head_idx
                - sect
                - (1 if sect < head_idx and arr[i] == arr[sect] else 0)
                + i
                + removed_middle
            )
            rs = min(rs, new_rs)
        return rs
