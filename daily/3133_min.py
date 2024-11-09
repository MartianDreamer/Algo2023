from functools import reduce
from typing import List

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        x_bits = []
        while x > 1:
            x_bits.append(x & 1)
            x >>= 1
        x_bits.append(x)

        n = n - 1
        cur_bit = 0
        while n > 0:
            least_significant_bit = n & 1
            n >>= 1

            i = cur_bit
            should_append = True
            for i in range(cur_bit, len(x_bits)):
                if x_bits[i] == 0:
                    cur_bit = i
                    x_bits[cur_bit] = least_significant_bit
                    should_append = False
                    break

            if should_append:
                cur_bit = len(x_bits)
                x_bits.append(least_significant_bit)
            
            cur_bit += 1

        rs = 0
        for i in range(len(x_bits)):
            rs = rs | x_bits[i] << i

        return rs

print(Solution().minEnd(7, 2))