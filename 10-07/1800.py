class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        pre, cur_sum, max_sum = -1, 0, 0
        for n in nums:
            if n > pre:
                cur_sum += n
            else:
                cur_sum = n
            if cur_sum > max_sum:
                max_sum = cur_sum
            pre = n
        return max_sum

