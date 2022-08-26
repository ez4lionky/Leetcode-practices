# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         res = 0
#         l = len(nums)
#         for i in range(l):
#             for j in range(i+1, l):
#                 product = (nums[i] - 1) * (nums[j] - 1)
#                 if product > res:
#                     res = product
#         return res


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a, b = nums[0], nums[1]
        if a < b:
            a, b = b, a
        for i in range(2, len(nums)):
            num = nums[i]
            if num > a:
                a, b = num, a
            elif num > b:
                b = num
        return (a - 1) * (b - 1)


