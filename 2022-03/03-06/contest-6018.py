# Definition for a binary tree node.
from typing import List, Optional
from collections import Counter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        v_nodes = {}
        degrees = Counter()
        for d in descriptions:
            left, right = None, None
            if d[1] in v_nodes.keys():
                tmp = v_nodes[d[1]]
            else:
                tmp = TreeNode(d[1])
                v_nodes[d[1]] = tmp
            degrees[d[1]] += 1
            if d[2]: left = tmp
            else: right = tmp

            if d[0] not in v_nodes.keys():
                parent = TreeNode(d[0], left, right)
                v_nodes[d[0]] = parent
            else:
                parent = v_nodes[d[0]]
                if d[2]: parent.left = left
                else: parent.right = right
        for v in v_nodes.keys():
            if degrees[v] == 0:
                return v_nodes[v]
        return


if __name__ == "__main__":
    sol = Solution()
    descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
    print(sol.createBinaryTree(descriptions).val)
