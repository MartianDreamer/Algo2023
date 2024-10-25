from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        def count_successful_pairs(potions: List[int], spell: int, success: int) -> int:
            left, right = 0, len(potions) - 1

            if spell * potions[left] >= success:
                return len(potions)
            elif spell * potions[right] < success:
                return 0
            midle = (left + right) // 2

            while not (spell * potions[midle - 1] < success and spell * potions[midle] >= success):
                if spell * potions[midle] < success:
                    left = midle + 1
                elif spell * potions[midle - 1] >= success:
                    right = midle - 1
                midle = (left + right) // 2
            return len(potions) - midle
                    
        sorted_potions = sorted(potions)

        return [count_successful_pairs(sorted_potions, sp, success) for sp in spells]
