from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph: dict[str, dict[str, float]] = {}
        
        for [dividend, divisor], result in zip(equations, values):
            if dividend not in graph:
                graph[dividend] = {divisor: result}
            else:
                graph[dividend][divisor] = result
            if divisor not in graph:
                graph[divisor] = {dividend: 1/result}
            else:
                graph[divisor][dividend] = 1/result
        
        def calculate(dividend, divisor, value, met: set[str]) -> float:
            met.add(dividend)
            if dividend not in graph or divisor not in graph:
                return -1
            if divisor in graph[dividend]:
                return value * graph[dividend][divisor]
            for possible in graph[dividend]:
                if possible in met:
                    continue
                rs = value * calculate(possible, divisor, graph[dividend][possible], met)
                if rs > 0:
                    return rs
            return -1
        
        return [calculate(dividend, divisor, 1, set()) for [dividend, divisor] in queries]
            
print(Solution().calcEquation([["a","b"],["b","c"],["d", "e"]], [2.0,3.0,1.0], [["a","c"],["b","a"],["a","e"]]))