# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    max_level = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0
        def dfs(r):
            if r is None:
                return 0
            left = dfs(r.left)
            right = dfs(r.right)
            left1 = left + 1 if r.left else 0
            right1 = right + 1 if r.right else 0
            self.max_length = max(self.max_length, left1 + right1)
            return max(left1, right1)

        dfs(root)
        return self.max_length

