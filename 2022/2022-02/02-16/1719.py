from typing import List
from collections import defaultdict


# A pair [xi, yi] exists in pairs if and only if xi is an ancestor of yi or yi is an ancestor of xi
# cannot be sibling node, which means adj(xi) must in adj(parent(xi))
class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        adj = defaultdict(set)
        for x, y in pairs:
            adj[x].add(y)
            adj[y].add(x)
        max_d, root = max([(len(adj[k]), k) for k in adj.keys()])
        if max_d != (len(adj.keys())-1):
            return 0
        res = 1
        for k in adj.keys():
            if k == root:
                continue
            cur_d = len(adj[k])
            parent, parent_d = -1, len(adj.keys())
            for n in adj[k]:
                if cur_d <= len(adj[n]) < parent_d:
                    parent = n
                    parent_d = len(adj[n])
            # for any node x, anyone node n in adj(x) that has same degree, and adj(x) in adj(n)
            # means all of those nodes adj to each other, so only need to judge once
            # because adj is mutual?
            if parent == -1 or any([n not in adj[parent] for n in adj[k] if n != parent]):
                return 0
            if cur_d == parent_d:
                res = 2
        return res


if __name__ == "__main__":
    sol = Solution()
    # pairs = [[1,2],[2,3]]
    # pairs = [[1,2],[2,3],[1,3]]
    pairs = [[1,2],[2,3],[2,4],[1,5]]
    print(sol.checkWays(pairs))

