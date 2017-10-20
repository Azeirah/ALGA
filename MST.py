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




def mst(graph, visitorCallback=lambda x: x):
    """Minimum spanning tree using some version of Prim's algorithm
    Note that this algorithm is only tested on unweighted graphs.
    The step of sorting weights is skipped.

    implementation based on pseudocode found on Wikipedia
    https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
    """
    disjSet = DisjointSet()
    A = set()

    for vertex in graph.getAllNodes():
        disjSet.make_set(vertex.getID())
    for (v1, v2) in graph.getAllEdges():
        if disjSet.find_set(v1) != disjSet.find_set(v2):
            A = A.union((v1, v2))
            disjSet.union(v1, v2)

            visitorCallback((v1, v2))

    return A


if __name__ == "__main__":
    from AdjacencyMatrix import AdjacencyMatrix
    g1 = AdjacencyMatrix(5)
    g1.connectNodes(1, 3)
    g1.connectNodes(2, 4)
    g1.connectNodes(2, 3)
    g1.connectNodes(0, 3)

    print("testcase for mst")
    mst(g1, lambda e: print(e[0], e[1]))
    print("Should show:")
    print("3 2")
    print("1 3")
    print("3 0")
    print("4 2")
