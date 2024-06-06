class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = dict()
        maxCharCount = 0
        start, end = 0, 1
        rs = 0
        while end <= len(s):
            while end <= len(s):
                c = s[end - 1]
                charCount[c] = charCount[c] + 1 if c in charCount else 1
                maxCharCount = charCount[c] if charCount[c] > maxCharCount else maxCharCount
                if end - start - maxCharCount > k or end > len(s):
                    end += 1
                    break
                rs = end - start if end - start > rs else rs
                end += 1
            charCount[s[start]] -= 1
            start += 1
        return rs
        



print(Solution().characterReplacement("AABABBA", 1))
print(Solution().characterReplacement("AABBAABBAA", 3))
print(Solution().characterReplacement("ABAB", 2))
print(Solution().characterReplacement("ABBB", 2))
print(Solution().characterReplacement(
    "BRJRRKNRBFOOKDEEGODTGMHNABMTHFNPTFRHRSEKKTFEQIKSIAJJMSDSLNSCNRNJFNFSIQDNMHDRIJIACLCJKATTFHDASGLRQSFN", 10))
