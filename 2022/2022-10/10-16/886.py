from collections import defaultdict, deque

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        colors = [0] * n
        edges = [[] for _ in range(n)]
        for x, y in dislikes:
            edges[x - 1].append(y - 1)
            edges[y - 1].append(x - 1)
        # edges = defaultdict(list)
        # for d in dislikes:
        #     edges[d[0]-1].append(d[1]-1)
        #     edges[d[1]-1].append(d[0]-1)
        for i, c in enumerate(colors):
            if c == 0:
                q = deque([i])
                colors[i] = 1
                while q:
                    f = q.popleft()
                    for n in edges[f]:
                        if colors[f] == colors[n]:
                            return False
                        if colors[n] == 0:
                            colors[n] = -colors[f]
                            q.append(n)
        return True

# class Solution:
#     def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
#         colors = [0] * n
#         for d in dislikes:
#             cur_c = colors[d[0]-1]
#             if cur_c == 0:
#                 colors[d[0]-1] = 1
#             neighbor_c = colors[d[1]-1]
#             if neighbor_c != 0 and neighbor_c == cur_c:
#                 return False
#             else:
#                 colors[d[1]-1] = -cur_c
#         return True

