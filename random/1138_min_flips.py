class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while a | b != c:
            a_1 = bool(a & 1)
            b_1 = bool(b & 1)
            c_1 = bool(c & 1)
            if (a_1 or b_1) != c_1:
                if not a_1 or b_1 == c_1:
                    count += 1
                elif not a_1 or not b_1 == c_1:
                    count += 2
            a >>= 1
            b >>= 1
            c >>= 1
        return count

print(Solution().minFlips(7, 3, 9))