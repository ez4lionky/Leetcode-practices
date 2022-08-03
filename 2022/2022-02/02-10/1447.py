from typing import List
from math import gcd


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        for i in range(2, n+1):
            for j in range(1, i):
                if gcd(i, j) == 1:
                    res.append(f'{j}/{i}')
        return res


if __name__ == "__main__":
    sol = Solution()
    n = 4
    print(sol.simplifiedFractions(n))

