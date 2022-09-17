from collections import defaultdict


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        index_dict = defaultdict(list)
        for i, c in enumerate(s):
            index_dict[c].append(i)
            if len(index_dict[c]) > 1:
                res = max(res, i - index_dict[c][0] - 1)
        return res

