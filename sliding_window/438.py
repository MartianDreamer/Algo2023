from functools import reduce
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        ht = {}

        for c in p:
            ht[c] = ht.get(c, 0) + 1

        for c in s[: len(p)]:
            if c in ht:
                ht[c] -= 1

        rs = []
        if reduce(lambda e1, e2: e1 and e2, map(lambda e: e == 0, ht.values()), True):
            rs.append(0)
        for i in range(len(p), len(s)):
            removed_char = s[i - len(p)]
            added_char = s[i]
            if removed_char in ht:
                ht[removed_char] += 1
            if added_char in ht:
                ht[added_char] -= 1
                if ht[added_char] == 0 and reduce(
                    lambda e1, e2: e1 and e2, map(lambda e: e == 0, ht.values()), True
                ):
                    rs.append(i - len(p) + 1)
        return rs
