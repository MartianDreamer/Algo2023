class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        rs = list(s[:2])
        for c in s[2:]:
            if [c] * 2 == rs[-2:]:
                continue
            rs.append(c)
        return "".join(rs)
