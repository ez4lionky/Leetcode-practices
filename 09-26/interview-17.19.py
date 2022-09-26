class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums)+3)) - set(nums))


# not finished
# class Solution:
#     def missingTwo(self, nums: List[int]) -> List[int]:
#         n = len(nums) + 2
#         nums.append([99999, 99999, 99999])
#         for i in range(n+1):
#             x = nums[i]
#             if x < n:
#                 nums[i] = -nums[i]
#         res = [i for i, x in enumerate(nums) if x > 0]
#         return res

