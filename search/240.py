from bisect import bisect_left
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in matrix:
            if target < r[0] or target > r[-1]:
                continue
            idx = bisect_left(r, target)
            if target == r[idx]:
                return True
        return False


print(
    Solution().searchMatrix(
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25],
        ],
        16,
    )
)

print(
    Solution().searchMatrix(
        [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ],
        5,
    )
)

print(Solution().searchMatrix([[5, 6, 10, 14], [6, 10, 13, 18], [10, 13, 18, 19]], 14))
