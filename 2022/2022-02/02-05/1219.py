from typing import List


class Solution:
    res = 0

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(i, j, grid, gold):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return
            gold += grid[i][j]
            self.res = max(self.res, gold)
            tmp = grid[i][j]
            grid[i][j] = 0
            dfs(i-1, j, grid, gold)
            dfs(i+1, j, grid, gold)
            dfs(i, j-1, grid, gold)
            dfs(i, j+1, grid, gold)
            grid[i][j] = tmp
            return

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    dfs(i, j, grid, 0)
        return self.res


if __name__ == "__main__":
    sol = Solution()
    # grid = [[0,6,0],[5,8,7],[0,9,0]]
    grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
    print(sol.getMaximumGold(grid))

