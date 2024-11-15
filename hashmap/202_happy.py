from typing import Generator


class Solution:
    def isHappy(self, n: int) -> bool:
        met = set()
        while n not in met and n != 1:
            met.add(n)
            total = 0
            for d in split_numb(n):
                total += d**2
            n = total
        return n == 1


def split_numb(n: int) -> Generator[int, int, None]:
    while n != 0:
        digit = n % 10
        n //= 10
        yield digit

print(Solution().isHappy(19))
