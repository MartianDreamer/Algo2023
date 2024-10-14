from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    carry = 0

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None and self.carry == 0:
            return None
        l1_val = 0
        next_l1 = None
        l2_val = 0
        next_l2 = None
        if l1 is not None:
            l1_val = l1.val
            next_l1 = l1.next
        if l2 is not None:
            l2_val = l2.val
            next_l2 = l2.next
        l3_val = l1_val + l2_val + self.carry
        self.carry = 1 if l3_val >= 10 else 0
        l3_val = l3_val % 10
        return ListNode(l3_val, self.addTwoNumbers(next_l1, next_l2))
