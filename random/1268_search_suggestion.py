from typing import List


class Solution:

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        class Trie:
            def __init__(self):
                self.chars: dict[str, Trie] = {}
                self.words = set()

            def insert(self, word: str) -> None:
                cur = self
                for c in word:
                    if c not in cur.chars:
                        cur.chars[c] = Trie()
                    cur = cur.chars[c]
                cur.words.add(word)

            def suggest(self, searchWord: str) -> List[List[str]]:
                cur = self
                rs = []
                current_word = ""
                for c in searchWord:
                    if cur is None or c not in cur.chars:
                        rs.append([])
                        cur = None
                        continue
                    cur = cur.chars[c]
                    current_word += c
                    words = [current_word] if current_word in cur.words else []
                    cur.__take_all_further_words__(words)
                    rs.append(sorted(words)[:3])
                return rs

            def __take_all_further_words__(self, rs: list[str], limit: int = 3):
                if len(rs) >= limit:
                    return
                for k in sorted(self.chars.keys()):
                    rs.extend(self.chars[k].words)
                    if len(rs) >= 3:
                        return
                    self.chars[k].__take_all_further_words__(rs, limit)
                    if len(rs) >= 3:
                        return

        t = Trie()

        for product in products:
            t.insert(product)

        return t.suggest(searchWord)
