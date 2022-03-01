class Solution:
    def optimalDivision(self, nums) -> str:
        nums = [str(n) for n in nums]
        return '/'.join(nums) if len(nums) <= 2 else f'{nums[0]}/(' + '/'.join(nums[1:]) + ')'


if __name__ == "__main__":
    sol = Solution()
    nums = [1000,100,10,2]
    print(sol.optimalDivision(nums))

