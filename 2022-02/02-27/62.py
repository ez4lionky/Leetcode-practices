# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         res = [[1] * n for _ in range(m)]
#         for i in range(m):
#             for j in range(n):
#                 if i>0 and j>0:
#                     res[i][j] = res[i-1][j] + res[i][j-1]
#                 elif i>0:
#                     res[i][j] = res[i-1][j]
#                 elif j>0:
#                     res[i][j] = res[i][j-1]
#         return res[m-1][n-1]


# advanced version
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for i in range(n)] for j in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[m - 1][n - 1]


if __name__ == "__main__":
    sol = Solution()
    m = 3
    n = 7
    print(sol.uniquePaths(m, n))

