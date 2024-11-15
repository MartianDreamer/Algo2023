from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return generate(n , n)


def generate(n: int, m: int) -> List[str]:
    if n == 0:
        return [")" * m]
    if n == m:
        return [f"({s}" for s in generate(n - 1, m)]
    else:
        return [f"){s}" for s in generate(n, m - 1)] + [f"({s}" for s in generate(n - 1, m)]
