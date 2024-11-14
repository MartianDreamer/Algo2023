from typing import Optional

from linked_list import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        prev, cur = None, head
        while cur is not None:
            if cur.next is not None and cur.next.val == cur.val:
                cur = cur.next
                continue
            if prev is None and cur != head:
                head = cur.next
                cur = cur.next
                continue
            elif prev is not None and prev.next != cur:
                prev.next = cur.next
                cur = cur.next
                continue
            prev = cur
            cur = cur.next
        return head
