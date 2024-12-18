from collections import deque
from typing import Deque, List, Tuple

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window: Deque[Tuple[int, int]] = deque()
        for i, n in enumerate(nums[:k]):
            while window and window[-1][1] < n:
                window.pop()
            window.append((i, n))
        rs = [window[0][1]]
        for i in range(k, len(nums)):
            n = nums[i]
            if window[0][0] <= i - k:
                window.popleft()
            while window and window[-1][1] < n:
                window.pop()
            window.append((i, n))
            rs.append(window[0][1])
        return rs
