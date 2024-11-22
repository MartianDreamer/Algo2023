from typing import Dict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hts: Dict[str, int] = {}
        htt: Dict[str, int] = {}

        for c in t:
            if c in htt:
                htt[c] += 1
            else:
                htt[c] = 1

        def is_covered():
            covered = True
            for k, v in htt.items():
                covered &= v <= hts.get(k, 0)
                if not covered:
                    break
            return covered

        left, right = 0, 0
        rs = ""

        while right < len(s):
            if not is_covered():
                rchar = s[right]
                if rchar in htt:
                    hts[rchar] = hts.get(rchar, 0) + 1
                right += 1
            while is_covered():
                rs = s[left:right] if rs == "" or len(rs) > right - left else rs
                lchar = s[left]
                if lchar in hts:
                    hts[lchar] -= 1
                left += 1

        return rs


print(Solution().minWindow("a", "aa"))
