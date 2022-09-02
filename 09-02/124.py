# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_sum = -float('inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -float('inf')
        def dfs(r):
            if r is None:
                return 0
            left = max(dfs(r.left), 0)
            right = max(dfs(r.right), 0)
            s = left + right + r.val
            self.max_sum = max(self.max_sum, s)
            return s + max(left, right)
        dfs(root)
        return self.max_sum


