from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = deque([root])
        res = []
        while q:
            cur_max = -float('inf')
            for i in range(len(q)):
                n = q.popleft()
                if n.val > cur_max:
                    cur_max = n.val
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
            res.append(cur_max)
        return res
