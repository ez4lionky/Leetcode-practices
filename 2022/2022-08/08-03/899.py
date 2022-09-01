class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return ''.join(sorted(s))
        min_s = s
        for i in range(len(s)):
            s = s[1:] + s[0]
            if s < min_s:
                min_s = s
        return min_s


if __name__ == "__main__":
    sol = Solution()
    s = "cba"
    k = 1
    print(sol.orderlyQueue(s, k))

