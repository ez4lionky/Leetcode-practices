from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(idx):
            if idx == len(nums):
                res.append(nums[:])
                return
            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                backtrack(idx+1)
                nums[idx], nums[i] = nums[i], nums[idx]
            return

        backtrack(0)
        return res


if __name__ == "__main__":
    sol = Solution()
    # nums = [1,2,3]
    nums = [0,1]
    print(sol.permute(nums))

