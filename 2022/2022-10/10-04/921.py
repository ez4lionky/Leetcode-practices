class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left_num, right_num = 0, 0
        for c in s:
            if c is "(":
                left_num += 1
            elif left_num > 0:
                left_num -= 1
            else:
                right_num += 1
        return left_num + right_num

