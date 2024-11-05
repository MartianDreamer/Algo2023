from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def shift(pos: int, limit: int):
            left, right = pos * 2 + 1, pos * 2 + 2
            if left >= limit:
                return
            elif right >= limit:
                if nums[left] > nums[pos]:
                    nums[pos], nums[left] = nums[left], nums[pos]
                    shift(left, limit)
            elif max(nums[left], nums[right]) > nums[pos]:
                smaller = left if nums[left] >= nums[right] else right
                nums[pos], nums[smaller] = nums[smaller], nums[pos]
                shift(smaller, limit)

        def heapify() -> None:
            for i in range(len(nums) // 2, -1, -1):
                shift(i, len(nums))

        def heapSort() -> None:
            heapify()
            limit = len(nums) - 1
            for i in range(len(nums)):
                nums[limit - i], nums[0] = nums[0], nums[limit - i]
                shift(0, limit - i)

        heapSort()

n = [2,0,2,1,1,0]
Solution().sortColors(n)
print(n)
