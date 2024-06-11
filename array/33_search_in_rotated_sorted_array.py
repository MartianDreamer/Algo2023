from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        rotate = self.findRotate(nums)
        findLeft, findRight = self.binarySearch(
            nums[:rotate], target), rotate + self.binarySearch(nums[rotate:], target)
        findRight = -1 if findRight < rotate else findRight
        return findRight if findRight != -1 else findLeft

    def findRotate(self, nums: List[int]):
        if nums[0] < nums[len(nums) - 1]:
            return 0
        middle = int(len(nums) / 2)
        if nums[0] > nums[middle - 1]:
            return self.findRotate(nums[:middle])
        if nums[middle] > nums[len(nums) - 1]:
            return middle + self.findRotate(nums[middle:])
        return middle

    def binarySearch(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        middle = int(len(nums) / 2)
        if nums[0] == target:
            return 0
        elif nums[middle] == target:
            return middle
        if nums[middle] > target:
            return self.binarySearch(nums[:middle], target)
        elif nums[middle] < target:
            rightIndex = self.binarySearch(nums[middle + 1:], target)
            return -1 if rightIndex == -1 else middle + 1 + rightIndex
        return -1
