from typing import Dict, Optional, Self, no_type_check


class ListNode:

    def __init__(self, key: int, value: int, prev: Optional[Self] = None, next: Optional[Self] = None) -> None:
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

    def add_node(self, node: Self) -> None:
        self.next = node
        node.prev = self

    def break_node(self) -> None:
        if self.prev is not None and self.next is not None:
            self.prev.next = self.next
            self.next.prev = self.prev
            self.prev, self.next = None, None
        elif self.prev is not None:
            self.prev.next = None
            self.prev = None
        elif self.next is not None:
            self.next.prev = None
            self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.CAPACITY = capacity
        self.__D: Dict[int, ListNode] = {}
        self.__head: Optional[ListNode] = None
        self.__tail: Optional[ListNode] = None

    def get(self, key: int) -> int:
        if key not in self.__D:
            return -1
        NODE = self.__D[key]
        if NODE == self.__tail:
            return NODE.value
        if NODE == self.__head:
            self.__head = self.__head.next  # type: ignore
        NODE.break_node()
        self.__set_tail(NODE)
        return NODE.value

    def put(self, key: int, value: int) -> None:
        # empty cache
        if self.__head is None and self.__tail is None:
            NODE = ListNode(key, value)
            self.__head, self.__tail = NODE, NODE
            self.__D[key] = NODE
            return

        if key in self.__D:
            NODE = self.__D[key]
            NODE.value = value
            if NODE == self.__tail:
                return
            if NODE == self.__head:
                self.__head = self.__head.next  # type: ignore
            NODE.break_node()
            self.__set_tail(NODE)
            return

        if len(self.__D) < self.CAPACITY:
            NODE = ListNode(key, value)
            self.__D[key] = NODE
            self.__set_tail(NODE)
            return

        NODE = ListNode(key, value)
        self.__D[key] = NODE
        if self.CAPACITY == 1:
            self.__D.clear()
            self.__head, self.__tail = NODE, NODE
            self.__D[key] = NODE
            return

        old_head = self.__head
        self.__head = self.__head.next  # type: ignore
        del self.__D[old_head.key]  # type: ignore
        self.__set_tail(NODE)

    @no_type_check
    def __set_tail(self, NODE: ListNode):
        self.__tail.add_node(NODE)
        self.__tail = NODE


obj = LRUCache(2)

fns = ["put", "put", "get", "put", "get", "put", "get", "get", "get"]
params = [[1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

for fn, param in zip(fns, params):
    print(getattr(obj, fn)(*param))
