from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = self.search(nums, target)
        if res == -1:
            return [-1, -1]
        left, right = res, res
        while left > 0:
            if nums[left-1] == target:
                left -= 1
            else: break

        while right < len(nums)-1:
            if nums[right+1] == target:
                right += 1
            else: break

        return [left, right]

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
    nums = [5,7,7,8,8,10]
    # nums = [5,7,8,8,8,10]
    target = 8
    print(sol.searchRange(nums, target))

