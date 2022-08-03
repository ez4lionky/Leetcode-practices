from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        nums = list(range(1, n+1))
        # def backtracking(i, left):
        #     # pruning the search space
        #     if n-i < left:
        #         return
        #     if left == 0:
        #         res.append(path[:])
        #         return
        #     backtracking(i+1, left)
        #     path.append(nums[i])
        #     backtracking(i+1, left-1)
        #     path.pop()
        #     return

        # n=4, path=[], i=0, left=2, path=[1], i=1, left=1, path=[1,2], i=2, left=0
        def backtracking(i, left):
            if left == 0:
                res.append(path[:])
                return
            for i in range(i, n):
                if n-i < left:
                    break
                path.append(nums[i])
                backtracking(i+1, left-1)
                path.pop()
            return
    
        backtracking(0, k)
        return res


if __name__ == "__main__":
    sol = Solution()
    n = 4
    k = 2
    print(sol.combine(n, k))

