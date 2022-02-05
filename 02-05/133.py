"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self) -> None:
        self.visited = {}


    def cloneGraph(self, node: 'Node'):
        if node is None:
            return None
        new_node = Node(node.val)
        self.visited[node.val] = new_node
        for n in node.neighbors:
            if n.val not in self.visited:
                new_node.neighbors.append(self.cloneGraph(n))
            else:
                new_node.neighbors.append(self.visited[n.val])
        return new_node

