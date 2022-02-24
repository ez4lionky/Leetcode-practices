from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dis = [[0] * n] * m
        return dis


if __name__ == "__main__":
    sol = Solution()
    mat = [[0,0,0],[0,1,0],[0,0,0]]
    print(mat)

