from dfs import dfs
from graphUtils import countGridEdges, isConnectedGraph
import random

CUTPERCENTAGE = .3

def roomConnector(graph):
    """Connects rooms in the underlying adjacency matrix (graph)
       constraints:
       1. Each room may only be connected to direct XY-coordinate neighbors
       2. Each room must be reachable

       The algorithm to reach these goals is far from perfect, but it should work
       the main problems are

       1. Unpredictable time-complexity due to randomness
       2. Uses tons and tons of memory due to copying, copying of graphs
       3. Probably fairly slow as well

       BUT. It works, and it works fairly robustly

       (manually tested @Thursday - 19 October 2017)
       for
       Graph(X=4, Y=8),
       Graph(X=7, Y=2)
       Graph(X=5, Y=5)
       where X and Y are the dungeonConfigs
    """

    numEdges = countGridEdges(graph.config["X"], graph.config["Y"])
    edgesToCut = int(numEdges * CUTPERCENTAGE)
    edges = graph.getAllEdges()

    while edgesToCut:
        edge = random.choice(list(edges))

        gcopy = graph.deepCopy()
        gcopy.disconnectNodes(edge[0], edge[1])

        if isConnectedGraph(gcopy):
            graph.disconnectNodes(edge[0], edge[1])
            edgesToCut -= 1
