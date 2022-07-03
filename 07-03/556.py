class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))
        l = len(s)
        pre, cur = 0, 0
        for i in range(1, l):
            if s[i-1] < s[i]:
                pre, cur = i-1, i
        if pre == cur:
            return -1
        
        for i in range(cur, l):
            if s[i] < s[cur] and s[i] > s[pre]:
                cur = i
        s[pre], s[cur] = s[cur], s[pre]
        s[pre+1:] = sorted(s[pre+1:])
        n = int(str(''.join(s)))
        print(n)
        if n <= 2**31-1:
            return n
        return -1


if __name__ == "__main__":
    sol = Solution()
    n = 2147483476
    print(sol.nextGreaterElement(n))

