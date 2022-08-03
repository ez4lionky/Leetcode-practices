from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        start, end = 0, len(s)
        res = []
        for c in s:
            if c == 'I':
                res.append(start)
                start += 1
            else:
                res.append(end)
                end -= 1
        res.append((set(range(len(s)+1)) - set(res)).pop())
        return res

