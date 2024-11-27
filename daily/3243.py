from typing import Dict, List
import __params


class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        jumps: Dict[int, List[int]] = {}
        steps = [i for i in range(n)]

        def calculate(cur: int, cur_step: int) -> int:
            if cur_step > steps[cur]:
                return steps[n - 1]
            else:
                steps[cur] = cur_step
            if cur == n - 1:
                return cur_step
            elif cur not in jumps:
                return calculate(cur + 1, cur_step + 1)
            step = n - 1
            for t in jumps[cur]:
                step = steps[n - 1]
                step = min(step, calculate(t, cur_step + 1))
            step = min(step, calculate(cur + 1, cur_step + 1))
            return step

        rs = []
        prev = n - 1
        for f, t in queries:
            if f not in jumps:
                jumps[f] = []
            jumps[f].append(t)
            prev = min(prev, calculate(f, steps[f]))
            rs.append(prev)

        return rs


print(Solution().shortestDistanceAfterQueries(8,[[0,4],[3,6],[2,5],[0,3]]))
# print(Solution().shortestDistanceAfterQueries(*__params.params1))
# print(Solution().shortestDistanceAfterQueries(*__params.params2))
# print(Solution().shortestDistanceAfterQueries(*__params.params3))
