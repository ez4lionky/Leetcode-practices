from collections import Counter
from typing import List



class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        s_t, s_a = Counter(target), Counter(arr)
        if s_t != s_a:
            return False
        return True


if __name__ == "__main__":
    sol = Solution()
    target, arr = [1, 2, 2, 3], [1, 1, 2, 3]
    print(sol.canBeEqual(target, arr))

