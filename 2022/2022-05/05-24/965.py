# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    num = None
    flag = True
    def isUnivalTree(self, root: TreeNode) -> bool:
        self.flag = True
        self.num = root.val
        def dfs(r):
            if r is not None and self.flag:
                if r.val != self.num:
                    self.flag = False
                    return
                dfs(r.left)
                dfs(r.right)
            return
        dfs(root)
        return self.flag

