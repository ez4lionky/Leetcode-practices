from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid
        return start


if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,5,6]
    # target = 5
    # target = 2
    target = 7
    print(sol.searchInsert(nums, target))

