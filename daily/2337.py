class Solution:
    def canChange(self, start: str, target: str) -> bool:
        prev = 0
        for si in range(len(start)):
            if start[si] == "_":
                continue
            s = prev if start[si] == "L" else max(prev, si)
            e = si + 1 if start[si] == "L" else len(target)
            ti = s
            for ti in range(s, e):
                if target[ti] == "_":
                    continue
                elif target[ti] != start[si]:
                    return False
                elif target[ti] == start[si]:
                    prev = ti + 1
                    break
            else:
                return False
        for i in range(prev, len(target)):
            if target[i] != "_":
                return False
        return True
