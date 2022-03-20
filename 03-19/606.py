# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    res = ""
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def pre_traverse(root):
            if root:
                self.res += str(root.val)
                if root.left and root.right:
                    self.res += "("
                    pre_traverse(root.left)
                    self.res += ")"
                    self.res += "("
                    pre_traverse(root.right)
                    self.res += ")"
                elif root.right:
                    self.res += "()"
                    self.res += "("
                    pre_traverse(root.right)
                    self.res += ")"
                elif root.left:
                    self.res += "("
                    pre_traverse(root.left)
                    self.res += ")"
            return
        pre_traverse(root)
        return self.res

