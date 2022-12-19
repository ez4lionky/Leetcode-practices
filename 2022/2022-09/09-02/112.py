# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = False
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.res = False
        def dfs(r, val):
            if r is None or self.res:
                return
            val += r.val
            if r.left:
                dfs(r.left, val)
            if r.right:
                dfs(r.right, val)
            if r.left is None and r.right is None and val == targetSum:
                self.res = True
                
        dfs(root, 0)
        return self.res

