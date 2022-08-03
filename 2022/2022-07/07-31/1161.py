from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        max_level, max_sum = -1, -10e7

        level = 0
        while q:
            level += 1
            cur_sum = 0
            for i in range(len(q)):
                r = q.popleft()
                cur_sum += r.val
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
            if cur_sum > max_sum:
                max_sum = cur_sum
                max_level = level
        return max_level

