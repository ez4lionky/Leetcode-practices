from collections import Counter


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        return nums.sort(key = lambda x: (counter[x], -x))

