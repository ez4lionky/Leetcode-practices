from typing import List
from collections import Counter


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = Counter()
        if len(s) > 10:
            for i in range(len(s)-9):
                res[s[i:i+10]] += 1
        return [k for k in res.keys() if res[k] > 1]



if __name__ == "__main__":
    sol = Solution()
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(sol.findRepeatedDnaSequences(s))
