from typing import Optional, Tuple

from linked_list import ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        def reverse(
            head: Optional[ListNode], k: int
        ) -> Tuple[Optional[ListNode], Optional[ListNode]]:
            if head is None:
                return None, None
            length = 1
            cur = head
            splits = [head]
            next_cur = cur.next
            while next_cur is not None:
                cur = next_cur
                length += 1
                if length % k == 0:
                    next_cur = cur.next
                    cur.next = None
                    continue
                if length % k == 1:
                    splits.append(cur)
                next_cur = cur.next

            if k > length:
                return (head, cur)
            elif k == length:
                prev = head
                cur = head.next
                prev.next = None
                while cur is not None:
                    next_cur = cur.next
                    cur.next = prev
                    prev = cur
                    cur = next_cur
                return prev, head
            else:
                prev_tail = None
                for i in range(len(splits)):
                    if i == 0:
                        head, prev_tail = reverse(splits[i], k)
                    else:
                        new_head, new_tail = reverse(splits[i], k)
                        prev_tail.next = new_head  # type: ignore
                        prev_tail = new_tail
                return head, prev_tail

        return reverse(head, k)[0]
