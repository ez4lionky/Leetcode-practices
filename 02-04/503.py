from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [-1] * length
        stack = []
        for i in range(length * 2 - 1):
            idx = i % length
            if len(stack) == 0 or nums[idx] <= nums[stack[-1]]:
                stack.append(idx)
            else:
                while len(stack) != 0 and nums[idx] > nums[stack[-1]]:
                    t_idx = stack.pop()
                    res[t_idx] = nums[idx]
                stack.append(idx)
        return res

    # def nextGreaterElements(self, nums: List[int]) -> List[int]:
    #     length = len(nums)
    #     nums = nums * 2
    #     res = [-1] * (length * 2)
    #     stack = []
    #     for i in range(length * 2):
    #         if len(stack) == 0 or nums[i] <= nums[stack[-1]]:
    #             stack.append(i)
    #         else:
    #             while len(stack) != 0 and nums[i] > nums[stack[-1]]:
    #                 idx = stack.pop()
    #                 res[idx] = nums[i]
    #             stack.append(i)
    #     return res[:length]
    #

if __name__ == "__main__":
    # nums = [1,2,1]
    nums = [1,2,3,4,3]
    sol = Solution()
    print(sol.nextGreaterElements(nums))

