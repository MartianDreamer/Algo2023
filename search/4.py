from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = []
        i1 = 0
        i2 = 0
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] <= nums2[i2]:
                total.append(nums1[i1])
                i1 += 1
            else:
                total.append(nums2[i2])
                i2 += 1
        for i in range(i1, len(nums1)):
            total.append(nums1[i])
        for i in range(i2, len(nums2)):
            total.append(nums2[i])
        return total[len(total) // 2] if len(total) % 2 == 1 else (total[len(total) // 2] + total[len(total) // 2 - 1]) / 2
