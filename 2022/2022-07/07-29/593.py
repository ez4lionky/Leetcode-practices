import math
from typing import List


class Solution:
    def sub(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def close(n1, n2, epsilon=10e-6):
            if abs(n1-n2) < epsilon:
                return True
            return False

        def dis(p0, p1):
            return math.sqrt((p1[0] - p0[0]) ** 2 + (p1[1] - p0[1]) ** 2)
        dis1, dis2, dis3 = dis(p1, p2), dis(p1, p3), dis(p1, p4)
        s = list(set((dis1, dis2, dis3)))
        # print(dis1, dis2, dis3)
        # print(len(s))
        if len(s) == 2 and (close(s[0], math.sqrt(2) * s[1]) or close(s[0] * math.sqrt(2), s[1])):
            return True
        return False

    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        return self.sub(p1, p2, p3, p4) and self.sub(p2, p1, p3, p4) and self.sub(p3, p1, p2, p4) and self.sub(p4, p1, p2, p3)

if __name__ == "__main__":
    sol = Solution()
    # p1 = [1, 0]
    # p2 = [-1, 0]
    # p3 = [0, 1]
    # p4 = [0, -1]

    p1=[0,0]
    p2=[1,1]
    p3=[1,0]
    p4=[1,1]

    print(sol.validSquare(p1, p2, p3, p4))

