from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        if target < 0:
            return []
        if target == 0:
            return [[]]
        rs = []
        for i in range(len(candidates)):
            if target - candidates[i] < 0:
                break
            coms = self.combinationSum(candidates[i:], target - candidates[i])
            rs.extend([[candidates[i], *com] for com in coms])
        return rs



print(Solution().combinationSum([2,3,6,7], 7))