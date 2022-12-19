from collections import defaultdict
from bisect import bisect_right


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d = defaultdict(list)
        for i, c in enumerate(s):
            d[c].append(i)
        res = len(words)
        for w in words:
            if len(w) > len(s):
                res -= 1
                continue
            p = -1
            for c in w:
                pos_list = d[c]
                j = bisect_right(pos_list, p)
                if j == len(pos_list):
                    res -= 1
                    break
                p = pos_list[j]
        return res

