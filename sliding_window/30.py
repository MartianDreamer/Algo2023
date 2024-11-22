from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        rs = []
        jump_length = len(words[0])
        matched_length = len(words) * jump_length
        worddict = {}
        for w in words:
            worddict[w] = worddict.get(w, 0) + 1
        for i in range(0, len(s) - matched_length + 1):
            if i > 0 and s[i - 1] == s[i + matched_length - 1] and rs[-1] == i - 1:
                rs.append(i)
                continue
            wdcopy = worddict.copy()
            count = 0
            while count < len(words):
                curword = s[i + count * jump_length : i + (count + 1) * jump_length]
                remainingword = wdcopy.get(curword, 0) - 1
                if remainingword < 0:
                    break
                wdcopy[curword] = remainingword
                count += 1
            if count == len(words):
                rs.append(i)

        return rs
