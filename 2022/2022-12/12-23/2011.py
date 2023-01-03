# class Solution:
#     def finalValueAfterOperations(self, operations: List[str]) -> int:
#         res = 0
#         for op in operations:
#             x = 1 if '+' in op else -1
#             res += x
#         return res


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(44 - ord(op[1]) for op in operations)

