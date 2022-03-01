from itertools import chain
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         r = numRows
#         if r == 1 or r >= len(s):
#             return s
#         mat = [[] for _ in range(r)]
#         t, x = r * 2 - 2, 0
#         for i, ch in enumerate(s):
#             mat[x].append(ch)
#             x += 1 if i % t < r - 1 else -1
#         return ''.join(chain(*mat))


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        res = []
        n, t = len(s), 2 * numRows - 2
        for i in range(numRows):
            for j in range(0,n-i,t):
                res.append(s[i+j])
                if 0<i<numRows-1 and j+t-i<n:
                    res.append(s[j+t-i])
        return ''.join(res)


if __name__ == "__main__":
    sol = Solution()
    s = "PAYPALISHIRING"
    numRows = 4
    print(sol.convert(s, numRows))

