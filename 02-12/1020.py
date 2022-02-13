from typing import List
from collections import deque


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        queue = deque()
        m, n = len(grid), len(grid[0])
        for i, row in enumerate(grid):
            if row[0]:
                grid[i][0] = 0
                queue.append((i, 0))
            if row[n-1]:
                grid[i][n-1] = 0
                queue.append((i, n-1))
        for j in range(1, n-1):
            if grid[0][j]:
                grid[0][j] = 0
                queue.append((0, j))
            if grid[m-1][j]:
                grid[m-1][j] = 0
                queue.append((m-1, j))

        offsets = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while queue:
            size = len(queue)
            for _ in range(size):
                u, v = queue.popleft()
                for x, y in offsets:
                    if 0<=u+x<m and 0<=v+y<n and grid[u+x][v+y]:
                        grid[u+x][v+y] = 0
                        queue.append((u+x, v+y))
        res = sum([sum(g) for g in grid])
        return res


if __name__ == "__main__":
    sol = Solution()
    # grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
    grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
    print(sol.numEnclaves(grid))

