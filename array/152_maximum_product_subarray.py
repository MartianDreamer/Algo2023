from typing import List

class Solution: 
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1
        for num in nums:
            if num == 0:
                curMin, curMax = 1, 1
                continue
            oldCurMax = curMax
            curMax = max(oldCurMax * num, curMin * num, num)
            curMin = min(oldCurMax * num, curMin * num, num)
            res = max(curMax, res)
        return res

Solution().maxProduct([-2,3,-4])