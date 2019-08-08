class Solution:
    def subsetsWithDup(self, nums: [int]) -> [[int]]:
        items = set()
        nums = sorted(nums)
        print(nums)
        max_value = 1 << len(nums)
        for i in range(max_value):
            item = []
            for j in range(len(nums)):
                if i & 1 << j:
                    item.append(nums[j])
            items.add(tuple(item))
        results = []
        for i in items:
            results.append(list(i))
        return results


nums = [2, 1, 2]
sol = Solution()
print(sol.subsetsWithDup(nums))
