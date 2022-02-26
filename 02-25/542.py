from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dis = [[-1] * n for _ in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dis[i][j] = 0
                    queue.append((i, j))
        step = 0
        while queue:
            size = len(queue)
            step += 1
            for _ in range(size):
                r, c = queue.popleft()
                for x, y in [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]:
                    if 0<=x<m and 0<=y<n and dis[x][y] == -1:
                        dis[x][y] = step
                        queue.append((x, y))
        return dis


if __name__ == "__main__":
    sol = Solution()
    mat = [[0,0,0],[0,1,0],[0,0,0]]
    # mat = [[0,0,0],[0,1,0],[1,1,1]]
    print(sol.updateMatrix(mat))

