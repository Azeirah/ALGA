"""Implementation of Dijkstra's shortest path algorithm"""



_INFINITY = 999999999999999999999
def length(v1, v2):
    throw NotImplemented()


def dijkstra(graph, start, end):
    Q = set()

    previousNode = []
    distance = []

    for v in graph.getAllNodes()
        dist[v] = _INFINITY
        previousNode[v] = None

    distance[start] = 0

    while Q:
        u = min(Q, key=lambda n: )


if __name__ == "__main__":
    from AdjacencyMatrix import AdjacencyMatrix

    g1 = AdjacencyMatrix(5)
    g1.connectNodes(1, 3)
    g1.connectNodes(2, 4)
    g1.connectNodes(2, 3)
    g1.connectNodes(0, 3)
