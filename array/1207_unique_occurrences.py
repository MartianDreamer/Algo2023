from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = {n: arr.count(n) for n in arr}
        counts_set = {v for _,v in counts.items()}
        return len(counts) == len(counts_set)
