import random


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius, self.x_center, self.y_center = radius, x_center, y_center

    def randPoint(self) -> List[float]:
        xc, yc, r = self.x_center, self.y_center, self.radius
        x, y = random.uniform(xc-r, xc+r), random.uniform(yc-r, yc+r)
        while (x - xc) ** 2 + (y - yc) ** 2 > r:
            x, y = random.uniform(xc-r, xc+r), random.uniform(yc-r, yc+r)
        return x, y



# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
