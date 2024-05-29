from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        return [self.__hammingWeight(i) for i in range(n)]

    def __hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            count += 1 if n & 1 == 1 else 0
            n >>= 1
        return count
