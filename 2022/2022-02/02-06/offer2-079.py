from typing import List


class Solution:
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     res = []
    #     def dfs(subset, i):
    #         if i == len(nums):
    #             res.append(subset)
    #             return
    #         else:
    #             dfs(subset, i+1)
    #             dfs(subset + [nums[i]], i+1)
    #     dfs([], 0)
    #     return res

    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     res = []
    #     path = []
    #     def backtracking(i):
    #         if i == len(nums):
    #             res.append(path[:])
    #             return
    #         backtracking(i+1)
    #         path.append(nums[i])
    #         backtracking(i+1)
    #         path.pop()
    #
    #     backtracking(0)
    #     return res

    # path=[], i=0, path=[1], i=1, path=[1, 2], i=2, path=[1,2,3], res=[[1,2,3]]
    # pop, path=[1, 2], res=[[1,2,3],[1,2]]
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def backtracking(i):
            if i == len(nums):
                res.append(path[:])
                return
            for i in range(i, len(nums)):
                path.append(nums[i])
                backtracking(i+1)
                path.pop()
            res.append(path[:])
            return
        backtracking(0)
        return res




if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4]
    # nums = [0]
    print(sol.subsets(nums))

