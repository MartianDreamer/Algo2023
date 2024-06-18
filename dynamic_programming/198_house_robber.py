from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = [[-1] * (len(nums) + 1) for _ in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            mem[i][i] = 0
        return self.__rob(mem, nums, 0, len(nums))

    def __rob(self, mem: List[List[int]], nums: List[int], start: int, end: int) -> int:
        if mem[start][end] != -1:
            return mem[start][end]
        if end - start <= 2:
            return max(nums[start:end])
        robFromStart = nums[start] + self.__rob(mem, nums, start + 2, end)
        robFromEnd = nums[end - 1] + self.__rob(mem, nums, start, end - 2)
        rs = max(robFromStart, robFromEnd)
        for i in range(start + 1, end - 1):
            robVal = nums[i] + self.__rob(mem, nums, start,
                                          i - 1) + self.__rob(mem, nums, i + 2, end)
            rs = max(rs, robVal)
        mem[start][end] = rs
        return rs


print(Solution().rob([1, 2, 3, 1]))
