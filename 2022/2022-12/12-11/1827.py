class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        pre = nums[0] + 1
        for i in range(1, len(nums)):
            pre = max(pre, nums[i])
            res += pre - nums[i]
            pre += 1
        return res

