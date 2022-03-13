from typing import List


# nums.length <= 10^5 << k <= 10^9
# so use sum of arithmetic progression to substract sum(nums[:i])
# notes: after reading the problem description, 
# firstly try to follow the train of thought of interviewer and solve the problem.
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = sorted(set(nums)) + [int(2e9)]
        s = 0
        for i, num in enumerate(nums):
            if num - 1 - i >= k:
                return (k + i) * (k + i + 1) // 2 - s
            s += num
        return -1


# class Solution:
#     def minimalKSum(self, nums, k: int):
#         nums = sorted(set(nums))
#         print(nums)
#         res, i, v = [], 0, 1
#         while k > 0 and i < len(nums):
#             if v != nums[i]:
#                 res.append(v)
#                 k -= 1
#                 v += 1
#             else:
#                 v += 1
#                 i += 1
#         while k > 0:
#             res.append(v)
#             v += 1
#             k -= 1
#         print(len(res), sum(res))
#         return res

if __name__ == "__main__":
    sol = Solution()
    # nums=[96,44,99,25,61,84,88,18,19,33,60,86,52,19,32,47,35,50,94,17,29,98,22,21,72,100,40,84]
    # k=35
    nums=[53,41,90,33,84,26,50,32,63,47,66,43,29,88,71,28,83]
    k=76
    print(sol.minimalKSum(nums, k))

