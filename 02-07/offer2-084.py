from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(idx):
            if idx == len(nums):
                res.append(nums[:])
                return
            swaped = set()
            for i in range(idx, len(nums)):
                if nums[i] in swaped:
                    continue
                swaped.add(nums[i])
                nums[idx], nums[i] = nums[i], nums[idx]
                backtrack(idx+1)
                nums[idx], nums[i] = nums[i], nums[idx]

        backtrack(0)
        return res


if __name__ == "__main__":
    sol = Solution()
    # nums = [1,1,2]
    nums = [0,1,0,0,9]
    # [[0,1,0,0,9],[0,1,0,9,0],[0,1,9,0,0],[0,0,1,0,9],[0,0,1,9,0],
    # [0,0,0,1,9],[0,0,0,9,1],[0,0,9,0,1],[0,0,9,1,0],[0,9,0,0,1],
    # [0,9,0,1,0],[0,9,1,0,0],[1,0,0,0,9],[1,0,0,9,0],[1,0,9,0,0],
    # [1,9,0,0,0],[9,1,0,0,0],[9,0,1,0,0],[9,0,0,1,0],[9,0,0,0,1]]
    print(sol.permuteUnique(nums))

