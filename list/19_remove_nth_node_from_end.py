from typing import Optional

from linked_list import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        cur = head
        for _ in range(n):
            if cur is not None:
                cur = cur.next
        if cur is None:
            return head.next
        prevRemove = head
        while cur.next is not None:
            cur = cur.next
            prevRemove = prevRemove.next # type: ignore
        prevRemove.next = prevRemove.next.next # type: ignore
        return head