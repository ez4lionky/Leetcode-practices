class Solution:
    def nextGreaterElement(self, n: int) -> int:
        chars = list(str(n))
        pre, cur = 0, 0
        for i in range(1, len(chars)):
            if chars[i] > chars[i-1]:
                pre, cur = i-1, i
        if pre == cur:
            return -1
        
        idx = cur
        for i in range(cur+1, len(chars)):
            if chars[pre] < chars[i] and chars[i] < chars[idx]:
                idx = i
        cur = idx
        tmp = chars[pre]
        chars[pre] = chars[cur]
        chars[cur] = tmp

        chars[pre+1:] = sorted(chars[pre+1:])
        res = int("".join(chars))
        if res <= 2**31 - 1:
            return res
        return -1


if __name__ == "__main__":
    sol = Solution()
    # n = 12
    # n = 21
    # n = 230241  # output should be 230412
    # n = 2147483476  # output should be 2147483647
    n = 12222333  # output should be 12223233
    print(sol.nextGreaterElement(n))

