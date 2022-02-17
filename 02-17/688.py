from functools import lru_cache


# class Solution:
#     def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
#         @functools.lru_cache(None)
#         def dfs(r, c, counts):
#             if r < 0 or r > N - 1 or c < 0 or c > N - 1:
#                 return 0
#             if counts == K:
#                 return 1
#             step = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
#             res = 0
#             for i, j in step:
#                 res += dfs(r + i, c + j, counts + 1)
#             return res / 8

#         return dfs(r, c, 0)


class Solution:
    offsets = [[-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2]]
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        @lru_cache(None)
        def dfs(r, c, step):
            if (step == k) or r<0 or r>=n or c<0 or c>=n:
                if step==k and 0<=r<n and 0<=c<n:
                    return 1
                return 0
            res = 0
            for x, y in self.offsets:
                res += dfs(r+x, c+y, step+1)
            return res/8
        return dfs(row, column, 0)

# class Solution:
#     num = 0
#     on_chess = 0
#     offsets = [[-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2]]
#     def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
#         @lru_cache(None)
#         def dfs(r, c, step):
#             if (step == k) or r<0 or r>=n or c<0 or c>=n:
#                 # if changed self.num = 8**k to self.num += 1, will be wrong
#                 # self.num += 1
#                 if step==k and 0<=r<n and 0<=c<n:
#                     self.on_chess += 1
#                 return
#             for x, y in self.offsets:
#                 dfs(r+x, c+y, step+1)
#             return
#         dfs(row, column, 0)
#         self.num = 8**k
#         print(self.on_chess, self.num)
#         return self.on_chess / self.num


if __name__ == "__main__":
    sol = Solution()
    n = 3
    k = 2
    # n = 1
    # k = 0
    row = 0
    column = 0
    print(sol.knightProbability(n, k, row, column))

