# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None


class Solution:
    def __init__(self):
        self.results = []
        self.path = []

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = None
        finish = 0
        self.search(root, p, finish)
        self.search(root, q, finish)
        path_len = min(len(self.results[0]), len(self.results[1]))
        for i in range(path_len):
            if self.results[0][i] != self.results[1][i]:
                result = self.results[0][i - 1]
            elif i == path_len - 1:
                s = 0 if len(self.results[0]) < len(self.results[1]) else 1
                result = self.results[s][i-1]
        return result

    def search(self, root, target, finish):
        if root is None or finish == 1:
            return
        self.path.append(root)
        if root == target:
            self.results.append(self.path.copy())
            finish = 1
        self.search(root.left, target, finish)
        self.search(root.right, target, finish)
        self.path.pop()

