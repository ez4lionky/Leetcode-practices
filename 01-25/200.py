import collections


class Solution:
    def numIslands(self, grid) -> int:
        nr, nc = len(grid), len(grid[0])  # at least one row
        k = 0
        for i in range(nr):
            for j in range(nc):
                # BFS to iterate neighbouring grid and set visited, until no new grid will be visited
                if grid[i][j] == '1':
                    k += 1
                    queue = collections.deque([[i, j]])
                    grid[i][j] = '0'
                    while len(queue) != 0:
                        u, v = queue.popleft()
                        offset_xys = [[u, v - 1], [u, v + 1], [u - 1, v], [u + 1, v]]
                        for x, y in offset_xys:
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == '1':
                                    queue.append([x, y])
                                    grid[x][y] = '0'
        return k

if __name__ == "__main__":
    grid = [["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]
    sol = Solution()
    print(sol.numIslands(grid))

