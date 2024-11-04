from typing import Tuple


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        start = 0
        cur = 1
        while s[cur] == s[cur - 1]:
            cur += 1
            if cur == len(s):
                break

        rs_start, rs_end = start, cur

        def find_panlindrome(left, right) -> Tuple[int, int]:
            cur_right, cur_left = right, left
            while cur_right >= cur_left:
                if s[cur_left] != s[cur_right]:
                    left += 1
                    cur_left = left
                    cur_right = right
                    continue
                cur_left += 1
                cur_right -= 1
            return left, right


        while cur < len(s):
            
            if start >= 0 and s[cur] == s[start]:
                start -= 1
            else:
                start, _ = find_panlindrome(start + 1, cur)
                start -= 1
 

            if cur - start > rs_end - rs_start:
                rs_start, rs_end = start + 1, cur + 1
            cur += 1

        return s[rs_start:rs_end]

# print(Solution().longestPalindrome("ababababababa"))
# print(Solution().longestPalindrome("banana"))
print(Solution().longestPalindrome("adam"))
