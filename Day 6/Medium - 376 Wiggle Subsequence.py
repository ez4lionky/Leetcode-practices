# My primary idea of solution is:
# use a stack to delete the jarring number, the nums left in stack is the wiggle sequence.
# This method is not implemented and validated.
# Here is the implementation of state machine.


class Solution:
    def wiggleMaxLength(self, nums: [int]) -> int:
        if len(nums) < 2:
            return len(nums)
        state = 0  # BEGIN = 0 UP = 1 DOWN = 2
        max_len = 1
        for i in range(1, len(nums)):
            if state == 0:
                if nums[i - 1] < nums[i]:
                    state = 1
                    max_len += 1
                elif nums[i - 1] > nums[i]:
                    state = 2
                    max_len += 1
                continue

            if state == 1:
                if nums[i - 1] > nums[i]:
                    state = 2
                    max_len += 1
                continue

            if state == 2:
                if nums[i - 1] < nums[i]:
                    state = 1
                    max_len += 1
                continue

        return max_len


sol = Solution()
nums = [1, 7, 4, 9, 2, 5]
print(sol.wiggleMaxLength(nums))
nums = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
print(sol.wiggleMaxLength(nums))
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sol.wiggleMaxLength(nums))
nums = [0, 0]
print(sol.wiggleMaxLength(nums))
