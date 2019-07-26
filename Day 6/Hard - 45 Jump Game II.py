# It is similar to the primary solution of 55.
# Find the next jump by look ahead 1 (calculate the farthest jump), which is similar to the solution in Bilibili.
# Here is the faster implementation. (embedding the jump into the traversal)


class Solution:
    def jump(self, nums: [int]) -> int:
        if len(nums) < 2:
            return 0
        jump_min = 1
        limit = nums[0]
        max_index = nums[0] + 0
        for i in range(len(nums)):
            if i > limit:
                jump_min += 1
                limit = max_index
            if max_index < nums[i] + i:
                max_index = nums[i] + i
        return jump_min


sol = Solution()
nums = [2, 3, 1, 1, 4]
print(sol.jump(nums))
