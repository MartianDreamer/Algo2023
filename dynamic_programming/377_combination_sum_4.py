from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        return self.__combinationSum4(dict(), nums, target)

    def __combinationSum4(self, mem: dict, nums: List[int], target: int) -> int:
        rs = 0
        if target == 0:
            return 0
        if target in mem:
            return mem[target]
        if target in nums:
            mem[target] = 1
            rs = 1
        for num in nums:
            if target - num < 0:
                continue
            count = self.__combinationSum4(mem, nums, target - num)
            rs += count
            mem[target] = rs
        return rs
    
print(Solution().combinationSum4([1,2,3], 4))