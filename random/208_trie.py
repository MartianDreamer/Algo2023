class Trie:

    def __init__(self):
        self.chars : dict[str, Trie] = {}
        self.words = set()

    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.chars:
                cur.chars[c] = Trie()
            cur = cur.chars[c]
        cur.words.add(word)


    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            if c not in cur.chars:
                return False
            cur = cur.chars[c]
        return word in cur.words

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            if c not in cur.chars:
                return False
            cur = cur.chars[c]
        return True

t = Trie()

methods = ["insert","insert","insert","insert","insert","insert","search","search","search","search","search","search","search","search","search","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith"]

paramsList = [["app"],["apple"],["beer"],["add"],["jam"],["rental"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"]]

for method, params in zip(methods, paramsList):
    print(getattr(t, method)(*params))