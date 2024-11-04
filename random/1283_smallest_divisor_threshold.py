import random
from typing import List
import math


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        mid = (left + right) // 2
        while right != left:
            total = sum([math.ceil(n / mid) for n in nums])
            if total <= threshold:
                right = mid
            else:
                left = mid + 1
            mid = (left + right) // 2
        return mid

print(Solution().smallestDivisor([21212,10101,12121], 1000000))