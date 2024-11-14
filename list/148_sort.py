from linked_list import ListNode
from typing import Optional, Tuple
from random import randint


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return quickSort(head, length(head))[0]


def length(head: Optional[ListNode]) -> int:
    if head is None:
        return 0
    c = 0
    while head is not None:
        head = head.next
        c += 1
    return c


def quickSort(
    head: Optional[ListNode], lenght: int
) -> Tuple[Optional[ListNode], Optional[ListNode]]:
    if lenght <= 1:
        return (head, head)

    pivot_idx = randint(0, lenght - 1)
    prev, pivot = None, head
    for _ in range(pivot_idx):
        prev = pivot
        pivot = pivot.next # type: ignore
    if prev is not None:
        prev.next = pivot.next # type: ignore
        pivot.next = head # type: ignore
    prev = pivot
    cur = pivot.next # type: ignore
    new_head = pivot
    first_half_length = 0
    while cur is not None:
        if cur.val < pivot.val: # type: ignore
            prev.next = cur.next # type: ignore
            cur.next = new_head
            new_head = cur
            cur = prev.next # type: ignore
            first_half_length += 1
        else:
            prev = cur
            cur = cur.next
    
    second_half_head = pivot.next # type: ignore
    second_half_length = lenght - first_half_length - 1
    second_half_tail = None
    first_half_head, first_half_tail = new_head, pivot
    pivot.next = None # type: ignore

    if second_half_length > 0:
        second_half_head, second_half_tail = quickSort(second_half_head, second_half_length)
    if first_half_length > 0:
        first_half_head, first_half_tail = quickSort(new_head, first_half_length + 1)
    
    first_half_tail.next = second_half_head # type: ignore
    
    return (first_half_head, second_half_tail if second_half_tail is not None else first_half_tail)
