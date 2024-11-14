from typing import Dict, Optional


class Node:
    def __init__(self, x: int, next: "Node | None" = None, random: "Node | None" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if head is None:
            return head
        new_head = Node(head.val)
        n_dict: Dict[Node, Node] = {head: new_head}

        cur = head.next
        new_cur = new_head
        while cur is not None:
            new_node = Node(cur.val)
            n_dict[cur] = new_node
            new_cur.next = new_node
            cur = cur.next
            new_cur = new_node

        cur = head
        new_cur = new_head
        while cur is not None:
            if cur.random is not None:
                new_cur.random = n_dict[cur.random] # type: ignore
            new_cur = new_cur.next # type: ignore
            cur = cur.next
        
        return new_head
