class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if is_open(c):
                stack.append(c)
                continue
            if not try_take_out(c, stack):
                return False
        return len(stack) == 0


def is_open(s: str) -> bool:
    return s == "(" or s == "{" or s == "["


def try_take_out(s: str, stack: list[str]) -> bool:
    if len(stack) > 0 and (stack[-1] == "(" and s == ")" or \
            stack[-1] == "{" and s == "}" or \
            stack[-1] == "[" and s == "]"):
        stack.pop()
        return True
    else:
        return False


Solution().isValid("]")