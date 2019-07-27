# Recursive method and loop method.
# Notation: the append() of list is appending the reference, so we need the copy() before append.


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


nums = [1, 2, 3]
sol = Solution()
print(sol.subsets(nums))
