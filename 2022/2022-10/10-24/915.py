class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left, left_max, cur_max = 0, nums[0], nums[0]
        for i in range(1, len(nums)):
            cur_max = max(cur_max, nums[i])
            if nums[i] < left_max:
                left_max = cur_max
                left = i
        return left+1

