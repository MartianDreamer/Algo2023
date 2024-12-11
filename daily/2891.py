from typing import Dict


class Solution:
    def maximumLength(self, s: str) -> int:
        cd: Dict[str, Dict[int, int]] = {}
        rs = -1
        cd[s[0]] = {1: 1}
        c = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                c += 1
                for j in range(1, c + 1):
                    cd[s[i]][j] = cd[s[i]].get(j, 0) + 1
            elif s[i] not in cd:
                c = 1
                cd[s[i]] = {1: 1}
            else:
                c = 1
                cd[s[i]][1] += 1
        for d in cd.values():
            for k, v in d.items():
                if v >= 3 and k > rs:
                    rs = k
        return rs

print(Solution().maximumLength("abcaba"))
