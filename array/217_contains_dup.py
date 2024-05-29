from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        rem = set()
        for num in nums:
            if num not in rem:
                rem.add(num)
            else:
                return True
