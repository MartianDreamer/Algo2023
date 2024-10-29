class StockSpanner:

    def __init__(self):
        self.m_stack: list[tuple[int, int]] = []

    def next(self, price: int) -> int:
        count = 1
        while len(self.m_stack) > 0 and self.m_stack[-1][0] <= price:
            (_, tail_count) = self.m_stack.pop()
            count += tail_count
        self.m_stack.append((price, count))
        return count
