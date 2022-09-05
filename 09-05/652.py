# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    tree_set = dict()
    repeated = set()
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.tree_set = dict()
        self.repeated = set()

        def dfs(r):
            if r is None:
                return ''
            serial = f"({r.val}) + ({dfs(r.left)}) + ({dfs(r.right)})"
            # serial = ''.join(['(', str(r.val), ')(', dfs(r.left), ')(', dfs(r.right)])
            t = self.tree_set.get(serial, None)
            if t:
                self.repeated.add(t)
            else:
                self.tree_set[serial] = r
            return serial

        dfs(root)
        return list(self.repeated)

