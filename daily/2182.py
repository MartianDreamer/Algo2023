class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        letterCount = [0] * 26
        a = ord("a")
        for c in s:
            letterCount[ord(c) - a] += 1
        letterCount = [
            [chr(a + c), letterCount[c]]
            for c in range(len(letterCount))
            if letterCount[c]
        ]
        i = len(letterCount) - 1
        prev = -1
        rs = []
        while i > -1:
            if not letterCount[i][1]:
                i += prev
                continue
            if i + 1 < len(letterCount) and sum(c[1] for c in letterCount[i + 1 :]):
                rs.append(letterCount[i][0] * 1)
                letterCount[i][1] -= 1
                prev = 1
            else:
                count = min(letterCount[i][1], repeatLimit)
                rs.append(letterCount[i][0] * count)
                letterCount[i][1] -= count
                prev = -1
            i += prev

        return "".join(rs)


# print(Solution().repeatLimitedString("cczazcc", 3))
# print(Solution().repeatLimitedString("aababab", 2))
# print(Solution().repeatLimitedString("xyutfpopdynbadwtvmxiemmusevduloxwvpkjioizvanetecnuqbqqdtrwrkgt", 1))
print(Solution().repeatLimitedString("bplpcfifosybmjxphbxdltxtfrjspgixoxzbpwrtkopepjxfooazjyosengdlvyfchqhqxznnhuuxhtbrojyhxwlsrklsryvmufoibgfyxgjw", 1))

