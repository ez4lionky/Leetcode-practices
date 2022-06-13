class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res = 0
        for i in points:
            for j in points:
                for k in points:
                    area = abs((j[0] - i[0])*(k[1] - i[1]) - (k[0] - i[0]) * (j[1] - i[1])) / 2
                    if area > res:
                        res = area
        return res

