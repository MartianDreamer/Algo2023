class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        tabular = [[-1 for _ in range(len(word2))] for _ in range(len(word1))]

        def distance(i: int, j: int) -> int:
            if i == -1 or j == -1:
                return abs(i - j)
            if tabular[i][j] != -1:
                return tabular[i][j]

            tabular[i][j] = min(distance(i - 1, j) + 1,
                       distance(i, j - 1) + 1,
                       distance(i - 1, j - 1) + (0 if word1[i] == word2[j] else 1))

            return tabular[i][j]

        return distance(len(word1) - 1, len(word2) - 1)

print(Solution().minDistance("horse", "ros"))