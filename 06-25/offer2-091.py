from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dps = costs[0]
        for i in range(1, len(costs)):
            dps = [min(dps[(j-1)%3], dps[(j+1)%3]) + c for j, c in enumerate(costs[i])]
        return min(dps)


if __name__ == "__main__":
    sol = Solution()
    costs = [[17,2,17],[16,16,5],[14,3,19]]
    print(sol.minCost(costs))

