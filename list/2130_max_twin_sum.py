from typing import Optional, no_type_check
from linked_list import ListNode

class Solution:

    @no_type_check
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        if head.next.next is None:
            return head.val + head.next.val

        size = 0
        cur = head
        while cur is not None:
            size += 1
            cur = cur.next

        rs = []

        cur = head
        for i in range(size):
            if i < size//2:
                rs.append(cur.val)
            else:
                rs[-(1 - size//2 + i)] += cur.val
            cur = cur.next
        return max(rs)


l = ListNode.makeList([5,4,2,1])
print(Solution().pairSum(l))