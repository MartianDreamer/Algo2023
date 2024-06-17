from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        posList = [[] for _ in range(len(s))]
        notReach = set()
        for word in wordDict:
            jumpStep = self.getJumpStep(word)
            i = 0
            wordLen = len(word)
            while len(s) - i >= wordLen:
                try:
                    start = s.index(word, i)
                    end = start + wordLen
                    posList[start].append(end)
                    i = start + jumpStep
                except:
                    break
        return self.checkWordBreak(notReach, posList, 0)

    def checkWordBreak(self, notReach: set, posList: List[List[int]], pos: int):
        if pos in notReach:
            return False
        result = False
        for nextPos in posList[pos]:
            if nextPos == len(posList):
                return True
            else:
                result |= self.checkWordBreak(notReach, posList, nextPos)
        if not result:
            notReach.add(pos)
        return result

    def getJumpStep(self, s: str) -> int:
        allSame = True
        firstChar = s[0]
        for char in s:
            allSame &= char == firstChar
        if allSame:
            return 1
        rs = True
        for i in range(int(len(s)/2)):
            rs &= s[i] == s[len(s) - 1 - i]
            if not rs:
                return len(s)
        return int(len(s)/2)


print(Solution().wordBreak("applepenapple", ["apple", "pen"]))
print(Solution().wordBreak("aaaaaaa", ["aaaa", "aaa"]))
print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
