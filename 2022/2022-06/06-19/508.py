from typing import Counter


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        counter = Counter()
        def dfs(r):
            if r is None:
                return 0
            s = dfs(r.left) + dfs(r.right) + r.val
            counter[s] += 1
            return s
        dfs(root)
        # items = counter.most_common()
        # max_v, max_n = items[0]
        # items = items[1:]
        # res = [max_v]
        # for v, n in items:
        #     if n != max_n:
        #         break
        #     else:
        #         res.append(v)
        # return res

        maxCnt = max(cnt.values())
        return [s for s, c in cnt.items() if c == maxCnt]


