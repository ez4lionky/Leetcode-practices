from typing import *


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        m, n = len(mat), len(mat[0])
        for i in range(m + n - 1):
            if i % 2:
                x = 0 if i < n else i - n + 1
                y = i if i < n else n - 1
                while x < m and y >= 0:
                    ans.append(mat[x][y])
                    x += 1
                    y -= 1
            else:
                x = i if i < m else m - 1
                y = 0 if i < m else i - m + 1
                while x >= 0 and y < n:
                    ans.append(mat[x][y])
                    x -= 1
                    y += 1
        return ans


# class Solution:
#     def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
#         res = []
#         m, n = len(mat), len(mat[0])
#         for i in range(0, m+n-1):
#             cur = []
#             for j in range(0, min(i+1, m)):
#                 k = i - j
#                 if k >= 0 and k < n:
#                     cur.append(mat[j][k])
#             if i % 2 == 0:
#                 res.extend(cur[::-1])
#             else:
#                 res.extend(cur)
#         return res
        

if __name__ == "__main__":
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    sol = Solution()
    print(sol.findDiagonalOrder(mat))

