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
