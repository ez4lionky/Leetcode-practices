# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res, level = 1, 0
        q = deque([[root, 0]])
        while q:
            level += 1
            cur_idxs = []
            for i in range(len(q)):
                r, idx = q.popleft()
                if r.left:
                    cur_idx = 2 * idx
                    q.append([r.left, cur_idx])
                    cur_idxs.append(cur_idx)
                if r.right: 
                    cur_idx = 2 * idx + 1
                    q.append([r.right, cur_idx])
                    cur_idxs.append(cur_idx)
            if cur_idxs:
                next_width = max(cur_idxs) - min(cur_idxs) + 1
                if next_width > res:
                    res = next_width
        return res

