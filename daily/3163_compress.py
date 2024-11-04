import random


class Solution:
    def compressedString(self, word: str) -> str:
        count, cur_c = 0, word[0]
        rs_l: list[str] = []
        for c in [*word, " "]:
            if c == cur_c and count < 9:
                count += 1
                continue
            rs_l.append(str(count))
            rs_l.append(cur_c)
            cur_c = c
            count = 1
        return "".join(rs_l)
