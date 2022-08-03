"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# class Solution:
#     vals = []
#     def postorder(self, root: 'Node') -> List[int]:
#         # print(root.val)
#         self.vals = []
#         res = self.pre_traverse(root)
#         return res
#
#     def pre_traverse(self, root: 'Node') -> List[int]:
#         if root is None:
#             return
#         for n in root.children:
#             self.pre_traverse(n)
#         self.vals.append(root.val)
#         return self.vals

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return
        res = []
        stack = [root]
        while stack:
            r = stack.pop()
            res.append(r.val)
            stack.extend(r.children)  # N, R, L -> L, R, N
        return res[::-1]

