from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        i: int = 0
        is_all = True
        for i in range(len(citations)):
            if i + 1 > citations[i]:
                is_all = False
                break

        return i + 1 if is_all else i
