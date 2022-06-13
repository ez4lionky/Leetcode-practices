from typing import List


# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         path, res = [], []
#         def backtracking(idx, target):
#             if n - len(path) < target or target < 0:
#                 return
#             if target == 0:
#                 res.append(path[:])
#             for i in range(idx, n+1):
#                 path.append(i)
#                 backtracking(i+1, target-1)
#                 path.pop()
#
#         backtracking(1, k)
#         return res


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path, res = [], []
        def backtracking(idx, target):
            if len(path) == target:
                res.append(path[:])
                return
            for i in range(idx, n-(k-len(path)) + 2):
                path.append(i)
                backtracking(i+1, target)
                path.pop()

        backtracking(1, k)
        return res

# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         res = []
#         path = []
#         def backtrack(n, k, StartIndex):
#             if len(path) == k:
#                 res.append(path[:])
#                 return
#             for i in range(StartIndex, n-(k-len(path)) + 2):
#                 path.append(i)
#                 backtrack(n, k, i+1)
#                 path.pop()
#         backtrack(n, k, 1)
#         return res


if __name__ == "__main__":
    sol = Solution()
    n = 4
    k = 2
    print(sol.combine(n, k))

