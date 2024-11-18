class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque

class Solution:
    def connect(self, root: "Node") -> "Node":
        if root is None:
            return None
        frontiers = deque([root])
        fcount = 1
        while frontiers:
            f = frontiers.popleft()
            fcount -= 1
            if f.left is not None:
                if len(frontiers) > fcount:
                    frontiers[-1].next = f.left
                frontiers.append(f.left)
            if f.right is not None:
                if len(frontiers) > fcount:
                    frontiers[-1].next = f.right
                frontiers.append(f.right)
            if fcount == 0:
                fcount = len(frontiers)
        return root
