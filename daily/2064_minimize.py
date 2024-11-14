from math import ceil
from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        if n == len(quantities):
            return max(quantities)

        def distributable(possible_min: int) -> bool:
            return sum(ceil(q / possible_min) for q in quantities) <= n

        left, right = 1, max(quantities) + 1
        while right - left > 1:
            mid = (right + left) // 2
            if distributable(mid):
                right = mid
            else:
                left = mid
        return left if distributable(left) else right


print(Solution().minimizedMaximum(6, [16, 1]))
