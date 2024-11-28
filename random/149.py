from typing import Dict, List, Set


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        max_line = 2
        for i in range(len(points) - 1):
            line_count: Dict[float, Set[str]] = {}
            for j in range(i + 1, len(points)):
                xi, yi = points[i]
                xj, yj = points[j]
                slope = (xj - xi) / (yj - yi) if yj != yi else float('inf')
                if slope not in line_count:
                    line_count[slope] = set()
                line_count[slope].add(f"{xj}_{yj}")
                line_count[slope].add(f"{xi}_{yi}")
                max_line = max(max_line, len(line_count[slope]))

        return max_line

print(Solution().maxPoints([[0,0],[4,5],[7,8],[8,9],[5,6],[3,4],[1,1]]))
