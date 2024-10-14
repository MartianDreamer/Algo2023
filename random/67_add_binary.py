class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n_a = int(a, 2)
        n_b = int(b, 2)
        return "{0:b}".format(n_a + n_b)