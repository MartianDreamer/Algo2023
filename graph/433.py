from typing import List
from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def neighbours(gene: str) -> List[str]:
            rs = [g for g in bank if mutable(gene, g) == 1]
            for g in rs:
                bank.remove(g)
            return rs

        frontiers = deque([startGene])
        fcount = 1
        mutcount = 0
        rs = -1

        while frontiers:
            f = frontiers.popleft()
            fcount -= 1
            frontiers.extend(neighbours(f))
            if fcount == 0:
                mutcount += 1
                fcount = len(frontiers)
            if endGene in frontiers:
                rs = mutcount + (1 if fcount != len(frontiers) else 0)
                break

        return rs


def mutable(gene1: str, gene2: str) -> int:
    diff = 0
    for c1, c2 in zip(gene1, gene2):
        diff += 1 if c1 != c2 else 0
    return diff


print(
    Solution().minMutation(
        "AAAAAAAA",
        "AAAAACGG",
        ["AAAAAAGA", "AAAAAGGA", "AAAAACGA", "AAAAACGG", "AAAAAAGG", "AAAAAAGC"],
    )
)
