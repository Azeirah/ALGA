"""Implementation of a breadth-first search"""

# bfs inspired by the excellent blog post by edd mann
# adapted to meet my requirements
# http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

def bfs_paths(graph, start, goal):
    # first element keeps track of shortest path
    # second element keeps track of what nodes need to be visited
    queue = [(start, [start])]

    try:
        start.getID()
        goal.getID()
    except:
        print("Warning: `start` and `goal` arguments must be nodes, not ID's")

    while queue:
        (vertex, path) = queue.pop(0)
        for nxt in graph.getAllNodesConnectedTo(vertex) - set(path):
            if nxt == goal:
                # yield whenever the shortest path is reached
                yield path + [nxt]
            else:
                queue.append((nxt, path + [nxt]))


def shortestPath(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None


if __name__ == "__main__":
    from AdjacencyMatrix import AdjacencyMatrix
    g1 = AdjacencyMatrix(5)
    g1.connectNodes(1, 3)
    g1.connectNodes(2, 4)
    g1.connectNodes(2, 3)
    g1.connectNodes(0, 3)

    print("length from 0 to 3 should be 2. Is " + str(len(shortestPath(g1, g1.nodes[0], g1.nodes[3]))))
    print("length from 0 to 4 should be 4. Is " + str(len(shortestPath(g1, g1.nodes[0], g1.nodes[4]))))

