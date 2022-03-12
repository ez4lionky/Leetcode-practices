# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     vals = []
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         self.vals = []
#         self.preorder(root)
#         return self.vals
#
#     def preorder(self, root):
#         if root is not None:
#             self.vals.append(root.val)
#             self.preorder(root.left)
#             self.preorder(root.right)

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res, stack = [], [root]
        while stack:
            r = stack.pop()
            res.append(r.val)
            if r.right: stack.append(r.right)
            if r.left: stack.append(r.left)
        return res

