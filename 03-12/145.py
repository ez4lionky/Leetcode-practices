# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    vals = []
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.vals = []
        self.postorder(root)
        return self.vals

    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            self.vals.append(root.val)


# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if root is None:
#             return []
#         res, stack = [], [root]
#         while stack:
#             r = stack.pop()
#             res.append(r.val)
#             if r.left: stack.append(r.left)
#             if r.right: stack.append(r.right)
#         return res[::-1]

