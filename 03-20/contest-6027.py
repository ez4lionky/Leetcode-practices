from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        res, n, i = 0, len(nums), 1
        while i<n-1:
            l_d, l, r_d, r = 0, 0, 0, n-1
            for j in reversed(range(i)):
                if nums[j] != nums[i]:
                    l_d = nums[i] - nums[j]
                    l = j
                    break
            for k in range(i, n):
                if nums[k] != nums[i]:
                    r_d = nums[i] - nums[k]
                    r = k
                    break
            if l_d and r_d:
                if l_d * r_d > 0:
                    res += 1
                    # print(i, l, r)
            i = r
        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [6,6,5,5,4,1]
    print(sol.countHillValley(nums))

