from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nodes = []
        while head is not None:
            nodes.append(TreeNode(head.val))
            head = head.next
        return connect_tree_node(nodes)


def connect_tree_node(nodes: list[TreeNode]) -> Optional[TreeNode]:
    if len(nodes) == 0:
        return None
    elif len(nodes) == 1:
        return nodes[0]
    mid = len(nodes) // 2
    nodes[mid].left = connect_tree_node(nodes[:mid])
    if mid + 1 < len(nodes):
        nodes[mid].right = connect_tree_node(nodes[mid + 1:])
    return nodes[mid]
