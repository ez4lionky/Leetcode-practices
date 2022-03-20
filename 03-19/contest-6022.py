import heapq
from typing import List


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        s, res, diff = sum(nums), 0, 0
        h = []
        for n in nums:
            heapq.heappush(h, -n)
        while s/2 > diff:
            n = heapq.heappop(h)
            n /= 2
            diff += -n
            heapq.heappush(h, n)
            res += 1
        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [5,19,8,1]
    print(sol.halveArray(nums))

