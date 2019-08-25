# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.path_value = 0
        self.results = []
        self.path = []

    def pathSum(self, root: TreeNode, sum: int) -> [[int]]:
        self.preorder(root, sum)
        return self.results

    def preorder(self, node: TreeNode, sum):
        if node is None:
            return
        self.path_value += node.val
        self.path.append(node.val)
        if node.left is None and node.right is None and self.path_value == sum:
            self.results.append(self.path.copy())
        self.preorder(node.left, sum)
        self.preorder(node.right, sum)
        self.path_value -= node.val
        self.path.pop()


sol = Solution()

