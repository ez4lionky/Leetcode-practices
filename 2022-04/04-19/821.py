class Solution:
    def shortestToChar(self, s: str, c: str):
        res = []
        n = len(s)
        idx = -n
        for i in range(n):
            if s[i] == c:
                idx = i
            res.append(i-idx)
        
        idx = 2*n
        for i in range(n-1,-1,-1):
            if s[i] == c:
                idx = i
            res[i] = min(res[i], idx-i)
        return res


if __name__ == "__main__":
    sol = Solution()
    s = "abaa"
    c = "b"
    print(sol.shortestToChar(s, c))

