class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        return num % 9
