import random


class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.d = {}

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.d[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        pos = self.d[val]
        del self.d[val]
        self.vals[pos], self.vals[-1] = self.vals[-1], self.vals[pos]
        self.vals.pop()
        if pos < len(self.vals):
            self.d[self.vals[pos]] = pos

        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)
