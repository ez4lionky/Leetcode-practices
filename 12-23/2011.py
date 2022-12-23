class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for op in operations:
            x = 1 if '+' in op else -1
            res += x
        return res

