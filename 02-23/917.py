class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        res = list(s)
        start, end = 0, len(s) - 1
        while start < end:
            while start < end:
                if s[start].isalpha() and s[end].isalpha():
                    break
                if not s[start].isalpha():
                    start += 1
                if not s[end].isalpha():
                    end -= 1
            if start < end:
                res[end], res[start] = res[start], res[end]
                start += 1
                end -= 1
        return ''.join(res)


if __name__ == "__main__":
    sol = Solution()
    # s = "ab-cd"
    s = "?6C40E"
    print(sol.reverseOnlyLetters(s))
