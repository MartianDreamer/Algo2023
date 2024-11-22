from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        ht = {}
        for r in matrix:
            rstr = "".join([str(c) for c in r])
            if rstr in ht:
                ht[rstr] += 1
            else:
                ivstr = "".join([str(0 if c else 1) for c in r])
                if ivstr in ht:
                    ht[ivstr] += 1
                else:
                    ht[rstr] = 1

        return max(ht.values())
