from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_n1 = set(nums1)
        set_n2 = set(nums2)
        return [[n for n in set_n1 if n not in set_n2], [n for n in set_n2 if n not in set_n1]]
