class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        l = len(nums)
        while l > 1:
            new_nums = []
            for i in range(l//2):
                if i % 2 == 0:
                    num = min(nums[2*i], nums[2*i+1])
                else:
                    num = max(nums[2*i], nums[2*i+1])
                new_nums.append(num)
            nums = new_nums
            l = len(nums)
        return nums[0]

