from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        reachable = [False] * (len(s) + 1)
        reachable[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i+len(w)] == w:
                    reachable[i] = reachable[i+len(w)]
                if reachable[i]:
                    break
        return reachable[0]


print(Solution().wordBreak("applepenapple", ["apple", "pen"]))
# print(Solution().wordBreak("aaaaaaa", ["aaaa", "aaa"]))
print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
