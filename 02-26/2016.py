from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        pre_min, max_diff = nums[0], 0
        for i in range(1, len(nums)):
            if max_diff < (nums[i] - pre_min):
                max_diff = nums[i] - pre_min
            elif nums[i] < pre_min:
                pre_min = nums[i]
        return max_diff if max_diff else -1


if __name__ == "__main__":
    sol = Solution()
    # nums = [1,5,2,10]
    # nums = [9,4,3,2]
    nums = [87,68,91,86,58,63,43,98,6,40]
    print(sol.maximumDifference(nums))

