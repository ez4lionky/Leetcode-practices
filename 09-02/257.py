# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    paths = []
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.paths = []
        def dfs(r, path):
            if r is None:
                return
            path += f'{r.val}->'
            if r.left is None and r.right is None:
                self.paths.append(path[:-2])
            if r.left: dfs(r.left, path)
            if r.right: dfs(r.right, path)
            return

        dfs(root, '')
        return self.paths


