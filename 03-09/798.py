from typing import List


class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        diffs = [0] * n
        for i, num in enumerate(nums):
            low = (i + 1) % n
            high = (i - num + n + 1) % n
            diffs[low] += 1
            diffs[high] -= 1
            if low >= high:
                diffs[0] += 1
        score, maxScore, idx = 0, 0, 0
        for i, diff in enumerate(diffs):
            score += diff
            if score > maxScore:
                maxScore, idx = score, i
        return idx


# 如果按k进行旋转
# 索引的变化为：<k的变为len-k,...len-1, >=k的变为0,...len-k-1
# 即i->(i-k+n) mod n
# 遍历每个数，可以得到不能超过的索引O(n)
# 遍历k in range(0, len), 也是O(n)，总时间复杂度为O(n^2)
# 此时使用差分数组来优化，求k对应积分的时间复杂度


if __name__ == "__main__":
    sol = Solution()
    nums = [2,3,1,4,0]
    print(sol.bestRotation(nums))
