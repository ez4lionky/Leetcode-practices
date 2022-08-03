from typing import *
from random import randrange
from bisect import bisect_right


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.sums = [0]
        for a, b, x, y in rects:
            self.sums.append(self.sums[-1] + (x - a + 1) * (y - b + 1))


    def pick(self) -> List[int]:
        num = randrange(self.sums[-1])
        idx = bisect_right(self.sums, num)
        a, b, x, y = self.rects[idx-1]
        o1, o2 = divmod(num - self.sums[idx-1], x - a + 1)
        return a + o2, b + o1



# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
