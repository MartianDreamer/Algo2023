from typing import List

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 2, - 1, -1):
            if arr[i] > arr[i + 1]:
                swapped = i + 1
                for j in range (i + 2, len(arr)):
                    if arr[j] > arr[swapped] and arr[j] < arr[i]:
                        swapped = j
                arr[swapped], arr[i] = arr[i], arr[swapped]
                break
        return arr


print(Solution().prevPermOpt1([1,9,6,4,3,2,7]))