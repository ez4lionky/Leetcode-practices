from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.q = deque(maxlen=size)
        self.s = 0

    def next(self, val: int) -> float:
        if len(self.q) < self.q.maxlen:
            self.s += val
            self.q.append(val)
        else:
            self.s -= self.q.popleft()
            self.q.append(val)
            self.s += val
        return self.s / len(self.q)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
