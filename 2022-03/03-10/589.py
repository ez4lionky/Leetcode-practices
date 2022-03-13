"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


# recursive implementation
# class Solution:
#     vals = []
#     def preorder(self, root: 'Node') -> List[int]:
#         # print(root.val)
#         self.vals = []
#         res = self.pre_traverse(root)
#         return res
#
#     def pre_traverse(self, root: 'Node') -> List[int]:
#         if root is None:
#             return
#         self.vals.append(root.val)
#         for n in root.children:
#             self.pre_traverse(n)
#         return self.vals


# non-recursive implementation
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        vals = []
        stack = [root]
        while stack:
            r = stack.pop()
            vals.append(r.val)
            for c in r.children[::-1]:
                stack.append(c)
        return vals

