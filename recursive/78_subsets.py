from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rs: List[List[int]] = [[]]
        def find_subsets(start: int) -> List[List[int]]:
            if len(nums) - start <= 1:
                return [[nums[start]]]
            subset = find_subsets(start + 1)
            return [[nums[start]], *subset, *[[nums[start], *s] for s in subset]]
        rs.extend(find_subsets(0))
        return rs


print(Solution().subsets([1, 2, 3]))
