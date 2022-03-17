from typing import List


class Solution:
    max_s, res = 1, 0
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def backtracking(i, cur_s):
            if i == len(nums):
                if cur_s > self.max_s:
                    self.max_s = cur_s
                    self.res = 1
                elif cur_s == self.max_s:
                    self.res += 1
                return
            
            # backtracking(i+1, cur_s)
            # cur_s = cur_s | nums[i]
            # backtracking(i+1, cur_s)

            backtracking(i+1, cur_s|nums[i])
            backtracking(i+1, cur_s)

        backtracking(0, 0)
        return self.res


if __name__ == "__main__":
    sol = Solution()
    # nums = [3,1]
    # nums = [2,2,2]
    nums = [3,2,1,5]
    print(sol.countMaxOrSubsets(nums))

