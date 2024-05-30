
class Solution:
    def reorderList(self, head):
        nodes = []
        while head is not None:
            nodes.append(head)
            head = head.next
        size = len(nodes)
        for i in range(size/2):
            nodes[i].next = nodes[size - 1 - i]
            nodes[size - 1 - i].next = nodes[i+1]
            nodes[i+1].next = None
