class Solution:
    def removeOuterParentheses(self, s: str):
        par_level = 0
        res = ''
        cur_item = ''
        for c in s:
            cur_item += c
            if c == '(':
                par_level += 1
            else:
                par_level -= 1
            if par_level == 0:
                # print(cur_item)
                if cur_item:
                    res += cur_item[1:-1]
                cur_item = ''
        return res


if __name__ == "__main__":
    sol = Solution()
    s = "(()())(())"
    print(sol.removeOuterParentheses(s))

