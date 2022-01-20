class Solution:
    def findMinArrowShots(self, points: [[int]]) -> int:
        points.sort()
        i = 0
        num = 0
        while i < len(points):
            interval = points[i]
            while i < len(points) - 1 and points[i+1][0] <= interval[1]:
                i += 1
                interval = [points[i][0], min(interval[1], points[i][1])]
            i += 1
            num += 1
        return num


sol = Solution()
points = [[10, 16], [2, 8], [1, 6], [7, 12]]
print(sol.findMinArrowShots(points))
points = [[1, 2], [2, 3], [3, 4], [4, 5]]
print(sol.findMinArrowShots(points))
