from typing import List
from random import choice
from collections import defaultdict


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.idx_set = defaultdict(list)
        for i, n in enumerate(nums):
            self.idx_set[n].append(i)

    def pick(self, target: int) -> int:
        return choice(self.idx_set[target])

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
