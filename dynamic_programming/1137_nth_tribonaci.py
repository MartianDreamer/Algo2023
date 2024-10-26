class Solution:
    def __init__(self) -> None:
        self.__table = [0, 1, 1, *[-1] * 35]

    def tribonacci(self, n: int) -> int:
        if self.__table[n] != -1:
            return self.__table[n]
        self.__table[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        return self.__table[n]
    
print(Solution().tribonacci(37))