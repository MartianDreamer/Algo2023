from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        pair_dict: dict[int, int] = {}
        count = 0
        for num in nums:
            if k - num in pair_dict and pair_dict[k - num] > 0:
                count += 1
                pair_dict[k - num] -= 1
            elif num in pair_dict:
                pair_dict[num] += 1
            elif num not in pair_dict:
                pair_dict[num] = 1
        return count
