import heapq
from typing import List

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        score, prefix_sum, min_heap = 0, 0, []
        for n1, n2 in sorted(zip(nums1, nums2), key=lambda e: e[1], reverse=True):
            prefix_sum += n1
            heapq.heappush(min_heap, n1)
            if len(min_heap) == k:
                score = max(score, n2 * prefix_sum)
                prefix_sum -= heapq.heappop(min_heap)

        return score
    
print(Solution().maxScore([1,3,3,2], [2,1,3,4], 3))