from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        def dfs_mark_province(city: int, isConnected: List[List[int]]):
            if isConnected[city][city] == 0:
                return

            for i in range(len(isConnected[city])):
                if i == city:
                    isConnected[city][i] = 0
                elif isConnected[city][i] == 1:
                    dfs_mark_province(i, isConnected)
        
        for i in range(len(isConnected)):
            if isConnected[i][i] == 1:
                count += 1
                dfs_mark_province(i, isConnected)
        return count
