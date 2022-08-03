from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        l, r = s.split(':')
        cols = [chr(i) for i in range(ord(l[0]), ord(r[0]))]
        cols.append(r[0])
        res = []
        for i in cols:
            for j in range(int(l[1]), int(r[1])+1):
                res.append(i+str(j))
        return res

if __name__ == "__main__":
    sol = Solution()
    s = "K1:L2"
    print(sol.cellsInRange(s))

