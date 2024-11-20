from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def generate_sentence():
            remaining = maxWidth
            linewlist = []
            while words and remaining >= len(words[0]):
                w = words.pop(0)
                linewlist.append(w)
                remaining -= len(w)
                remaining -= 1
            remaining += 1
            if words:
                idx = 0
                leng = len(linewlist) - 1 if len(linewlist) != 1 else 1
                while remaining > 0:
                    linewlist[idx % leng] += " "
                    idx += 1
                    remaining -= 1
            else:
                print(remaining)
                while remaining > 0:
                    linewlist[-1] += " "
                    remaining -= 1
            return " ".join(linewlist)

        rs = []
        while words:
            rs.append(generate_sentence())
        return rs
