from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid
        return -1


if __name__ == "__main__":
    sol = Solution()
    nums = [-1,0,3,5,9,12]
    target = 9
    print(sol.search(nums, target))

