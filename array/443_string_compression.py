from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        start = 0
        rs = 0
        for end in range(0, len(chars) + 1):
            if end > 0 and (end == len(chars) or chars[end] != chars[end - 1]):
                length = end - start
                len_length = 0
                chars[rs] = chars[end - 1]
                if length > 1:
                    length_chars = [c for c in str(length)]
                    len_length = len(length_chars)
                    for i in range(len(length_chars)):
                        chars[rs + 1 + i] = length_chars[i]
                rs += 1 + len_length
                start = end                
        return rs

print(Solution().compress(["a","a","b","b","c","c","c"]))