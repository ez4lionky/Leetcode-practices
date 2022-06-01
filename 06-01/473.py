from typing import *


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        perimeter = sum(matchsticks)
        if perimeter % 4 != 0:
            return False
        l = perimeter // 4
        matchsticks.sort(reverse=True)
        edges = [0] * 4
        def dfs(idx: int) -> bool:
            if idx == len(matchsticks):
                return True
            for i in range(4):
                edges[i] += matchsticks[idx]
                if edges[i] <= l and dfs(idx + 1):
                    return True
                edges[i] -= matchsticks[idx]
            return False
        return dfs(0)

