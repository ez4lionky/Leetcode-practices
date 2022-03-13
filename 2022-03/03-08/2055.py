from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        res = []
        n_s = len(s)
        plates_num, p_n = [0] * n_s, 0
        l, l_i = [0] * n_s, -1
        for i, ch in enumerate(s):
            if ch == '|':
                plates_num[i] = p_n
                l_i = i
            else:
                p_n += 1
            l[i] = l_i

        r, r_i = [0] * n_s, n_s
        for i in range(n_s-1, -1, -1):
            if s[i] == '|':
                r_i = i
            r[i] = r_i
        for x, y in queries:
            if x<=r[x]<=y and x<=l[y]<=y and r[x] != l[y]:
                res.append(plates_num[l[y]] - plates_num[r[x]])
            else:
                res.append(0)
        return res


if __name__ == "__main__":
    sol = Solution()
    s = "**|**|***|"
    queries = [[2,5],[5,9]]
    print(sol.platesBetweenCandles(s, queries))

