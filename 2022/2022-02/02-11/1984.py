from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums.sort()
        res = min([nums[i+k-1] - nums[i] for i in range(0, len(nums)-k+1)])
        return res


if __name__ == "__main__":
    sol = Solution()
    # nums = [90]
    # k = 1
    nums = [9,4,1,7]
    k = 2
    print(sol.minimumDifference(nums, k))

