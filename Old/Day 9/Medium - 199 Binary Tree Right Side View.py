# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> [int]:
        if not root:
            return
        results = []
        queue = list()
        queue.append(root)
        while len(queue) > 0:
            len_queue = len(queue)
            for i in range(len_queue):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == len_queue - 1:
                    results.append(node.val)
        return results
