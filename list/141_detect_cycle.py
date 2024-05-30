
from typing import Optional

from list.linked_list import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        slowNode = head
        fastNode = head.next
        while fastNode is not None and fastNode.next is not None:
            if slowNode == fastNode.next:
                return True
            slowNode = slowNode.next
            fastNode = fastNode.next.next
