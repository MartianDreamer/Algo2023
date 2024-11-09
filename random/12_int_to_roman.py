from typing import Dict, List


class Solution:
    def intToRoman(self, num: int) -> str:
        rs: List[str] = []

        while (num > 0):
            if num >= 1000:
                rs.append("M" * (num // 1000))
                num %= 1000
            elif num >= 900:
                rs.append("CM")
                num %= 100
            elif num >= 500:
                rs.append("D")
                rs.append("C" * ((num - 500) // 100))
                num %= 100
            elif num >= 400:
                rs.append("CD")
                num %= 100
            elif num >= 100:
                rs.append("C" * (num // 100))
                num %= 100
            elif num >= 90:
                rs.append("XC")
                num %= 10
            elif num >= 50:
                rs.append("L")
                rs.append("X" * ((num - 50) // 10))
                num %= 10
            elif num >= 40:
                rs.append("XL")
                num %= 10
            elif num >= 10:
                rs.append("X" * (num // 10))
                num %= 10
            elif num >= 9:
                rs.append("IX")
                num %= 1
            elif num >= 5:
                rs.append("V")
                rs.append("I" * ((num - 5) // 1))
                num %= 1
            elif num >= 4:
                rs.append("IV")
                num %= 1
            elif num >= 1:
                rs.append("I" * (num // 1))
                num %= 1

        return "".join(rs)


print(Solution().intToRoman(1994))
