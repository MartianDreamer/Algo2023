from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        first, second =  nums[0], None
        for num in nums:
            if first > num:
                first = num
            elif first < num:
                if second == None or second > num:
                    second = num
                elif num > second:
                    return True
        return False
