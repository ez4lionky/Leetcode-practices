from typing import List


# class Solution:
#     def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
#         r_s = sum(rolls)
#         m = len(rolls)
#         s = (m + n) * mean
#         if s > n * 6 + r_s or r_s + n > s:
#             return []
#         diff = s - r_s
#         r = diff // n
#         diff -= r * n
#         res = [r] * n
#         i = 0
#         while diff:
#             res[i] += 1
#             diff -= 1
#             i += 1
#         return res


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m_s = mean * (n + len(rolls)) - sum(rolls)
        if not n <= m_s <= n*6:
            return []
        quotient, remainder = divmod(m_s, n)
        return [quotient + 1] * remainder + [quotient] * (n - remainder)


if __name__ == "__main__":
    sol = Solution()
    rolls = [3,2,4,3]
    mean = 4
    n = 2
    print(sol.missingRolls(rolls, mean, n))

