from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return True
            # nums[start] == nums[mid] means start==mid or (nums[start:mid+1] or nums[mid:] are all the same)

            if nums[start] < nums[mid] or start == mid:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[start] > nums[mid]:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                is_dup = True
                init = nums[start]
                for i in range(start, mid+1):
                    if nums[i] != init:
                        is_dup = False
                if is_dup:
                    start = mid + 1
                else:
                    end = mid - 1
        return False


if __name__ == "__main__":
    sol = Solution()
    # nums = [2,5,6,0,0,1,2]
    # target = 0
    # target = 3
    nums = [1,0,1,1,1]
    target = 0
    print(sol.search(nums, target))

