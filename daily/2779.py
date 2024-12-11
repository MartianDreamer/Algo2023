import bisect
from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        start = 0
        count = 1
        rs = 1
        for i in range(1, len(nums)):
            s = bisect.bisect_left(nums, nums[i] - 2 * k)
            count = count - s + start + 1
            start = s
            rs = max(rs, count)
        return rs

print(Solution().maximumBeauty([13, 46, 71], 29))
