class Solution:
    def findContentChildren(self, g: [int], s: [int]) -> int:
        # s -> sugar(cookie) list
        # g -> children's content
        g.sort()
        s.sort()
        gi, si = 0, 0
        while gi < len(g) and si < len(s):
            if g[gi] <= s[si]:
                gi += 1
            si += 1
        return gi


g = [1, 2, 3]
s = [1, 1]
sol = Solution()
print(sol.findContentChildren(g, s))
