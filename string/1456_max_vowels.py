class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "o", "u", "e", "i"}
        k_str_count = sum([s[:k].count(c) for c in vowels])
        rs = 0
        for i in range(1, len(s) - k + 1):
            if s[i - 1] in vowels:
                k_str_count -= 1
            if s[i + k - 1] in vowels:
                k_str_count += 1
            rs = max(rs, k_str_count)
        return rs

print(Solution().maxVowels("abciiidef", 3))