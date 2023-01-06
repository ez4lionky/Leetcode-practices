class Solution:
    def countEven(self, num: int) -> int:
        res = 0
        for n in range(1, num+1):
            if sum(int(c) for c in str(n)) % 2 == 0:
                res += 1
        return res

