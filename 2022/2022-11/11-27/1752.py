class Solution:
    def check(self, nums: List[int]) -> bool:
        x = 0
        l = len(nums)
        for i in range(l-1):
            if nums[i+1] < nums[i]:
                x = i+1
                break
        if x == 0:
            return True
        for i in range(x, l-1):
            if nums[i+1] < nums[i]:
                return False
        return nums[0] >= nums[l-1]

