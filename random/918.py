from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        kadane_total = -3 * 10**4
        kadane_rs = kadane_total
        reversed_kadane_total = 3 * 10**4
        reversed_kadane_rs = reversed_kadane_total
        total = 0
        for n in nums:
            total += n
            kadane_total = max(kadane_total + n, n)
            kadane_rs = max(kadane_rs, kadane_total)
            reversed_kadane_total = min(reversed_kadane_total + n, n)
            reversed_kadane_rs = min(reversed_kadane_rs, reversed_kadane_total)
        
        if reversed_kadane_total == total:
            return kadane_rs
        return max(kadane_rs, total - reversed_kadane_rs)
