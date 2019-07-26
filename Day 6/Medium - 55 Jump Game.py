# My primary solution is to find the next jump by look ahead 1 (calculate the farthest jump).
# Here is a more explicit implementation, which refers to the video in Bilibili.


class Solution:
    def canJump(self, nums: [int]) -> bool:
        jump = 0
        max_index = nums[0]
        index = []
        for i in range(len(nums)):
            index.append(i + nums[i])
        while jump < len(nums) and jump <= max_index:
            if max_index < index[jump]:
                max_index = index[jump]
            jump += 1
        if max_index < len(nums) - 1:
            return False
        return True


sol = Solution()
nums = [2, 3, 1, 1, 4]
print(sol.canJump(nums))
nums = [3, 2, 1, 0, 4]
print(sol.canJump(nums))
