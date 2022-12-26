class Solution:
    def minimumMoves(self, s: str) -> int:
        res, i = 0, 0
        while i < len(s):
            if s[i] == 'X':
                i += 3
                res += 1
            else:
                i += 1
        return res

if __name__ == "__main__":
    sol = Solution()
    s = "XXOX"
    print(sol.minimumMoves(s))

