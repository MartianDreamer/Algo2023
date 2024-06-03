from typing import List


class Solution:
    # TODO not done yet
    def pacificAtlantic(self, heights):
        rs = []
        pacificCells = []
        atlantisCells = []
        rowQuan = len(heights)
        colQuan = len(heights[0])
        pacificVisitted = [[False] * colQuan for _ in range(rowQuan)]
        atlantisVisitted = [[False] * colQuan for _ in range(rowQuan)]
        queue = []
        for i in range(rowQuan):
            pacificCells.append([i, 0])
            atlantisCells.append([i, colQuan - 1])
        for i in range(colQuan):
            pacificCells.append([0, i])
            atlantisCells.append([rowQuan - 1, i])

        # find all the cells can reach Pacific
        for cell in pacificCells:
            r, c = cell[0], cell[1]
            if pacificVisitted[r][c]:
                continue
            pacificVisitted[r][c] = True
            queue.append(cell)
            while len(queue) > 0:
                head = queue.pop(0)
                headR, headC = head[0], head[1]
                for n in self.__neighbors(headR, headC, rowQuan, colQuan):
                    nR, nC = n[0], n[1]
                    if not pacificVisitted[nR][nC] and heights[nR][nC] >= heights[headR][headC]:
                        pacificVisitted[nR][nC] = True
                        queue.append(n)

        # find all the cells can reach Pacific and Atlantis
        for cell in atlantisCells:
            r, c = cell[0], cell[1]
            if atlantisVisitted[r][c]:
                continue
            atlantisVisitted[r][c] = True
            queue.append(cell)
            while len(queue) > 0:
                head = queue.pop(0)
                headR, headC = head[0], head[1]
                if pacificVisitted[headR][headC]:
                    rs.append(head)
                for n in self.__neighbors(headR, headC, rowQuan, colQuan):
                    nR, nC = n[0], n[1]
                    if not atlantisVisitted[nR][nC] and heights[nR][nC] >= heights[headR][headC]:
                        atlantisVisitted[nR][nC] = True
                        queue.append(n)

        return rs

    def __neighbors(self, r, c, rowQuan, colQuan):
        rs = []
        if r - 1 >= 0:
            rs.append([r - 1, c])
        if r + 1 < rowQuan:
            rs.append([r + 1, c])
        if c - 1 >= 0:
            rs.append([r, c - 1])
        if c + 1 < colQuan:
            rs.append([r, c + 1])
        return rs


print(Solution().pacificAtlantic([[1,1],[1,1],[1,1]]))
