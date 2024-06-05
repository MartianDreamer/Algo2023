class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        repeat = dict()
        count = 0
        result = 0
        limit = 0
        for i, c in enumerate(s):
            if c in repeat and repeat[c] >= limit:
                result = count if count > result else result
                count = i - repeat[c] - 1
                limit = repeat[c]
                repeat.pop(c)
            count += 1
            repeat[c] = i
            i += 1
        result = count if count > result else result
        return result


print(Solution().lengthOfLongestSubstring("abcabcbb"))
