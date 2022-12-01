class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dist, res = 10**9, -1
        for i, p in enumerate(points):
            if (p[0] == x or p[1] == y):
                cur_dist = abs(p[0] - x) + abs(p[1] - y)
                if cur_dist < dist:
                    dist = cur_dist
                    res = i
        return res

