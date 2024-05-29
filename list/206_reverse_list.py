from typing import Optional
from linked_list import ListNode

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        prev = None
        while head is not None:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev