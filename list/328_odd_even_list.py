
from typing import Optional
from linked_list import ListNode


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None or head.next.next is None:
            return head
        
        size = 1
        tail = head
        while tail.next is not None:
            size += 1
            tail = tail.next
            
        
        prev, cur = None, head
        for i in range(size):
            if i % 2 == 0:
                prev = cur
                cur = cur.next # type: ignore
            else:
                prev.next = cur.next # type: ignore
                cur.next = None # type: ignore
                tail.next = cur # type: ignore
                tail = cur
                cur = prev.next # type: ignore
        return head


l = ListNode.makeList([1,1])
print(Solution().oddEvenList(l))