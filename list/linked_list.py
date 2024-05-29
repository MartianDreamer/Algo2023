from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def makeList(cls, nums: List[int]):
        if nums is None or len(nums) == 0:
            return None
        head = cls(nums[0], None)
        cur = head
        for e in nums[1:]:
            next = cls(e, None)
            cur.next = next
            cur = cur.next
        return head
    
    def __str__(self) -> str:
        rs = "["
        cur = self
        while cur is not None:
            rs += str(cur.val)
            if cur.next is not None:
                rs += ", "
            cur = cur.next
        rs += "]"
        return rs

if __name__ == "__main__":
    nodeList = ListNode.makeList([1,2,3,4,5,6,7,8,9,10])
    print(nodeList)