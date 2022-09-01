from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])

        while q:
            cur_sum = 0
            for i in range(len(q)):
                r = q.popleft()
                cur_sum += r.val
                if r.left is not None:
                    q.append(r.left)
                if r.right is not None:
                    q.append(r.right)

        return cur_sum


