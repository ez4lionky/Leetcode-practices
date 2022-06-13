from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0:
            return 0
        s = sum(nums)
        f0 = sum([i*n for i, n in enumerate(nums)])
        f_max, pre_f = f0, f0
        for i in range(1, l):
            cur_f = pre_f + s - l*nums[l-i]
            if cur_f > f_max:
                f_max = cur_f
            pre_f = cur_f
        return f_max


if __name__ == "__main__":
    sol = Solution()
    nums = [4,3,2,6]
    print(sol.maxRotateFunction(nums))

