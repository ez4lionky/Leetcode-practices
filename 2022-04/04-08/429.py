from typing import List
from collections import deque


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        q = deque([root])
        while q:
            s = len(q)
            cur = []
            for _ in range(s):
                r = q.popleft()
                cur.append(r.val)
                for c in r.children:
                    q.append(c)
            res.append(cur)
        return res

