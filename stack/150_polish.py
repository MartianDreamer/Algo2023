from typing import Callable, Dict, List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        OPERATORS: Dict[str, Callable[[int, int], int]] = {"+": lambda a, b: a + b,
                                                           "-": lambda a, b: a - b,
                                                           "*": lambda a, b: a * b,
                                                           "/": lambda a, b: abs(a) // abs(b) * abs(a) // a * abs(b) // b}
        stack = []
        for t in reversed(tokens):
            if len(stack) == 0 or stack[-1] in OPERATORS or t in OPERATORS:
                stack.append(t)
                continue
            operand2 = int(t)
            while len(stack) >= 2 and stack[-1] not in OPERATORS:
                operand1 = int(stack.pop())
                operator = stack.pop()
                operand2 = OPERATORS[operator](operand2, operand1)
            stack.append(operand2)
        return int(stack[-1])

print(Solution().evalRPN(["2", "1", "+", "3", "*"]))
print(Solution().evalRPN(["4", "13", "5", "/", "+"]))
print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
