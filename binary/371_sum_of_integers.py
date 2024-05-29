class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a & b != 0:
            return self.getSum(a ^ b, (a & b) << 1)
        return a ^ b
