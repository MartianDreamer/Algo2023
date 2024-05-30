from typing import List, Optional

from linked_list import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sortedArr = []
        for e in lists:
            while e is not None:
                sortedArr.insert(0, e.val)
                e = e.next
        sortedArr.sort()
        rs = None
        cur = None
        for e in sortedArr:
            if rs is None:
                rs = ListNode(e)
                cur = rs
            else:
                cur.next = ListNode(e)
                cur = cur.next
        return cur
