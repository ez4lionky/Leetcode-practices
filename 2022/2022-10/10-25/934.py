from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        s_t = [-1, -1]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    s_t = [i, j]
                    grid[i][j] = -1
                    break
            if s_t != [-1, -1]:
                break
        
        q = deque([s_t])
        visited = deque([s_t])
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for r_offset, c_offset in [[0, 1], [-1, 0], [0, -1], [1, 0]]:
                    n_r, n_c = r+r_offset, c+c_offset
                    if 0<=n_r<n and 0<=n_c<n and grid[n_r][n_c]==1:
                        grid[n_r][n_c] = -1
                        q.append([n_r, n_c])
                        visited.append([n_r, n_c])
        d = -1
        while visited:
            d += 1
            for i in range(len(visited)):
                r, c = visited.popleft()
                for r_offset, c_offset in [[0, 1], [-1, 0], [0, -1], [1, 0]]:
                    n_r, n_c = r+r_offset, c+c_offset
                    if 0<=n_r<n and 0<=n_c<n and grid[n_r][n_c]==0:
                        visited.append([n_r, n_c])
                        grid[n_r][n_c] = -1
                    elif 0<=n_r<n and 0<=n_c<n and grid[n_r][n_c]==1:
                        return d

