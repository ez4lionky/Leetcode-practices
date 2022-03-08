class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return str(num)

        flag = num < 0
        res = ''
        num = abs(num)
        while num > 0:
            remainder = num % 7
            num = num // 7
            res += str(remainder)
        if flag:
            res+='-'
        return res[::-1]


if __name__ == "__main__":
    sol = Solution()
    # num = 100
    # num = -7
    num = -10
    print(sol.convertToBase7(num))
