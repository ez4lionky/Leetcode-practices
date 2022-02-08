from typing import List


# class Solution:
#     candidates = []
#     res = []
#     path = []
#
#     def backtrack(self, idx, target):
#         if idx == len(self.candidates) or target == 0:
#             if target == 0:
#                 self.res.append(self.path[:])
#             return
#
#         for i in range(idx, len(self.candidates)):
#             if target < self.candidates[i]:
#                 break
#             if i > idx and self.candidates[i] == self.candidates[i-1]:
#                 # avoid repeating number in the same recursion
#                 # e.g. [1, 2, 5], [1, 2, 5]
#                 continue
#             self.path.append(self.candidates[i])
#             self.backtrack(i+1, target-self.candidates[i])
#             self.path.pop()
#         return
#
#
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         self.candidates = sorted(candidates)
#         self.res = []
#         self.path = []
#         self.backtrack(0, target)
#         return self.res


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def backtrack(idx, target):
            if idx == len(candidates) or target == 0:
                if target == 0:
                    res.append(path[:])
                return

            for i in range(idx, len(candidates)):
                if target < candidates[i]:
                    break
                if i > idx and candidates[i] == candidates[i-1]:
                    # avoid repeating number in the same recursion
                    # e.g. [1, 2, 5], [1, 2, 5]
                    continue
                path.append(candidates[i])
                backtrack(i+1, target-candidates[i])
                path.pop()
            return
        candidates = sorted(candidates)
        backtrack(0, target)
        return res


if __name__ == "__main__":
    sol = Solution()
    candidates = [10,1,2,7,6,1,5]
    # candidates = [1, 1, 2, 5, 6, 7, 10]
    target = 8
    # candidates = [2,5,2,1,2]
    # target = 5
    print(sol.combinationSum2(candidates, target))

