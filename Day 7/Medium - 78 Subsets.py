# Recursive method and loop method.
# Notation: the append() of list is appending the reference, so we need the copy() before append.
# The problem also can be solved by using Bit operation.


class Solution:
    # def subsets(self, nums: [int]) -> [[int]]:
    #     res = [[]]
    #     for num in nums:
    #         for temp in res[:]:
    #             x = temp[:]
    #             x.append(num)
    #             res.append(x)
    #     return res
    def __init__(self):
        self.result = []

    def subsets(self, nums: [int]) -> [[int]]:
        i = 0
        item = []
        self.result.append(item)
        self.generate(i, nums, item)
        return self.result

    def generate(self, i, nums, item):
        if i >= len(nums):
            return
        item.append(nums[i])
        self.result.append(item.copy())
        self.generate(i + 1, nums, item)
        item.pop(-1)
        self.generate(i + 1, nums, item)

    # def subsets(self, nums: [int]) -> [[int]]:
    #     items = []
    #     max_value = 1 << len(nums)
    #     for i in range(max_value):
    #         item = []
    #         for j in range(len(nums)):
    #             if i & 1 << j:
    #                 item.append(nums[j])
    #         items.append(item)
    #     return items


nums = [1, 2, 3]
sol = Solution()
print(sol.subsets(nums))
