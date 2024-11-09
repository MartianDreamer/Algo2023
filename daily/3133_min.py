class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        c = 0

        # min end for x = 0b100110, n - 1 = 15 (0b1111) is 0b1111111
        # go through every bit of n - 1
        # or the bit with zero bit in x
        # consider there are zeros before the most significant bit of x

        while n > 0:
            lsb = n & 1
            n >>= 1


            remember_x = x
            x >>= c
            while x & 1:
                c += 1
                x >>= 1
            x = (x | lsb) << c | remember_x
            c += 1


        return x
