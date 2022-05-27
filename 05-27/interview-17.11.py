# class Solution:
#     def findClosest(self, words: List[str], word1: str, word2: str) -> int:
#         pos1, pos2 = [], []
#         for i, w in enumerate(words):
#             if w == word1:
#                 pos1.append(i)
#             elif w == word2:
#                 pos2.append(i)
#         res = 1000000
#         for i in pos1:
#             for j in pos2:
#                 if abs(i-j) < res:
#                     res = abs(i-j)
#         return res


class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        ans, idx1, idx2 = inf, inf, -inf
        for i, word in enumerate(words):
            if word1 == word:
                idx1 = i
            elif word2 == word:
                idx2 = i
            ans = min(ans, abs(idx1 - idx2))
        return ans

