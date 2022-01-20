class Solution:
    def __init__(self):
        self.result = set()

    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
        nums = sorted(candidates)
        s = 0
        item = []
        self.generate(0, nums, item, s, target)
        r = []
        for i in self.result:
            r.append(list(i))
        self.result = r
        return self.result

    def generate(self, i, nums, item, s, target):
        if i >= len(nums) or s > target:
            return
        item.append(nums[i])
        s += nums[i]
        if s == target:
            self.result.add(tuple(item))
        self.generate(i+1, nums, item, s, target)
        item.pop(-1)
        s -= nums[i]
        self.generate(i+1, nums, item, s, target)


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
sol = Solution()
print(sol.combinationSum2(candidates, target))
