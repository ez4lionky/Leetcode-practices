class Solution:
    # def decodeString(self, s: str) -> str:
    #     stack, res, multi = [], "", 0
    #     # string is always valid
    #     for c in s:
    #         if c == '[':
    #             stack.append([multi, res])
    #             res, multi = "", 0
    #         elif c == ']':
    #             cur_multi, last_res = stack.pop()
    #             res = last_res + cur_multi * res
    #         elif '0' <= c <= '9':
    #             multi = multi * 10 + int(c)            
    #         else:
    #             res += c
    #     return res


    i = 0
    def decodeString(self, s: str) -> str:
        def dfs(s):
            res, count = '', 0
            while self.i < len(s):
                if s[self.i].isalpha():
                    res += s[self.i]
                elif s[self.i].isnumeric():
                    count = count * 10 + int(s[self.i])
                elif s[self.i] == '[':
                    self.i += 1
                    tmp = dfs(s)
                    res += count * tmp
                    count = 0
                else:
                    return res
                self.i += 1
            return res
        return dfs(s)

if __name__ == "__main__":
    s = "3[a]2[bc]"
    # s = "3[a2[c]]"
    # s = "2[abc]3[cd]ef"
    sol = Solution()
    print(sol.decodeString(s))

