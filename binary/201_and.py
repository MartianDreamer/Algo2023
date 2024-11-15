class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        common = 1 << 30
        rs = 0
        while left & common == right & common:
            rs |= left & common
            common >>= 1
        return rs
