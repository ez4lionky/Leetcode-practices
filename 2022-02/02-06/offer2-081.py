from types import TracebackType
from typing import List


# from candidates[-1] to candidates[0], so that sorted need to be reversed
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates, reverse=True)
        res = []
        path = []
        def backtracking(i, s):
            if i == len(candidates) or s > target:
                return
            if s == target:
                res.append(path[:])
                return
            backtracking(i+1, s)
            if s + candidates[i] <= target:
                path.append(candidates[i])
                backtracking(i, s+candidates[i])
                path.pop()
            return

        backtracking(0, 0)
        return res


# add element from candiates[0] to candidates[-1], can directly use for loop
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         self.track = []
#         self.ans = []
#         self.candidates = sorted(candidates)
#         self.dfs_backtrack(0, target, 0)
#         return self.ans 

#     def dfs_backtrack(self, sum, target, last_idx):
#         if sum == target:
#             self.ans.append(self.track.copy())
#             return 
#         # 剪枝
#         for idx in range(last_idx, len(self.candidates)):
#             val = self.candidates[idx]
#             if (val + sum > target):
#                 break 
#             self.track.append(val)
#             self.dfs_backtrack(sum + val, target, idx)
#             self.track.pop()
#         return

if __name__ == "__main__":
    sol = Solution()
    candidates = [2,3,6,7]
    target = 7
    print(sol.combinationSum(candidates, target))

    # sum=0, path=[], idx=0, val=2, path=[2], sum+val=2, backtrack(2, 7, 0)
    # sum=2, path=[2], idx=0, val=2, path=[2, 2], sum+val=4, backtrack(4, 7, 0)
    # sum=4, path[2, 2], idx=0, val=2, path=[2, 2, 2], sum+val=6, backtrack(6, 7, 0)
    # sum=6, path[2, 2, 2], idx=0, val=2, break, path.pop(), path=[2, 2], idx=1, val=3
