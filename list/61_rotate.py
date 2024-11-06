from typing import Optional

from linked_list import ListNode



class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        cur = head
        count = 0
        tail = None
        while cur is not None:
            cur = cur.next
            count += 1
            if cur is not None and cur.next is None: # type: ignore
                tail = cur # type: ignore

        nth_node_from_head = count - (k % count)
        if nth_node_from_head == count:
            return head

        cur = head
        for _ in range(nth_node_from_head - 1):
            cur = cur.next  # type: ignore
        new_head = cur.next  # type: ignore
        cur.next = None # type: ignore
        tail.next = head # type: ignore

        return new_head

print(Solution().rotateRight(ListNode.makeList([1,2]), 2))