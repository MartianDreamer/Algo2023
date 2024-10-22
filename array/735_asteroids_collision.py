from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        rs = [asteroids[0]]
        for a in asteroids[1:]:
            should_append = True
            while len(rs) > 0 and a * rs[-1] < 0 and rs[-1] > 0:
                if abs(a) > abs(rs[-1]):
                    rs.pop()
                    continue
                elif abs(a) == abs(rs[-1]):
                    rs.pop()
                    should_append = False
                    break
                else:
                    should_append = False
                    break
            if should_append:
                rs.append(a)
        return rs

print(Solution().asteroidCollision([-2,-1,1,2]))