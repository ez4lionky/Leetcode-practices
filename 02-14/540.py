from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if mid%2==0:
                if nums[mid]==nums[mid+1]:
                    start = mid + 1
                else:
                    end = mid
            else:
                if nums[mid-1]==nums[mid]:
                    start = mid + 1
                else:
                    end = mid
        return nums[start]
        # 0,8,4 -> 4,8,6 -> 4,6,5
        # 0,6,3 -> 3,6,4

    # def singleNonDuplicate(self, nums: List[int]) -> int:
    #     low, high = 0, len(nums) - 1
    #     while low < high:
    #         mid = (low + high) // 2
    #         if nums[mid] == nums[mid ^ 1]:
    #             low = mid + 1
    #         else:
    #             high = mid
    #     return nums[low]



if __name__ == "__main__":
    sol = Solution()
    # nums = [1,1,3,3,4,5,5,8,8]
    # nums = [1,1,3,3,4,4,5,8,8]
    # nums = [1,1,2,3,3,4,4,8,8]
    # nums = [3,3,7,7,10,11,11]
    # nums = [3,7,7,10,10,11,11]
    # nums = [3,3,7,7,10,11,11]
    # nums = [1]
    nums = [3,3,4,4,5,5,7,8,8,9,9]
    print(sol.singleNonDuplicate(nums))

