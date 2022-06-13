from typing import List
from itertools import product


# brute force
# class Solution:
#     def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
#         m, n = len(img), len(img[0])
#         res = [[0 for _ in range(n)] for _ in range(m)]
#         for i in range(m):
#             for j in range(n):
#                 s, num = 0, 0
#                 for x in range(-1, 2):
#                     for y in range(-1, 2):
#                         if 0<=i+x<m and 0<=j+y<n:
#                             s += img[i+x][j+y]
#                             num += 1
#                 res[i][j] = s // num
#         return res


# presum
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        presum = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                presum[i][j] = presum[i-1][j] + presum[i][j-1] - presum[i-1][j-1] + img[i-1][j-1]
        res = [[0] * n for _ in range(m)]
        for i, j in product(range(m), range(n)):
            a, b = max(0, i - 1), max(0, j - 1)
            c, d = min(m - 1, i + 1), min(n - 1, j + 1)
            cnt = (c - a + 1) * (d - b + 1)
            tot = presum[c + 1][d + 1] - presum[a][d + 1] - presum[c + 1][b] + presum[a][b]
            res[i][j] = tot // cnt
        return res
 

if __name__ == "__main__":
    sol = Solution()
    img = [[100,200,100],[200,50,200],[100,200,100]]
    print(sol.imageSmoother(img))

