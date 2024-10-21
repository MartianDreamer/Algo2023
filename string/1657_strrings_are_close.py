class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False
        w1_counts = {}
        w2_counts = {}
        for c in word1:
            w1_counts[c] = w1_counts.get(c, 0) + 1
        for c in word2:
            w2_counts[c] = w2_counts.get(c, 0) + 1
        return sorted(w1_counts.values()) == sorted(w2_counts.values())
