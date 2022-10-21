from collections import deque


class StockSpanner:

    def __init__(self):
        self.prices = deque()
        self.index = -1

    def next(self, price: int) -> int:
        self.index += 1
        while self.prices and price >= self.prices[-1][0]:
            _ = self.prices.pop()
        if len(self.prices) == 0:
            res = self.index + 1
        else:
            res = self.index - self.prices[-1][1]
        self.prices.append([price, self.index])
        return res

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
