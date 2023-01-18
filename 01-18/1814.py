from collections import Counter


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        res = 0
        counter = Counter()
        for n in nums:
            rev_n = int(str(n)[::-1])
            dif = n - rev_n
            res += counter[dif]
            counter[dif] += 1
        return res % (10 ** 9 + 7)

