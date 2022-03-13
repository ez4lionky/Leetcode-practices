from typing import List
from collections import Counter, defaultdict


# class Solution:
#     def findRepeatedDnaSequences(self, s: str) -> List[str]:
#         res = Counter()
#         if len(s) > 10:
#             for i in range(len(s)-9):
#                 res[s[i:i+10]] += 1
#         return [k for k in res.keys() if res[k] > 1]


L = 10
bin = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n <= L:
            return []
        ans = []
        x = 0
        for ch in s[:L - 1]:
            x = (x << 2) | bin[ch]
        cnt = defaultdict(int)
        # print(x)
        for i in range(n - L + 1):
            x = ((x << 2) | bin[s[i + L - 1]]) & ((1 << (L * 2)) - 1)
            cnt[x] += 1
            if cnt[x] == 2:
                ans.append(s[i : i + L])
        return ans


if __name__ == "__main__":
    sol = Solution()
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(sol.findRepeatedDnaSequences(s))
