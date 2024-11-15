from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return combine(1, n, k)


def combine(start: int, end: int, k: int) -> List[List[int]]:
    if k == 0:
        return [[]]
    if k == end + 1 - start:
        return [[i for i in range(start, end + 1)]]
    if k == 1:
        return [[i] for i in range(start, end + 1)]
    rs = []
    for i in range(start, end + 1 - k + 1):
        coms = combine(i + 1, end, k - 1)
        for c in coms:
            c.insert(0, i)
            rs.append(c)
    return rs

