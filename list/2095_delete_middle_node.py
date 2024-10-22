from typing import Optional

from linked_list import ListNode


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        cur = head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        middle = count // 2
        cur = head
        for _ in range(middle - 1):
            cur = cur.next # type: ignore
        cur.next = cur.next.next  # type: ignore
        return head

list = ListNode.makeList([1,3,4,7,1,2,6])

print(Solution().deleteMiddle(list))