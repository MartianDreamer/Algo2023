UP, DOWN = 1, 2

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for _ in range(numRows)]
        direct = UP
        pos = 0

        def move():
            nonlocal pos, direct
            if direct == UP:
                pos += 1
            if direct == DOWN:
                pos -= 1
            if pos == 0:
                direct = UP
            elif pos == numRows - 1:
                direct = DOWN


        for c in s:
            rows[pos].append(c)
            move()

        return "".join(["".join(r) for r in rows])


print(Solution().convert("PAYPALISHIRING", 1))