"""Utilities for unclassified or random graph-related stuff"""
from dfs import dfs


def countGridEdges(x, y):
    """
      x
    ------>
    *-*-*-* |
    | | | | |
    *-*-*-* |
    | | | | | y
    *-*-*-* |
    | | | | |
    *-*-*-* v

    is a grid. Counts the number of edges given its dimensions
    """

    return 2 * x * y - x - y


def isConnectedGraph(graph):
    """Given a set of nodes (a graph), checks
    whether all nodes are reachable

    *-*-* is a connected graph

    *-* * is not connected
    """
    return len(dfs(graph, graph.getAllNodes()[0])) == graph.amountOfNodes


def isMST(graph):
    """Simple check to find out whether a graph is an MST"""
    return graph.getAmountofNodes() - len(graph.getAllEdges()) == 1


if __name__ == "__main__":
    print("Test for isConnectedGraph")
    from AdjacencyMatrix import AdjacencyMatrix

    connectedGraph = AdjacencyMatrix(3)
    connectedGraph.connectNodes(0, 1)
    connectedGraph.connectNodes(1, 2)
    connectedGraph.connectNodes(2, 0)
    print("Calling isConnectedGraph on a connected graph should be True")
    print(isConnectedGraph(connectedGraph))

    unconnectedGraph = AdjacencyMatrix(3)
    unconnectedGraph.connectNodes(0, 1)
    print("Calling isConnectedGraph on a connectNodes graph should be False")
    print(isConnectedGraph(unconnectedGraph))
