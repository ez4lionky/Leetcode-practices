from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        for i, row in enumerate(mat):
            cnt = sum(row)
            if cnt:
                for j, v in enumerate(row):
                    if v == 1:
                        mat[0][j] += cnt - (i==0)
        return sum(v == 1 for v in mat[0])


if __name__ == "__main__":
    sol = Solution()
    mat = [[1,0,0],
            [0,1,0],
            [0,0,1]]
    print(sol.numSpecial(mat))

