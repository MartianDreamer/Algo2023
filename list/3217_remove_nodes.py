from typing import List, Optional

from linked_list import ListNode


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        set_nums = set(nums)
        while head is not None and head.val in set_nums:
            head = head.next
        prev,cur = head, head
        while cur is not None:
            if cur.val in set_nums:
                prev.next = cur.next # type: ignore
                cur = prev
            prev = cur
            cur = cur.next # type: ignore
            
        return head
        
print(Solution().modifiedList([1,2,3], ListNode.makeList([1,2,3,4,5])))