from typing import List


class Solution:
    # def findMin(self, nums: List[int]) -> int:
    #     start, end = 0, len(nums) - 1
    #     if nums[start] <= nums[end]:
    #         return nums[start]
    #     while start < end:
    #         mid = (start + end) // 2
    #         if nums[start] < nums[mid]:
    #             start = mid
    #         elif nums[start] > nums[mid]:
    #             end = mid
    #         else:
    #             if nums[start] > nums[end]:
    #                 start = end
    #             else:
    #                 end = start
    #     return nums[start]

    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[end] > nums[mid]:
                end = mid
            else:
                start = mid + 1
        return nums[start]


if __name__ == "__main__":
    sol = Solution()
    nums = [3,4,5,1,2]
    # nums = [12, 11]
    # nums = [4,5,6,7,0,1,2]
    print(sol.findMin(nums))

