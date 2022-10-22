class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        l, min_i = min([len(word1), 0], [len(word2), 1])
        for i in range(l):
            res += word1[i] + word2[i]
        res += word2[l:] if min_i == 0 else word1[l:]
        return res

