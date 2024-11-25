from typing import Callable, Dict, List


ADDITION, SUBSTRACTION = "+", "-"
OPEN, CLOSE = "(", ")"
OPERATORS = {ADDITION, SUBSTRACTION}


class Solution:
    def calculate(self, s: str) -> int:
        tokens = rpn(s)

        OPS: Dict[str, Callable[[int, int], int]] = {
            ADDITION: lambda a, b: a + b,
            SUBSTRACTION: lambda a, b: a - b,
        }
        stack = []

        for t in reversed(tokens):
            if len(stack) == 0 or stack[-1] in OPS or t in OPS:
                stack.append(t)
                continue
            operand2 = int(t)
            while len(stack) >= 2 and stack[-1] not in OPS:
                operand1 = int(stack.pop())
                operator = stack.pop()
                operand2 = OPS[operator](operand2, operand1)
            stack.append(operand2)
        return int(stack[-1])


def rpn(s: str) -> List[int | str]:
    operators_stack = []
    output = []
    idx = 0
    s.strip()
    if s[0] == SUBSTRACTION:
        output.append(0)
        operators_stack.append(SUBSTRACTION)
        idx = 1

    while idx < len(s):
        char = s[idx]
        if char == " ":
            # skip space characters
            idx += 1
        elif char == OPEN:
            operators_stack.append(char)
            idx += 1
            while s[idx] == " ":
                idx += 1
            if s[idx] == SUBSTRACTION:
                output.append(0)
                operators_stack.append(SUBSTRACTION)
                idx += 1
        elif char == CLOSE:
            op = operators_stack.pop()
            while op != OPEN:
                output.append(op)
                op = operators_stack.pop()
            idx += 1
        elif char in OPERATORS:
            while operators_stack and operators_stack[-1] in OPERATORS:
                output.append(operators_stack.pop())
            operators_stack.append(char)
            idx += 1
        else:
            number = 0
            while char.isdecimal():
                number = number * 10 + int(char)
                idx += 1
                if idx >= len(s):
                    break
                char = s[idx]
            output.append(number)

    output.extend(reversed(operators_stack))

    return output


print(Solution().calculate("1 - (   -2)"))
