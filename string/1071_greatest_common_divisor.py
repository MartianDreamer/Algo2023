class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        div = detect_divisor(str1)
        if div != detect_divisor(str2):
            return ""
        count1 = str1.count(div)
        count2 = str2.count(div)
        from math import gcd
        return gcd(count1, count2)*div


def detect_divisor(s: str) -> str:
    divisor = ""
    for c in s:
        if len(divisor) == 0 or c != divisor[0]:
            divisor += c
        else:
            new_s = s.replace(divisor,"")
            if len(new_s) == 0:
                return divisor
            else:
                divisor += c
    return divisor
