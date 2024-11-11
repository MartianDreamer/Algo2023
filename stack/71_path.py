class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split("/")
        for p in parts:
            if p == "" or p == ".":
                continue
            elif p == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)
        print(parts)
        print(stack)
        return "/" + "/".join(stack)
