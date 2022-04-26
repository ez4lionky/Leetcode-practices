from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        s_xy, s_xz, s_yz = 0, [0]*n, 0
        for i in range(n):
            max_r = 0
            for j in range(n):
                if grid[i][j] > 0:
                    s_xy += 1
                if grid[i][j] > max_r:
                    max_r = grid[i][j]
                if grid[i][j] > s_xz[j]:
                    s_xz[j] = grid[i][j]
            s_yz += max_r
        return s_xy + s_yz + sum(s_xz)

if __name__ == "__main__":
    sol = Solution()
    grid = [[1,2],[3,4]]
    print(sol.projectionArea(grid))

