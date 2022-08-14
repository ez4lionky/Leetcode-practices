class Solution:
    def maxScore(self, s: str) -> int:
        st, l = 1, len(s)
        zero_num, one_num = s[:st] == '0', s[st:].count('1')
        res = zero_num + one_num
        # print(zero_num, one_num, res)
        while st < l-1:
            zero_num += s[st] == '0'
            one_num -= s[st] == '1'
            if zero_num + one_num > res:
                res = zero_num + one_num
            st += 1
        return res



if __name__ == "__main__":
    sol = Solution()
    s = "00"
    print(sol.maxScore(s))

