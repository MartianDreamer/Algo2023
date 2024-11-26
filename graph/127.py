from typing import List, Set
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        frontiers = deque([beginWord])
        met = set([beginWord])
        count = 1
        step = 0

        while frontiers:
            f = frontiers.popleft()
            count -= 1
            fneighbours = neighbours(f, word_set, met)
            met.update(fneighbours)
            frontiers.extend(fneighbours)
            if count == 0:
                count = len(frontiers)
                step += 1
                if endWord in frontiers:
                    break
        else:
            return 0

        return step + 1


def neighbours(word: str, word_set: Set[str], met: Set[str]) -> List[str]:
    rs = []
    for i in range(len(word)):
        for c in range(ord("a"), ord("z") + 1):
            if c == ord(word[i]):
                continue
            new_word = word[:i] + chr(c) + word[i + 1 :]
            if new_word in word_set and new_word not in met:
                rs.append(new_word)
    return rs


print(Solution().ladderLength("hot", "dog", ["hot", "dog"]))
