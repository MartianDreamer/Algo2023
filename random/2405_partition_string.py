class Solution:
    def partitionString(self, s: str) -> int:
        met: set[str] = set()
        count = 1
        for c in s:
            if c in met:
                met.clear()
                count += 1
            met.add(c)
        return count
