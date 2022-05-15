from collections import deque


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """

        res = []
        def dfs(r):
            if r is not None:
                res.append(r.val)
                dfs(r.left)
                dfs(r.right)
                return

        dfs(root)
        res = ' '.join(res)
        return res
            

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        pass
