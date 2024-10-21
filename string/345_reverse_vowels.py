class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "o", "u", "e", "i"}
        vowels_in_s = [v for v in s if v.lower() in vowels]
        for i in range(len(vowels_in_s)//2):
            t = vowels_in_s[i]
            vowels_in_s[i] = vowels_in_s[len(vowels_in_s) - 1  -i]
            vowels_in_s[len(vowels_in_s) - 1  -i] = t
        return "".join([c if c.lower() not in vowels else vowels_in_s.pop(0) for c in s])
