from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        zones = [1] * len(nums)
        cur_zone = 1
        for i in range(1, len(nums)):
            if (nums[i] - nums[i - 1]) % 2 == 1:
                zones[i] = cur_zone
            else:
                cur_zone += 1
                zones[i] = cur_zone
        rs = []
        for s, e in queries:
            rs.append(zones[s] == zones[e])
        return rs

