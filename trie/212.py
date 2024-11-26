from typing import Dict, List
import __params


class TrieNode:
    def __init__(self, char: str, is_word: bool) -> None:
        self.char = char
        self.is_word = is_word
        self.children: List[TrieNode | None] = [None] * 26

    def check(self, word: str) -> bool:
        return self.__check_with_idx(word, 0)

    def __check_with_idx(self, word: str, i: int) -> bool:
        char = ord(word[i]) - ord("a")
        if i == len(word) - 1:
            return self.children[char] is not None and self.children[char].is_word  # type: ignore
        return self.children[char] is not None and self.children[char].__check_with_idx(  # type: ignore
            word, i + 1
        )


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode("", False)

        def dfs(
            r: int,
            c: int,
            level: int,
            depth: int,
            trie: TrieNode,
        ) -> None:
            if level == depth:
                return
            if r >= len(board) or r < 0:
                return
            if c >= len(board[0]) or c < 0:
                return
            if board[r][c] == ".":
                return
            pos = ord(board[r][c]) - ord("a")
            if trie.children[pos] is None:
                trie.children[pos] = TrieNode(board[r][c], True)
            child = trie.children[pos]
            board[r][c] = "."
            left, right, up, down = c - 1, c + 1, r - 1, r + 1
            dfs(r, left, level + 1, depth, child) # type: ignore
            dfs(r, right, level + 1, depth, child) # type: ignore
            dfs(up, c, level + 1, depth, child) # type: ignore
            dfs(down, c, level + 1, depth, child) # type: ignore
            board[r][c] = child.char # type: ignore

        prefixes = set()
        depth = 0

        for w in words:
            prefixes.add(w[0:1])
            depth = max(depth, len(w))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in prefixes:
                    dfs(i, j, 0, depth, root)

        rs = []
        for w in words:
            if root.check(w):
                rs.append(w)

        return rs


print(Solution().findWords(*__params.params4))
