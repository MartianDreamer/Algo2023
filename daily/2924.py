from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        teams: List[List[int]] = [[] for _ in range(n)]
        for s, w in edges:
            teams[w].append(s)
        strongs = [s for s in range(len(teams)) if len(teams[s]) == 0]
        return -1 if len(strongs) > 1 else strongs[0]
