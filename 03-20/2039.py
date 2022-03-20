from typing import List
from collections import defaultdict
import heapq


class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        # dijkstra
        nodes = set()
        es = defaultdict(list)
        for e0, e1 in edges:
            nodes.add(e0)
            nodes.add(e1)
            es[e0].append((e0, e1))
            es[e1].append((e1, e0))

        n = len(nodes)
        dist = [0 if _ == 0 else 10**6 for _ in range(n)]
        visited = set()
        hq = [(0, 0)]
        while hq:
            d, v = heapq.heappop(hq)
            if v in visited:
                continue
            visited.add(v)
            for e0, e1 in es[v]:
                if d + 1 < dist[e1]:
                    dist[e1] = d + 1
                    heapq.heappush(hq, (d+1, e1))
        res = 0
        for i in range(1, n):
            if (2 * dist[i]) % patience[i] == 0:
                res = max(res, 4 * dist[i] - patience[i])
            else:
                res = max(res, 4 * dist[i] - (2 * dist[i]) % patience[i])
        return res + 1

