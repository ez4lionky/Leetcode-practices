from itertools import groupby


class Solution:
    def countHomogenous(self, s: str) -> int:
        res = 0
        for k, g in groupby(s):
            g_l = len(list(g))
            res += g_l * (g_l + 1) // 2
        return res % (10**9 + 7)


if __name__ == "__main__":
    sol = Solution()

