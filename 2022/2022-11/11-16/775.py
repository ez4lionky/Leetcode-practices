# class Solution:
#     def isIdealPermutation(self, nums: List[int]) -> bool:
#         l = len(nums)
#         min_v = nums[l-1]
#         for i in range(l-3, -1, -1):
#             if nums[i] > min_v:
#                 return False
#             if nums[i+1] < min_v:
#                 min_v = nums[i+1]
#         return True


class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        return all(abs(x - i) <= 1 for i, x in enumerate(nums))

