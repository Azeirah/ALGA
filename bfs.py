"""Implementation of a breadth-first search"""

# bfs inspired by the excellent blog post by edd mann
# adapted to meet my requirements
# http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

def bfs(graph, start, visitorCallback=lambda x: x):
    visited = set()
    queue = [start]

    try:
        start.getID()
    except:
        print("Warning: `start` argument should be a node, not an ID")

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            visitorCallback(vertex)
            queue.extend(graph.getAllNodesConnectedTo(vertex) - visited)

    return visited


if __name__ == "__main__":
    from AdjacencyMatrix import AdjacencyMatrix
    g1 = AdjacencyMatrix(5)
    g1.connectNodes(1, 3)
    g1.connectNodes(2, 4)
    g1.connectNodes(2, 3)
    g1.connectNodes(0, 3)

    print("testcase for bfs")
    print(bfs(g1, g1.nodes[0]))
    print("Should be {0 3 1 2 4}")
    print(set([node.getID() for node in bfs(g1, g1.nodes[0])]) == {0, 3, 1, 2, 4})
