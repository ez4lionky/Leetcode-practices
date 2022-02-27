from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_c, t_c = Counter(s), Counter(t)
        diff_s, diff_t = s_c - t_c, t_c - s_c
        return sum([diff_s[k] for k in diff_s]) + sum([diff_t[k] for k in diff_t])


if __name__ == "__main__":
    sol = Solution()
    s = "leetcode"
    t = "coats"
    print(sol.minSteps(s, t))

