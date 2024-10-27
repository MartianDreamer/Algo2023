class Solution:
    def numTilings(self, n: int) -> int:
        table = [1, 1, 2, *[0] * (n - 2)]
        for i in range(3, n + 1):
            table[i] = table[i - 1] * 2 + table[i - 3]
        return table[n]
