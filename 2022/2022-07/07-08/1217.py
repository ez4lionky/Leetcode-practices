from collections import Counter


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        c = Counter([p % 2 for p in position])
        return min(c[0], c[1])

