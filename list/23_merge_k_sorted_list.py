from typing import List, Optional

from linked_list import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        lenHeap = 0
        for e in lists:
            while e is not None:
                heap.insert(0, e.val)
                lenHeap += 1
                self.heapify(heap, 0, lenHeap)
                e = e.next
        rs = None
        cur = None
        for _ in range(lenHeap):
            if rs is None:
                rs = ListNode(heap[0])
                cur = rs
            else:
                cur.next = ListNode(heap[0])
                cur = cur.next
            heap[0] = heap[lenHeap - 1]
            lenHeap -= 1
            self.heapify(heap, 0, lenHeap)
        print(rs)

    def heapify(self, heap: List[int], i: int, lenHeap: int):
        left, right = i * 2 + 1, i * 2 + 2
        if left < lenHeap and right < lenHeap:
            if heap[left] < heap[right]:
                if heap[left] < heap[i]:
                    temp = heap[i]
                    heap[i] = heap[left]
                    heap[left] = temp
                    self.heapify(heap, left, lenHeap)
            elif heap[right] < heap[i]:
                temp = heap[i]
                heap[i] = heap[right]
                heap[right] = temp
                self.heapify(heap, right, lenHeap)
        elif left < lenHeap and heap[left] < heap[i]:
            temp = heap[i]
            heap[i] = heap[left]
            heap[left] = temp


l1 = [[1,4,5],[1,3,4],[2,6]]
l1 = [ListNode.makeList(e) for e in l1]
Solution().mergeKLists(l1)