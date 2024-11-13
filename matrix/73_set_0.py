from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroes = []
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    zeroes.append((r, c))
        for r, c in zeroes:
            for i in range(len(matrix[r])):
                matrix[r][i] = 0
            for i in range(len(matrix)):
                matrix[i][c] = 0
