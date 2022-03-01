from typing import List
import functools


# class Solution:
#     res = 0
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         # if target - amount > sum(nums[i:]): should be pruned
#         # if amount - sum(nums[i:]) > target: should be pruned
#         def dfs(i, amount):
#             # if i == len(nums) or (target-amount>sum(nums[i:])) or (amount-sum(nums[i:])>target):
#             if i == len(nums):
#                 if amount == target:
#                     self.res += 1
#                 return
#             dfs(i+1, amount + nums[i])
#             dfs(i+1, amount - nums[i])
#             return
#
#         dfs(0, 0)
#         return self.res


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        @functools.lru_cache(None)
        def find(i,t):  #从下标为i的数字开始凑和为t的方案数
            if i==n-1:
                ans=0
                if t==nums[i]:
                    ans+=1
                if t==-nums[i]:
                    ans+=1
                return ans
            else:
                return find(i+1,t-nums[i])+find(i+1,t+nums[i])
        return find(0,target)


if __name__ == "__main__":
    sol = Solution()
    # nums = [1,1,1,1,1]
    # target = 5
    nums = [1,1,1,1,1]  # out should be 5
    target = 3
    # nums = [1]
    # target = 1
    # nums = [27,33,4,43,31,44,47,6,6,11,39,37,15,16,8,19,48,17,18,39]
    # target = 24
    print(sol.findTargetSumWays(nums, target))

