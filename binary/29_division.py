import random


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dividend_less_than_0 = 1
        divisor_less_than_0 = 1
        if dividend < 0:
            dividend = -dividend
            dividend_less_than_0 = -1
        if divisor < 0:
            divisor = -divisor
            divisor_less_than_0 = - 1
        rs = 0
        while dividend >= divisor:
            cur_divisor = divisor
            rs1 = 1
            while cur_divisor <= dividend:
                cur_divisor <<= 1
                rs1 <<= 1
            rs += rs1 >> 1
            dividend -= cur_divisor >> 1
        rs = rs * divisor_less_than_0 * dividend_less_than_0
        return rs if rs < 2**31 - 1 else 2**31 - 1

# print(Solution().divide(10, 3))
print(Solution().divide(-2147483648, -1))