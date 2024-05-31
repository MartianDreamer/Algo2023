from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacencyList = [[] for _ in range(numCourses)]
        visitted = [0] * numCourses
        for pre in prerequisites:
            toTake, mustTake = pre[0], pre[1]
            adjacencyList[toTake].append(mustTake)
        for e in range(numCourses):
            if self.dfsDetectCycle(e, adjacencyList, visitted):
                return False
        return True

    # not visit yet = 0, visitting  = 1, cycle = 2, no cycle = 3
    def dfsDetectCycle(self, root: int, adjacencyList: List[List[int]], visitted: List[int]) -> bool:
        if visitted[root] == 1 or visitted[root] == 2:
            visitted[root] = 2
            return True
        elif visitted[root] == 3:
            return False
        visitted[root] = 1
        for e in adjacencyList[root]:
            if self.dfsDetectCycle(e, adjacencyList, visitted):
                visitted[root] = 2
                return True
        visitted[root] = 3
        return False


print(Solution().canFinish(2, [[1, 0]]))
