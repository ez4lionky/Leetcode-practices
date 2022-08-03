class Solution:
    def countEven(self, num: int) -> int:
        nums = list(range(1, num+1))
        res = 0
        for n in nums:
            n = str(n)
            s = sum([int(ch) for ch in n])
            if s % 2 == 0:
                res += 1
        return res


if __name__ == "__main__":
    sol = Solution()
    # num = 30
    num = 4
    print(sol.countEven(num))

