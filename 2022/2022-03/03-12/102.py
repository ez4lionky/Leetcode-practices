from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = []
        q = deque([root])
        while q:
            size = len(q)
            cur = []
            for _ in range(size):
                r = q.popleft()
                cur.append(r.val)
                if r.left: q.append(r.left)
                if r.right: q.append(r.right)
            res.append(cur)
        return res

