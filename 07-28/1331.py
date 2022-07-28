# class Solution:
#     def arrayRankTransform(self, arr: List[int]) -> List[int]:
#         tmp = sorted(set(arr))
#         s  = {tmp[i]:i+1 for i in range(len(tmp))}
#         res = [s[n] for n in arr]
#         return res


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {v: i for i, v in enumerate(sorted(set(arr)), 1)}
        return [ranks[v] for v in arr]


