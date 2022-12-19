class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        def dfs(i, ss):
            if i == len(s):
                res.append(ss)
                return
            if s[i].isalpha():
                dfs(i+1, ss+s[i].lower())
                dfs(i+1, ss+s[i].upper())
            else:
                dfs(i+1, ss+s[i])
        dfs(0, '')
        return res

