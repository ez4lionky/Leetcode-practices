from typing import *


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        p1, p2, p3 = points
        # k = (p2[1] - p1[1]) / (p2[0] - p1[0])
        # b = 
        # return not (p3[0] - p1[0]) / (p2[0] - p1[0]) == (p3[1] - p1[1]) / (p2[1] - p1[1])
        return not (p3[0] - p1[0]) * (p2[1] - p1[1]) == (p3[1] - p1[1]) * (p2[0] - p1[0])


if __name__ == "__main__":
    sol = Solution()
    points = [[1,1],[2,3],[3,2]]
    print(sol.isBoomerang(points))

