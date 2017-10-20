# -*- coding: utf-8 -*-
"""Implements depth-first graph search with a visitor callback"""

# dfs inspired by the excellent blog post by edd mann
# http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

def dfs(graph, start, visitorCallback=lambda x: x):
    """callback is optional. Depth-first search, start should be a node, not an id"""
    visited = set()
    stack = [start]

    try:
        start.getID()
    except:
        print("Warning: `start` argument should be a node, not an ID")

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            visitorCallback(vertex)
            # yep, set arithmetic is beautiful <3
            stack.extend(graph.getAllNodesConnectedTo(vertex) - visited)

    return visited


if __name__ == "__main__":
    from AdjacencyMatrix import AdjacencyMatrix
    g1 = AdjacencyMatrix(5)
    g1.connectNodes(1, 3)
    g1.connectNodes(2, 4)
    g1.connectNodes(2, 3)
    g1.connectNodes(0, 3)

    print("testcase for dfs")
    dfs(g1, g1.nodes[0], lambda n: print(n))
    print("Should show 0 3 1 2 4")
