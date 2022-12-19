# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# this problem should not be solved from the up to the bottom, otherwise the time complexity is n**2
# but we can solve it from the bottom to the top.
class Solution:
    max_level = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.max_level = 0
        def dfs(r):
            if r is None:
                return 0
            left = dfs(r.left)
            right = dfs(r.right)
            left1 = left + 1 if r.left and r.left.val == r.val else 0
            right1 = right + 1 if r.right and r.right.val == r.val else 0
            if self.max_level < left1 + right1:
                self.max_level = left1 + right1
            return max(left1, right1)

        dfs(root)
        return self.max_level

