from typing import Optional

from linked_list import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        rs = list1 if list1.val <= list2.val else list2
        prevList1 = None
        while list1 is not None and list2 is not None:
            while list1 is not None and list1.val <= list2.val:
                prevList1 = list1
                list1 = list1.next
            start = list2
            end = None
            while list2 is not None and list1 is not None and list2.val <= list1.val:
                end = list2
                list2 = list2.next
            if prevList1 is not None:
                prevList1.next = start
            if end is not None:
                end.next = list1
        return rs
