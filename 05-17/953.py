from itertools import pairwise


# class Solution:
#     def isAlienSorted(self, words: List[str], order: str) -> bool:
#         def if_sorted(w0, w1, order):
#             l = min(len(w0), len(w1))
#             for i in range(l):
#                 s0, s1 = order.find(w0[i]), order.find(w1[i])
#                 if s0 > s1:
#                     return False
#                 elif s0 < s1:
#                     return True
#             if len(w0) > l:
#                 return False
#             return True
#
#         for i in range(len(words) - 1):
#             w0, w1 = words[i], words[i+1]
#             flag = if_sorted(w0, w1, order)
#             if not flag:
#                 return False
#         return True

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index = {c: i for i, c in enumerate(order)}
        return all([s <= t for s, t in pairwise([index[c] for c in word] for word in words)])

