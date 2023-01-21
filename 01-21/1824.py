from collections import deque


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        dist = [[n]*3 for _ in range(n)]
        dist[0][1] = 0
        q = deque([(0, 1)])
        while True:
            i, j = q.popleft()
            d = dist[i][j]
            if i == n-1: return d
            if obstacles[i+1] != j+1 and d<dist[i+1][j]:
                dist[i+1][j] = d
                q.appendleft((i + 1, j))
            for k in (j+1)%3, (j+2)%3:
                if obstacles[i] != k + 1 and d + 1 < dist[i][k]:
                    dist[i][k] = d + 1
                    q.append((i, k))


