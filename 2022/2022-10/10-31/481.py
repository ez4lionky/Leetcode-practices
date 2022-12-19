# class Solution:
#     def magicalString(self, n: int) -> int:
#         pre, cur, cur_c = 0, 0, '1'
#         s = '1'
#         while pre < n:
#             l = int(s[pre])
#             if s[cur:cur+l] == l * cur_c:
#                 cur_c = '2' if cur_c == '1' else '1'
#                 s += cur_c
#                 cur += l
#                 pre += 1
#             else:
#                 left = (l - len(s[cur:cur+l])) * cur_c
#                 s += left
#         return s[n]


# class Solution:
#     def magicalString(self, n: int) -> int:
#         pre, cur, cur_c = 0, 0, '1'
#         s = '1'
#         while cur < n:
#             l = int(s[pre])
#             if s[cur:cur+l] == l * cur_c:
#                 cur_c = '2' if cur_c == '1' else '1'
#                 s += cur_c
#                 cur += l
#                 pre += 1
#             else:
#                 s += cur_c
#         print(s[n])
#         return s[:n].count('1')


s = [1, 2, 2]
i = 2
one = True
while len(s) <= 100000:
    s += [1 if one else 2] * s[i]
    one = not one
    i += 1
cnt = [0] * (len(s) + 1)
for i in range(len(s)):
    cnt[i + 1] = cnt[i] + (s[i] == 1)


class Solution:
    def magicalString(self, n: int) -> int:
        return cnt[n]


if __name__ == "__main__":
    sol = Solution()
    print(sol.magicalString(6))

