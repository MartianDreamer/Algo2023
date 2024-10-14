class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        weight = 1
        s = s.lstrip()
        if s.startswith("-"):
            weight = -1
            s = s[1:]
        elif s.startswith("+"):
            s = s[1:]
        for c in s:
            if not c.isdigit():
                break
            result = result*10 + weight*int(c)
            if result < -2**31:
                return -2**31
            elif result > 2**31 - 1:
                return 2**31 - 1

        return result


print(Solution().myAtoi("-+12"))