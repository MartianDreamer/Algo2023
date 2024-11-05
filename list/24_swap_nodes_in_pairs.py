from typing import Optional

from linked_list import ListNode

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        prev: ListNode = head.next
        head.next = prev.next
        prev.next = head
        cur = head
        rs = prev
        i: int = 0
        while cur is not None:
            if i % 2 == 1:
                n_cur = cur.next
                if n_cur is not None:
                    prev.next = n_cur
                    cur.next = n_cur.next
                    n_cur.next = cur
                    cur = n_cur

            prev, cur = cur, cur.next # type: ignore
            i += 1
        return rs


print(Solution().swapPairs(ListNode.makeList([1,2,3,4])))