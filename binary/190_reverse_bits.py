class Solution:
    def reverseBits(self, n: int) -> int:
        rs = 0
        for _ in range(32):
            rs = rs << 1 | n & 1
            n >>= 1
        return rs