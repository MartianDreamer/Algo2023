from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        rs = [bisect_left(nums, target), bisect_right(nums, target) - 1]
        return rs if rs[1] >= rs[0] else [-1, -1]
