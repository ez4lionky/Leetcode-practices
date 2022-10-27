class Solution:
    def arraySign(self, nums: List[int]) -> int:
        s = 0
        for num in nums:
            if num < 0:
                s += 1
            elif num == 0:
                return 0
        return 1 if s % 2 == 0 else -1

