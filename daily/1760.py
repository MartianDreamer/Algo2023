from typing import List
from math import ceil
import bisect


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        nums.sort()

        def calculate_operation_number(maxBag: int) -> int:
            idx = bisect.bisect_right(nums, maxBag)
            rs = 0
            for i in range(idx, len(nums)):
                rs += ceil(nums[i] / maxBag) - 1
            return rs

        def binsearch(start: int, target: int, end: int = 1) -> int:
            mid = (end + start) // 2
            while start - end > 1:
                ops = calculate_operation_number(mid)
                if ops <= target:
                    start = mid
                else:
                    end = mid
                mid = (end + start) // 2
            return start

        return binsearch(nums[-1], maxOperations)

print(Solution().minimumSize([9], 2))