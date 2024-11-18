class Solution:
    def trailingZeroes(self, n: int) -> int:
        c = 0
        f = 1
        for num in range(1, n + 1):
            f *= num
            while f % 10 == 0:
                c += 1
                f //= 10
        return c
    
print(Solution().trailingZeroes(20))
