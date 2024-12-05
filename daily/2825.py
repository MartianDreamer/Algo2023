class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        s2idx = 0
        for c in str1:
            oc = ord(c)
            oc2 = ord(str2[s2idx])
            if oc == oc2 or oc2 - oc == 1 or oc2 - oc == -25:
                s2idx += 1
                if s2idx == len(str2):
                    return True
        return False
