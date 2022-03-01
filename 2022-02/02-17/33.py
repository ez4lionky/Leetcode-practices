from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

    # def search(self, nums: List[int], target: int) -> int:
    #     min_idx = min(range(len(nums)), key=nums.__getitem__)
    #     if min_idx == 0:
    #         return self.binary_search(nums, target)
    #     r_value = nums[0]
    #     nums = nums[min_idx:] + nums[:min_idx]
    #     res = self.binary_search(nums, target)
    #     if res == -1:
    #         return -1
    #     if r_value <= target:
    #         return res - len(nums) + min_idx
    #     return res + min_idx
    # 
    # def binary_search(self, nums, target):
    #     start, end = 0, len(nums) - 1
    #     while start <= end:
    #         mid = (start + end) // 2
    #         if nums[mid] < target:
    #             start = mid + 1
    #         elif nums[mid] > target:
    #             end = mid - 1
    #         else:
    #             return mid
    #     return -1


if __name__ == "__main__":
    sol = Solution()
    # nums = [4,5,6,7,0,1,2]
    # target = 0
    # target = 6
    # nums = [3,5,1]
    # target = 3
    # nums = [1]
    # target = 1
    # nums = [1,3]
    # target = 3
    nums = [5,1,3]
    target = 3
    print(sol.search(nums, target))

