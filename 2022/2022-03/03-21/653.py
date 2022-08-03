class Solution:
    res = False
    residuals = set()
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def pre_order(root):
            if root and not self.res:
                if root.val in self.residuals:
                    self.res = True
                else:
                    diff = k - root.val
                    self.residuals.add(diff)
                    pre_order(root.left)
                    pre_order(root.right)
            return

        self.res = False
        self.residuals = set()
        pre_order(root)
        return self.res

# class Solution:
#
#     def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
#         res = False
#         residuals = set()
#         def pre_order(root):
#             nonlocal res, residuals
#             if root and not res:
#                 if root.val in residuals:
#                     res = True
#                 else:
#                     diff = k - root.val
#                     residuals.add(diff)
#                     pre_order(root.left)
#                     pre_order(root.right)
#             return
#
#         pre_order(root)
#         return res
