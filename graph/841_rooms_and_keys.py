from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited: set[int] = set()
        current_keys = [0]
        while len(current_keys) > 0:
            key = current_keys.pop(0)
            if key in visited:
                continue
            visited.add(key)
            current_keys.extend(rooms[key])
        return len(visited) == len(rooms)
