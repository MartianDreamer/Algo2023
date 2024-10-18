class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = ""
        i = 0
        for i in range(min(len(word1), len(word2))):
            word += word1[i] + word2[i]
        word += word1[i + 1:] + word2[i + 1:]
        return word
