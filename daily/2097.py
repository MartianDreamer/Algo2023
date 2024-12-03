from typing import Dict, List


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        out_edges: Dict[int, List[int]] = {}
        in_edges: Dict[int, int] = {s: 0 for s, _ in pairs}
        for s, e in pairs:
            if s not in out_edges:
                out_edges[s] = [e]
            else:
                out_edges[s].append(e)
            in_edges[e] = in_edges.get(e, 0) + 1
        start = pairs[0][0]
        for s in out_edges:
            if len(out_edges[s]) - in_edges[s] > 0:
                start = s

        def find_cycle(start: int) -> List[int]:
            stack = [start]
            path = []
            while stack:
                n = stack[-1]
                if n in out_edges and out_edges[n]:
                    next_n = out_edges[n].pop()
                    stack.append(next_n)
                else:
                    path.append(stack.pop())
            return path

        path = find_cycle(start)

        for i in range(len(path)):
            if path[i] in out_edges and out_edges[path[i]]:
                sub_cycle = find_cycle(path[i])
                path = path[:i] + sub_cycle + path[i+1:]
                
        rs = []
        while len(path) > 1:
            rs.append([path.pop(), path[-1]])
        return rs


print(
    Solution().validArrangement(
        [
            [5, 13],
            [10, 6],
            [11, 3],
            [15, 19],
            [16, 19],
            [1, 10],
            [19, 11],
            [4, 16],
            [19, 9],
            [5, 11],
            [5, 6],
            [13, 5],
            [13, 9],
            [9, 15],
            [11, 16],
            [6, 9],
            [9, 13],
            [3, 1],
            [16, 5],
            [6, 5],
        ]
    )
)
# print(Solution().validArrangement([[5, 1], [4, 5], [11, 9], [9, 4]]))
