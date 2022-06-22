# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    val, max_h = 0, 0
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def dfs(r, h):
            if r is None:
                return
            if h > self.max_h:
                self.max_h = h
                self.val = r.val
            dfs(r.left, h+1)
            dfs(r.right, h+1)

        dfs(root, 1)
        return self.val

