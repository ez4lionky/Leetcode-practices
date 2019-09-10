class GraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    def __init__(self):
        self.graphs = []
        self.visits = []

    def canFinish(self, numCourses: int, prerequisites: [[int]]) -> bool:
        for i in range(numCourses):
            g = GraphNode(i)
            self.graphs.append(g)
            self.visits.append(-1)

        for i in range(len(prerequisites)):
            begin = prerequisites[i][1]
            end = prerequisites[i][0]
            self.graphs[begin].neighbors.append(self.graphs[end])

        for i in range(len(self.graphs)):
            if self.visits[i] == -1 and self.DFS_Graph(self.graphs[i]) is not True:
                return False
        return True

    def DFS_Graph(self, node: GraphNode) -> bool:
        self.visits[node.label] = 0
        for i in range(len(node.neighbors)):
            if self.visits[node.neighbors[i].label] == -1:
                if self.DFS_Graph(node.neighbors[i]) is False:
                    return False
            elif self.visits[node.neighbors[i].label] == 0:
                return False
        self.visits[node.label] = 1
        return True

