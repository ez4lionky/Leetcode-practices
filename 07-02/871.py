import heapq


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        res, fuel, prev, h, n = 0, startFuel, 0, [], len(stations)
        for i in range(n + 1):
            cur = stations[i][0] if i < n else target
            fuel -= cur - prev
            while fuel < 0 and len(h):
                res += 1
                fuel -= heapq.heappop(h)
            if fuel < 0:
                return -1
            if i < n:
                heapq.heappush(h, -stations[i][1])
                prev = cur
        return res

