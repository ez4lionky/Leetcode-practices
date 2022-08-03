from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path, res = [], []
        def backtracking(idx, sum, target):
            if target < 0:
                return
            if target == 0:
                res.append(path[:])
                return
            for i in range(idx, len(candidates)):
                path.append(candidates[i])
                backtracking(i, sum+candidates[i], target-candidates[i])
                path.pop()
        backtracking(0, 0, target)
        return res


if __name__ == "__main__":
    sol = Solution()
    # candidates = [2,3,6,7]
    # target = 7
    # candidates = [2,3,5]
    # target = 8
    candidates = [2]
    target = 1
    print(sol.combinationSum(candidates, target))

