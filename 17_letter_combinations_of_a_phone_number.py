from typing import List

class Solution:
    digitMap = [
        '',
        '',
        'abc',
        'def',
        'ghi',
        'jkl',
        'mno',
        'pqrs',
        'tuv',
        'wxyz'
    ]
        
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return self.digitMap[int(digits)]
        firstNumb = int(digits[0])
        remaining = digits[1::]
        remainingRs = self.letterCombinations(remaining)
        rs = []
        for x in self.digitMap[firstNumb]:
            rs.extend([x + y for y in remainingRs])
        return rs
