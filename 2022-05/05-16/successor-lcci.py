# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        data, pre, cur = [], None, root
        while data or cur:
            while cur:
                data.append(cur)
                cur = cur.left
            cur = data.pop()
            if pre == p:
                return cur
            pre = cur
            cur = cur.right
        return None
