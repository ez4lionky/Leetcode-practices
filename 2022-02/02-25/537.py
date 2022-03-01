class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        plus1, plus2 = num1.find('+'), num2.find('+')
        re1, re2 = int(num1[:plus1]), int(num2[:plus2])
        im1, im2 = int(num1[plus1+1:-1]), int(num2[plus2+1:-1])
        res_re, res_im = re1 * re2 - im1 * im2, im1 * re2 + im2 * re1
        res = f'{res_re}+{res_im}i'
        return res


if __name__ == "__main__":
    sol = Solution()
    # num1 = "1+1i"
    # num2 = "1+1i"
    num1 = "1+-1i"
    num2 = "1+-1i"
    print(sol.complexNumberMultiply(num1, num2))

