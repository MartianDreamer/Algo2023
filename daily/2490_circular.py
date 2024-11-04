class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        first_letter = sentence[0]
        last_letter = sentence[-1]
        if first_letter != last_letter:
            return False
        prev_last = first_letter 
        is_new_word = False
        for c in sentence:
            if c == " ":
                is_new_word = True
                continue
            if is_new_word:
                is_new_word = False
                if c != prev_last:
                    return False
            prev_last = c
        return True
