# class NumMatrix:
#
#     def __init__(self, matrix: List[List[int]]):
#         m, n = len(matrix), len(matrix[0])
#         dp = [[0 for _ in range(n)] for _ in range(m)]
#         dp[0][0] = matrix[0][0]
#         for i in range(1, m):
#             dp[i][0] = dp[i-1][0] + matrix[i][0]
#         for i in range(1, n):
#             dp[0][i] = dp[0][i-1] + matrix[0][i]
#         for i in range(1, m):
#             for j in range(1, n):
#                 dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + matrix[i][j]
#         self.m, self.n = m, n
#         self.dp = dp
#
#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         s = self.dp[row2][col2]
#         if row1 != 0 and col1 != 0:
#             s = s + self.dp[row1-1][col1-1] - self.dp[row1-1][col2] - self.dp[row2][col1-1]
#         elif row1 != 0:
#             s = s - self.dp[row1-1][col2]
#         elif col1 != 0:
#             s = s - self.dp[row2][col1-1]
#         return s


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), (len(matrix[0]) if matrix else 0)
        self.sums = [[0] * (n + 1) for _ in range(m + 1)]
        _sums = self.sums

        for i in range(m):
            for j in range(n):
                _sums[i + 1][j + 1] = _sums[i][j + 1] + _sums[i + 1][j] - _sums[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        _sums = self.sums

        return _sums[row2 + 1][col2 + 1] - _sums[row1][col2 + 1] - _sums[row2 + 1][col1] + _sums[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
