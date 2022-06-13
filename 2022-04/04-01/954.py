from typing import List
from collections import Counter


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        c = Counter(arr)
        if c[0] % 2 != 0:
            return  False
        for v in sorted(c.keys(), key=abs):
            # print(v)
            if c[2*v] < c[v]:
                return False
            c[2*v] -= c[v]
        return True


if __name__ == "__main__":
    sol = Solution()
    arr = [3,1,3,6]
    arr = [4,-2,2,-4]
    print(sol.canReorderDoubled(arr))

