from typing import List


# class Solution:
#     def findBall(self, grid: List[List[int]]) -> List[int]:
#         m, n = len(grid), len(grid[0])
#         res = [-1] * n
#         def dfs(bi, r, c):
#             if r == m:
#                 res[bi] = c
#                 return
#             if (c == 0 and grid[r][c] == -1) or (c == n-1 and grid[r][c] == 1):
#                 res[bi] = -1
#                 return
#             if grid[r][c] == 1:
#                 if grid[r][c+1] == -1:
#                     res[bi] = -1
#                     return
#                 else:
#                     dfs(bi, r+1, c+1)
#             if grid[r][c] == -1:
#                 if grid[r][c-1] == 1:
#                     res[bi] = -1
#                     return
#                 else:
#                     dfs(bi, r+1, c-1)
#             return
#
#         for j in range(len(grid[0])):
#             dfs(j, 0, j)
#         return res


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])

        def fn(j):
            for i in range(m):
                temp = j + grid[i][j]
                if 0 > temp or temp >= n or grid[i][temp] + grid[i][j] == 0:
                    return -1
                j = temp
            return j
        
        res = list(fn(k) for k in range(n))
        return res


if __name__ == "__main__":
    sol = Solution()
    # grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
    # grid = [[-1]]
    grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
    print(sol.findBall(grid))

