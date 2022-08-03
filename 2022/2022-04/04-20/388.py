class Solution:
    def lengthLongestPath(self, input: str) -> int:
        self.res = 0
        self.items = input.split('\n')
        self.length = len(self.items)
        def dfs(prefix, cur, str_len):
            if cur == self.length or not self.items[cur].startswith(prefix):
                if '.' in self.items[cur-1]:
                    self.res = max(self.res, str_len-1)
                return cur
            new_p = prefix + '\t'
            while cur < self.length and self.items[cur].startswith(prefix):
                cur = dfs(new_p, cur+1, str_len + len(self.items[cur]) - len(prefix) + 1)
            return cur
        dfs('', 0, 0)
        return self.res


if __name__ == "__main__":
    sol = Solution()
    inputs = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    # inputs = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    print(sol.lengthLongestPath(inputs))

