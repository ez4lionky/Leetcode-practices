class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums = sorted(nums, reverse=True)
        s = sum(nums)

        res, cur_s = [], 0
        for i in range(len(nums)):
            res.append(nums[i])
            cur_s += nums[i]
            if cur_s > s - cur_s:
                return res

