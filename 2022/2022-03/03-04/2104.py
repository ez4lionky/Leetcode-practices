class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for i in range(n):
            minVal, maxVal = inf, -inf
            for j in range(i, n):
                minVal = min(minVal, nums[j])
                maxVal = max(maxVal, nums[j])
                ans += maxVal - minVal
        return ans


if __name__ == "__main__":
    nums = [1,2,3]
    sol = Solution()
    print(sol.subArrayRanges(nums))

