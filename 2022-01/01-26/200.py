from collections import deque


class Solution:
    # def numIslands(self, grid) -> int:
    #     nr, nc = len(grid), len(grid[0])  # at least one row
    #     k = 0
    #     for i in range(nr):
    #         for j in range(nc):
    #             # BFS to iterate neighbouring grid and set visited, until no new grid will be visited
    #             if grid[i][j] == '1':
    #                 k += 1
    #                 queue = deque([[i, j]])
    #                 grid[i][j] = '0'
    #                 while len(queue) != 0:
    #                     u, v = queue.popleft()
    #                     offset_xys = [[u, v - 1], [u, v + 1], [u - 1, v], [u + 1, v]]
    #                     for x, y in offset_xys:
    #                         if 0 <= x < nr and 0 <= y < nc and grid[x][y] == '1':
    #                                 queue.append([x, y])
    #                                 grid[x][y] = '0'
    #     return k
    
    # DFS version
    def numIslands(self, grid) -> int:
        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0': return
            grid[i][j] = '0'
            dfs(grid, i - 1, j)
            dfs(grid, i + 1, j)
            dfs(grid, i, j - 1)
            dfs(grid, i, j + 1)
            return

        nr, nc = len(grid), len(grid[0])
        k = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == '1':
                    k += 1
                    dfs(grid, i, j)
        return k

if __name__ == "__main__":
    grid = [["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]
    sol = Solution()
    print(sol.numIslands(grid))

