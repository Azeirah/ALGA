"""Implementation of the minimum spanning tree algorithm"""
import random

# Relevant question
# Our graph is completely unweighted
# so we don't necessarily need the weighted parts of prim's and kruskal's algorithms.
# According to
# https://cs.stackexchange.com/questions/23179/if-all-edges-are-of-equal-weight-can-one-use-bfs-to-obtain-a-minimal-spanning-t
# /any/ spanning tree is a minimal spanning tree, so it works.
# The problem becomes to find a path from S to E
#
# Given a graph, G, with (S)tart and (E)nd
# Find a spanning-tree path from S to E, call this path P
# new Graph is now G - ¬P, ~= remove all edges that don't interfere with P

class DisjointSet:
    """Implementation based on Wikipedia, I don't pretend to understand it very well..."""
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def make_set(self, vertex):
        self.parent[vertex] = vertex
        self.rank[vertex] = 0

    def find_set(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find_set(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find_set(vertex1)
        root2 = self.find_set(vertex2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]: self.rank[root2] += 1

def mst(graph):
    """Minimum spanning tree using some version of Kruskal's algorithm
    Note that this algorithm is only tested on unweighted graphs.
    The step of sorting weights is skipped.

    returns a set of edges (tuples of vertices)

    implementation based on pseudocode found on Wikipedia
    https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
    """
    disjSet = DisjointSet()
    A = set()

    for vertex in graph.getAllNodes():
        disjSet.make_set(vertex.getID())
    for (v1, v2) in graph.getAllEdges():
        if disjSet.find_set(v1) != disjSet.find_set(v2):
            A.add((v1, v2))
            disjSet.union(v1, v2)

    return A


if __name__ == "__main__":
    from AdjacencyMatrix import AdjacencyMatrix
    g1 = AdjacencyMatrix(5)
    g1.connectNodes(0, 3)
    g1.connectNodes(1, 2)
    g1.connectNodes(1, 3)
    g1.connectNodes(1, 4)
    g1.connectNodes(2, 3)
    g1.connectNodes(2, 4)

    print("testcase for mst")
    print(mst(g1))
    print("Should show (ORDER DOESN'T MATTER!)")
    print({(1, 2), (3, 0), (3, 2), (1, 4)})
