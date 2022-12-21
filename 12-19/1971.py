from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        fa = list(range(n))
        def find(x):
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]
        for u, v in edges:
            fa[find(u)] = find(v)
        return find(source) == find(destination)
        
if __name__ == "__main__":
    sol = Solution()
    n = 3
    edges = [[0,1],[1,2],[2,0]]
    source = 0
    destination = 2
    print(sol.validPath(n, edges, source, destination))

