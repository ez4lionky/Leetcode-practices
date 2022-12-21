class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        max_val = max([a, b, c])
        left_s = sum([a, b, c]) - max_val
        return left_s if max_val >= left_s else (a+b+c) // 2
        

