class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        aord = ord("a")
        charcount = [0, 0, 0]
        l, r = 0, len(s)

        while r > l and (charcount[0] < k or charcount[1] < k or charcount[2] < k):
            r -= 1
            c = s[r]
            charcount[ord(c) - aord] += 1
        
        rs = len(s) - r

        if charcount[0] < k or charcount[1] < k or charcount[2] < k:
            return -1

        for l in range(0, len(s)):
            charcount[ord(s[l]) - aord] += 1
            while r < len(s) and charcount[ord(s[r]) - aord] > k:
                charcount[ord(s[r]) - aord] -= 1
                r += 1
            
            rs = min(rs, len(s) - r + l + 1)

        return rs
