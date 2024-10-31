import sys
from typing import List


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        factories = []

        for pos, limit in factory:
            factories.extend([pos] * limit)

        # tabular[i][j] is the minimum distiance to repare i robots with j factories
        tabular = [[sys.maxsize] * (len(factories) + 1)
                   for _ in range(len(robot))]
        # tabular[0][j] is to repare 0 robots so distances are 0
        # all other distances are set to inf, which means not figure out
        # tabular[i][0] are always inf because can not move robots to repare with 0 factories 
        tabular.insert(0, [0] * (len(factories) + 1))

        for i in range(1, len(robot) + 1):
            for j in range(1, len(factories) + 1):
                # add new factory one by one
                # tabular[i][j - 1] means that repare i robots with j - 1 factories ignore the new j
                # tabular[i - 1][j - 1] + abs(robot[i - 1] - factories[j - 1] means that move robot ith to the newly added factory (jth)
                tabular[i][j] = min(tabular[i][j - 1],
                                    tabular[i - 1][j - 1] + abs(robot[i - 1] - factories[j - 1]))

        return tabular[len(robot)][len(factories)]
