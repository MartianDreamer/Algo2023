from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        rs = [0] * len(temperatures)
        m_stack = []
        for index in range(len(temperatures)):
            while len(m_stack) > 0 and temperatures[m_stack[-1]] < temperatures[index]:
                i = m_stack.pop()
                rs[i] = index - i
            m_stack.append(index)
            
        return rs


print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))