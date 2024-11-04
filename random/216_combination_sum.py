from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def back_track(k: int, n: int, before: list[int], possibles: list[int]) -> list[list[int]]:
            if n <= 0:
                return []
            if k == 1:
                if n in possibles:
                    return [[*before, n]]
            rs = []
            for i in range(len(possibles)):
                rs.extend(back_track(k - 1, n - possibles[i], [*before, possibles[i]], possibles[i + 1:]))
            return rs
        
        return back_track(k, n, [], [i for i in range(1, 10)])

print(Solution().combinationSum3(3, 7))
