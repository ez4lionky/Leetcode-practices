import random


# class Solution:
#     def repeatedNTimes(self, nums: List[int]) -> int:
#         s = set()
#         for n in nums:
#             if n in s:
#                 return n
#             s.add(n)
#         return -1


# class Solution:
#     def repeatedNTimes(self, nums: List[int]) -> int:
#         n = len(nums)
#         for gap in range(1, 4):
#             for i in range(n - gap):
#                 if nums[i] == nums[i + gap]:
#                     return nums[i]
        
#         # 不可能的情况
#         return -1


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)

        while True:
            x, y = random.randrange(n), random.randrange(n)
            if x != y and nums[x] == nums[y]:
                return nums[x]

