from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        for i in range(size // 2):
            for j in range(i, size - 1 - i):
                t1, t2, t3, t4 = matrix[i][j], matrix[j][size - 1 -
                                                         i], matrix[size - 1 - i][size - 1 - j], matrix[size - 1 - j][i]
                matrix[i][j] = t4
                matrix[j][size - 1 - i] = t1
                matrix[size - 1 - i][size - 1 - j] = t2
                matrix[size - 1 - j][i] = t3
